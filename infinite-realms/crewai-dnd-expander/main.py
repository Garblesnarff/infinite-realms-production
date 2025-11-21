import os
import json
import uuid
from typing import Dict, Any, List
from dotenv import load_dotenv
from pydantic import BaseModel, Field, validator
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import markdown
import re
import argparse
import glob
import os
from pathlib import Path
from datetime import datetime
from supabase import create_client, Client
import sys
from tqdm import tqdm

# Load environment variables
load_dotenv()

# OpenRouter API key (user needs to set this)
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
MODELS = json.loads(os.getenv('MODELS', '{}'))

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

class Campaign(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    genre: str
    difficulty_level: str
    campaign_length: str
    tone: str
    setting_details: Dict[str, Any] = {}
    thematic_elements: Dict[str, List[str]] = Field(default_factory=lambda: {"mainThemes": [], "keyLocations": [], "importantNPCs": [], "recurringMotifs": []})

class World(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    campaign_id: str
    name: str
    description: str
    climate_type: str
    magic_level: str
    technology_level: str

class NPC(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    world_id: str
    name: str
    race: str
    class_: str  # 'class' is reserved
    level: int = 1
    description: str
    personality: str
    stats: Dict[str, Any]

class Quest(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    campaign_id: str
    title: str
    description: str
    difficulty: str
    quest_type: str
    prerequisites: Dict[str, Any] = {}
    rewards: Dict[str, Any] = {}

class Location(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    world_id: str
    name: str
    location_type: str
    description: str
    parent_location_id: str | None = None
    coordinates: Dict[str, Any] | None = None

class CampaignOutput(BaseModel):
    campaign: Campaign
    worlds: List[World]
    npcs: List[NPC]
    quests: List[Quest]
    locations: List[Location]
    factions: List[Dict[str, Any]] = []
    history_events: List[Dict[str, Any]] = []
    memories: List[Dict[str, Any]] = []
    # Add more as needed

def create_llm(model_name: str):
    """Create LLM instance for OpenRouter using ChatOpenAI"""
    # OpenRouter model names might need prefixing
    if model_name.startswith('google/'):
        display_name = model_name
    else:
        display_name = f"openrouter/{model_name}"
    
    return ChatOpenAI(
        model=model_name,
        api_key=OPENROUTER_API_KEY,
        base_url=OPENROUTER_BASE_URL,
        temperature=0.7,
        model_kwargs={"headers": {"HTTP-Referer": "http://localhost:3000", "X-Title": "D&D Campaign Expander"}}
    )

# Define Agents (verbose set dynamically)
def create_agents(verbose: bool = True):
    return {
        'idea_parser': Agent(
            role='Campaign Idea Parser',
            goal='Extract structured data from Markdown campaign ideas and map to Supabase schema',
            backstory="""You are an expert at parsing D&D campaign outlines from Markdown files. 
            You identify key elements like premise, arcs, NPCs, locations, and mechanics, then structure 
            them into JSON compliant with the Supabase campaigns, worlds, npcs, quests, and locations tables.""",
            llm=create_llm(MODELS.get('gemini', 'google/gemini-2.5-flash-lite-exp')),
            verbose=verbose,
            allow_delegation=False
        ),
        'campaign_architect': Agent(
            role='Campaign Architect',
            goal='Design full campaign structure ensuring 5E compatibility and balanced progression',
            backstory="""You are a master D&D campaign designer with deep knowledge of 5E rules. 
            You take parsed ideas and expand them into complete arcs, session plans, and quest flows 
            that fit the schema's campaign_length, difficulty_level, and level progression.""",
            llm=create_llm(MODELS.get('deepseek', 'deepseek/deepseek-chat-v3.1:free')),
            verbose=verbose,
            allow_delegation=False
        ),
        'world_builder': Agent(
            role='World Builder',
            goal='Create detailed world lore, locations, and factions from campaign themes',
            backstory="""You are a world-building expert who crafts immersive settings. 
            Generate worlds table entries with climate/magic/tech levels, locations with hierarchies, 
            and factions with relationships, all tied to the campaign_id.""",
            llm=create_llm(MODELS.get('nemotron', 'nvidia/nemotron-nano-9b-v2:free')),
            verbose=verbose,
            allow_delegation=False
        ),
        'npc_designer': Agent(
            role='NPC Designer',
            goal='Generate full 5E stat blocks and personalities for NPCs',
            backstory="""You are a 5E rules expert specializing in NPC creation. 
            Build npcs table entries with race, class, level, personality, and stats JSON 
            (ability scores, HP, AC, etc.) based on campaign needs.""",
            llm=create_llm(MODELS.get('gpt_oss', 'openai/gpt-oss-120b:free')),
            verbose=verbose,
            allow_delegation=False
        ),
        'encounter_planner': Agent(
            role='Encounter Planner',
            goal='Design combats, social encounters, and quests with 5E balance',
            backstory="""You balance deadly encounters and meaningful quests. 
            Create quests table entries and suggest combat_encounters with participants, 
            ensuring CR-appropriate challenges for player levels.""",
            llm=create_llm(MODELS.get('deepseek', 'deepseek/deepseek-chat-v3.1:free')),
            verbose=verbose,
            allow_delegation=False
        ),
        'rules_validator': Agent(
            role='Rules Validator',
            goal='Validate 5E rules compliance and schema integrity',
            backstory="""You are a strict 5E rules lawyer and database schema expert. 
            Review all outputs for balance, terminology, and Supabase constraints (e.g., enums, FKs). 
            Suggest fixes and validate JSON against Pydantic models.""",
            llm=create_llm(MODELS.get('gpt_oss', 'openai/gpt-oss-120b:free')),
            verbose=verbose,
            allow_delegation=False
        ),
        'db_compiler': Agent(
            role='Database Compiler',
            goal='Assemble validated data into import-ready JSON/SQL payloads',
            backstory="""You generate production-ready outputs for Supabase import. 
            Create JSON bundles with proper UUIDs/FKs, SQL INSERT statements, and API payloads. 
            Ensure atomic insertion order (campaigns -> worlds -> etc.).""",
            llm=create_llm(MODELS.get('gemini', 'google/gemini-2.5-flash-lite-exp')),
            verbose=verbose,
            allow_delegation=False
        )
    }

# No static agents - all created dynamically in run_expansion

def parse_markdown_idea(idea_content: str) -> Dict[str, Any]:
    """Parse Markdown campaign idea into structured data"""
    # Extract frontmatter-like data using regex
    title_match = re.search(r'^# (.*)', idea_content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "Untitled Campaign"
    
    # Extract genre/difficulty from the first line
    genre_line = re.search(r'\*([^*]+)\*', idea_content)
    genre_info = genre_line.group(1).strip().split('—') if genre_line else []
    
    # Find core premise
    premise_match = re.search(r'Core Premise.*?:(.*?)(?=\n---|$)', idea_content, re.DOTALL | re.MULTILINE)
    premise = premise_match.group(1).strip() if premise_match else idea_content
    
    # Extract major sections
    sections = {
        'npcs': re.findall(r'###?s*([^#]+?)(?=\n###?s*|$)', idea_content, re.DOTALL | re.MULTILINE),
        'locations': re.findall(r'Key Locations.*?:(.*?)(?=Central Conflict|$)', idea_content, re.DOTALL | re.MULTILINE),
        'story_arcs': re.findall(r'Story Arc.*?:(.*?)(?=Session-by-Session|$)', idea_content, re.DOTALL | re.MULTILINE)
    }
    
    # Basic structured output
    parsed = {
        'campaign': {
            'name': title,
            'description': premise,
            'genre': genre_info[0].strip() if len(genre_info) > 0 else 'Fantasy',
            'difficulty_level': 'medium' if 'medium' in idea_content.lower() else 'hard',
            'campaign_length': 'full' if 'long' in idea_content.lower() else 'short',
            'tone': 'epic' if 'epic' in idea_content.lower() else 'serious'
        },
        'worlds': [{'name': 'Main World', 'description': 'Primary campaign setting'}],
        'npcs': [],
        'quests': [],
        'locations': []
    }
    
    # Extract NPCs
    for npc_section in sections['npcs']:
        npc_name = re.search(r'(\d+\.\s+)?(\*{0,3})([^**]+?)(\*{0,3})', npc_section)
        if npc_name:
            parsed['npcs'].append({
                'name': npc_name.group(3).strip(),
                'description': npc_section.strip()
            })
    
    return parsed

def create_tasks(parsed_data: Dict[str, Any], campaign_id: str | None = None) -> List[Task]:
    campaign_json = json.dumps(parsed_data, indent=2)
    
    # Task 1: Parse the idea (now using pre-parsed data)
    parse_task = Task(
        description=f"""You have pre-parsed campaign data: {campaign_json}
        
        Validate and enhance the extraction. Ensure it maps correctly to Supabase schema:
        - campaigns: name, description, genre, difficulty_level, campaign_length, tone
        - Extract or infer setting_details and thematic_elements from content
        - Identify initial worlds, locations, NPCs, and quest outlines
        - Output clean JSON using the exact Pydantic model structure""",
        agent=idea_parser_agent,
        expected_output="Clean, validated JSON with Campaign, World, NPC, Quest, Location objects matching Pydantic models"
    )
    
    # Task 2: Architect the campaign
    architect_task = Task(
        description="""Expand the parsed data into a full campaign outline. 
        Ensure 5E level progression (e.g., start level 1-5 to end 15+), balanced arcs, 
        and quest dependencies. Update quests and add session structure.""",
        agent=campaign_architect_agent,
        context=[parse_task],
        expected_output="Detailed campaign architecture with expanded quests and arcs"
    )
    
    # Task 3: Build the world
    world_task = Task(
        description="""From the campaign architecture, generate detailed world entries. 
        Infer climate_type, magic_level, technology_level from genre. 
        Create hierarchical locations and initial factions.""",
        agent=world_builder_agent,
        context=[architect_task],
        expected_output="List of World and Location Pydantic models, linked to campaign_id"
    )
    
    # Task 4: Design NPCs
    npc_task = Task(
        description="""Create full NPC profiles with 5E stat blocks. 
        Generate stats JSON with ability scores, HP, AC, skills, etc. 
        Ensure personalities fit the campaign tone.""",
        agent=npc_designer_agent,
        context=[world_task],
        expected_output="List of NPC Pydantic models with complete 5E stats"
    )
    
    # Task 5: Plan encounters
    encounter_task = Task(
        description="""Design main quests and encounters. 
        Create quests table entries with prerequisites/rewards. 
        Suggest combat_encounters with balanced monsters/NPCs.""",
        agent=encounter_planner_agent,
        context=[npc_task],
        expected_output="Expanded Quest list and encounter outlines"
    )
    
    # Task 6: Validate
    validate_task = Task(
        description="""Review all outputs for 5E rules accuracy (balance, mechanics) 
        and Supabase schema compliance (constraints, FKs, enums). 
        Fix any issues and validate against Pydantic models.""",
        agent=rules_validator_agent,
        context=[encounter_task],
        expected_output="Validated, corrected campaign data ready for compilation"
    )
    
    # Task 7: Compile for DB
    compile_task = Task(
        description=f"""Assemble into CampaignOutput Pydantic model. 
        Generate JSON bundle, SQL INSERT statements (in insertion order), 
        and Supabase API payloads. Use campaign_id: {campaign_id or 'new UUID'}.
        Include optional Markdown export.""",
        agent=db_compiler_agent,
        context=[validate_task],
        expected_output="CampaignOutput model with import-ready JSON/SQL"
    )
    
    return [parse_task, architect_task, world_task, npc_task, encounter_task, validate_task, compile_task]

def run_expansion(idea_file_path: str, campaign_id: str | None = None, output_dir: str = "output") -> CampaignOutput:
    """Main function to run the CrewAI expansion"""
    if not OPENROUTER_API_KEY or OPENROUTER_API_KEY == 'your_api_key_here':
        raise ValueError("Please set your OpenRouter API key in .env")
    
    # Read and parse the idea file
    with open(idea_file_path, 'r') as f:
        idea_content = f.read()
    
    parsed_data = parse_markdown_idea(idea_content)
    
    # Create agents dynamically
    agents_dict = create_agents(verbose=True)
    agents_list = list(agents_dict.values())
    
    # Create tasks with parsed data
    tasks = create_tasks(parsed_data, campaign_id)
    
    # Create and run Crew
    dnd_crew = Crew(
        agents=agents_list,
        tasks=tasks,
        process=Process.sequential
    )
    
    result = dnd_crew.kickoff()
    
    # Parse output (assuming final task returns JSON string)
    try:
        # Try to extract JSON from the result
        json_match = re.search(r'\{.*\}', result, re.DOTALL)
        if json_match:
            output_data = json.loads(json_match.group())
        else:
            # Fallback: assume the entire result is JSON
            output_data = json.loads(result)
        
        # Validate with Pydantic
        validated_output = CampaignOutput(**output_data)
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
        print(f"Raw output: {result[:500]}...")  # First 500 chars for debugging
        raise ValueError("CrewAI output was not valid JSON. Check agent prompts.")
    except Exception as e:
        print(f"Validation error: {e}")
        raise
    
    # Save outputs
    os.makedirs(output_dir, exist_ok=True)
    
    # JSON bundle
    with open(f"{output_dir}/expanded_campaign.json", "w") as f:
        json.dump(validated_output.dict(), f, indent=2)
    
    # Generate SQL (simplified example)
    sql_content = generate_sql(validated_output)
    with open(f"{output_dir}/import.sql", "w") as f:
        f.write(sql_content)
    
    # Markdown export
    md_content = generate_markdown(validated_output)
    with open(f"{output_dir}/campaign_book.md", "w") as f:
        f.write(md_content)
    
    print(f"Expansion complete! Outputs saved to {output_dir}/")
    return validated_output

def generate_sql(output: CampaignOutput) -> str:
    """Generate SQL INSERT statements with proper escaping"""
    def escape_sql(value):
        if isinstance(value, str):
            return value.replace("'", "''")
        elif isinstance(value, dict) or isinstance(value, list):
            return json.dumps(value).replace("'", "''")
        return str(value)
    
    sql = "-- Supabase Import SQL for D&D Campaign\n"
    sql += "-- WARNING: Review and adjust timestamps/user_ids as needed\n\n"
    
    # Campaigns table
    campaign = output.campaign
    sql += f"""INSERT INTO public.campaigns 
(id, name, description, genre, difficulty_level, status, campaign_length, tone, 
 setting_details, thematic_elements, created_at, updated_at) 
VALUES ('{campaign.id}', '{escape_sql(campaign.name)}', '{escape_sql(campaign.description)}', 
        '{escape_sql(campaign.genre)}', '{escape_sql(campaign.difficulty_level)}', 'active', 
        '{escape_sql(campaign.campaign_length)}', '{escape_sql(campaign.tone)}', 
        '{escape_sql(campaign.setting_details)}', '{escape_sql(campaign.thematic_elements)}', 
        '{datetime.now()}', '{datetime.now()}' );\n\n"""
    
    # Worlds table
    for world in output.worlds:
        sql += f"""INSERT INTO public.worlds 
(id, campaign_id, name, description, climate_type, magic_level, technology_level, 
 created_at, updated_at) 
VALUES ('{world.id}', '{world.campaign_id}', '{escape_sql(world.name)}', 
        '{escape_sql(world.description)}', '{escape_sql(world.climate_type)}', 
        '{escape_sql(world.magic_level)}', '{escape_sql(world.technology_level)}', 
        '{datetime.now()}', '{datetime.now()}' );\n"""
    sql += "\n"
    
    # Locations table
    for location in output.locations:
        parent_id = location.parent_location_id or "NULL"
        coords = escape_sql(location.coordinates) if location.coordinates else "{}"
        sql += f"""INSERT INTO public.locations 
(id, world_id, name, location_type, description, parent_location_id, coordinates, 
 created_at, updated_at) 
VALUES ('{location.id}', '{location.world_id}', '{escape_sql(location.name)}', 
        '{escape_sql(location.location_type)}', '{escape_sql(location.description)}', 
        {parent_id}, {coords}, '{datetime.now()}', '{datetime.now()}' );\n"""
    sql += "\n"
    
    # NPCs table
    for npc in output.npcs:
        sql += f"""INSERT INTO public.npcs 
(id, world_id, name, race, class, level, description, personality, stats, 
 created_at, updated_at) 
VALUES ('{npc.id}', '{npc.world_id}', '{escape_sql(npc.name)}', 
        '{escape_sql(npc.race)}', '{escape_sql(npc.class_)}', {npc.level}, 
        '{escape_sql(npc.description)}', '{escape_sql(npc.personality)}', 
        '{escape_sql(npc.stats)}', '{datetime.now()}', '{datetime.now()}' );\n"""
    sql += "\n"
    
    # Quests table
    for quest in output.quests:
        prereqs = escape_sql(quest.prerequisites)
        rewards = escape_sql(quest.rewards)
        sql += f"""INSERT INTO public.quests 
(id, campaign_id, title, description, difficulty, quest_type, prerequisites, rewards, status, 
 created_at, updated_at) 
VALUES ('{quest.id}', '{quest.campaign_id}', '{escape_sql(quest.title)}', 
        '{escape_sql(quest.description)}', '{escape_sql(quest.difficulty)}', 
        '{escape_sql(quest.quest_type)}', {prereqs}, {rewards}, 'available', 
        '{datetime.now()}', '{datetime.now()}' );\n"""
    sql += "\n"
    
    # Factions (if any)
    for faction in output.factions:
        faction_id = faction.get('id', str(uuid.uuid4()))
        sql += f"""INSERT INTO public.world_factions 
(id, world_id, name, description, faction_type, influence_level, relationships, 
 created_at, updated_at) 
VALUES ('{faction_id}', '{faction.get('world_id', output.worlds[0].id if output.worlds else '00000000-0000-0000-0000-000000000000')}', 
        '{escape_sql(faction.get('name', 'Unknown Faction'))}', 
        '{escape_sql(faction.get('description', ''))}', 
        '{escape_sql(faction.get('faction_type', 'organization'))}', 
        {faction.get('influence_level', 5)}, 
        '{escape_sql(faction.get('relationships', {}))}', 
        '{datetime.now()}', '{datetime.now()}' );\n"""
    
    sql += "\n-- Note: Add user_id references and review JSON fields for your specific needs\n"
    return sql

def generate_markdown(output: CampaignOutput) -> str:
    """Generate comprehensive human-readable Markdown campaign book"""
    md = f"# {output.campaign.name}\n\n"
    md += f"**Genre:** {output.campaign.genre}  **Difficulty:** {output.campaign.difficulty_level}  **Length:** {output.campaign.campaign_length}  **Tone:** {output.campaign.tone}\n\n"
    md += f"> {output.campaign.description}\n\n"
    
    # Campaign Overview
    md += "## Campaign Overview\n\n"
    md += f"**Setting Details:** {output.campaign.setting_details}\n\n"
    md += "**Thematic Elements:**\n"
    for theme in output.campaign.thematic_elements.get('mainThemes', []):
        md += f"- {theme}\n"
    md += "\n"
    
    # Worlds Section
    md += "## Worlds\n\n"
    for world in output.worlds:
        md += f"### {world.name}\n"
        md += f"**Climate:** {world.climate_type}  **Magic Level:** {world.magic_level}  **Technology:** {world.technology_level}\n\n"
        md += f"{world.description}\n\n"
        
        # Locations for this world
        world_locations = [loc for loc in output.locations if loc.world_id == world.id]
        if world_locations:
            md += "#### Locations\n"
            for loc in world_locations:
                md += f"**{loc.name}** ({loc.location_type})\n{loc.description}\n\n"
    
    # NPCs Section
    md += "## Major NPCs\n\n"
    for npc in output.npcs:
        md += f"### {npc.name}\n"
        md += f"**Race:** {npc.race}  **Class:** {npc.class_}  **Level:** {npc.level}\n"
        md += f"**Personality:** {npc.personality}\n\n"
        md += f"{npc.description}\n\n"
        
        # Stats block
        if npc.stats:
            md += "#### 5E Stat Block\n"
            md += "```statblock\n"
            for key, value in npc.stats.items():
                if isinstance(value, dict):
                    md += f"{key.upper()}:\n"
                    for subkey, subval in value.items():
                        md += f"  {subkey}: {subval}\n"
                else:
                    md += f"{key}: {value}\n"
            md += "```\n\n"
    
    # Quests Section
    md += "## Main Quests\n\n"
    for quest in output.quests:
        md += f"### {quest.title}\n"
        md += f"**Type:** {quest.quest_type}  **Difficulty:** {quest.difficulty}\n\n"
        md += f"{quest.description}\n\n"
        
        if quest.prerequisites:
            md += "**Prerequisites:**\n"
            for prereq in quest.prerequisites.values():
                md += f"- {prereq}\n"
            md += "\n"
        
        if quest.rewards:
            md += "**Rewards:**\n"
            for reward_type, reward in quest.rewards.items():
                md += f"- {reward_type}: {reward}\n"
        md += "\n"
    
    # Factions
    if output.factions:
        md += "## Factions\n\n"
        for faction in output.factions:
            md += f"### {faction.get('name', 'Unknown Faction')}\n"
            md += f"**Type:** {faction.get('faction_type', 'organization')}  **Influence:** {faction.get('influence_level', 5)}/10\n\n"
            md += f"{faction.get('description', '')}\n\n"
            if faction.get('relationships'):
                md += "**Relationships:**\n"
                for rel, score in faction.get('relationships', {}).items():
                    md += f"- {rel}: {score}\n"
                md += "\n"
    
    # World History
    if output.history_events:
        md += "## World History\n\n"
        for event in output.history_events:
            md += f"### {event.get('event_name', 'Historical Event')}\n"
            md += f"**Significance:** {event.get('significance_level', 3)}/5\n\n"
            md += f"{event.get('description', '')}\n\n"
    
    md += "## DM Notes\n\n"
    md += "- Review all stat blocks for balance\n"
    md += "- Adjust quest difficulties based on party composition\n"
    md += "- Consider player backstories when assigning relationships\n"
    md += "- Use the generated UUIDs for database import\n\n"
    
    md += f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    return md

def slugify_filename(filename: str) -> str:
    """Convert filename to URL-friendly slug"""
    return re.sub(r'[^\w\-_\.]', '-', filename.lower().replace('.md', ''))

def run_interactive_mode():
    """Interactive mode for single campaign expansion"""
    print("=== D&D Campaign Expander - Interactive Mode ===")
    
    # Prompt for file path
    default_path = "../campaign-ideas/aethelgard-the-once-and-future-king.md"
    idea_path = input(f"Enter path to campaign idea (or Enter for default: {default_path}): ").strip()
    if not idea_path:
        idea_path = default_path
    
    if not os.path.exists(idea_path):
        print(f"Error: File '{idea_path}' not found!")
        return 1
    
    # Prompt for campaign ID
    campaign_id = input("Enter existing campaign ID (or Enter for new): ").strip()
    if not campaign_id:
        campaign_id = None
    
    # Prompt for output directory
    output_dir = input("Enter output directory (or Enter for 'output'): ").strip()
    if not output_dir:
        output_dir = "output"
    
    try:
        result = run_expansion(idea_path, campaign_id, output_dir)
        print(f"\n✅ Success! Campaign '{result.campaign.name}' generated in {output_dir}/")
        return 0
    except Exception as e:
        print(f"❌ Error during expansion: {e}")
        return 1

def run_batch_mode(input_dir: str, output_base_dir: str, campaign_id: str | None, verbose: bool, dry_run: bool = False):
    """Batch process all .md files in input directory"""
    print(f"=== D&D Campaign Expander - Batch Mode ===")
    print(f"Input directory: {input_dir}")
    print(f"Output base: {output_base_dir}")
    if dry_run:
        print("Dry run mode: No LLM calls will be made")
    
    # Create output directory
    os.makedirs(output_base_dir, exist_ok=True)
    
    # Find all .md files
    md_files = glob.glob(os.path.join(input_dir, "*.md"))
    if not md_files:
        print(f"No .md files found in {input_dir}")
        return 1
    
    print(f"Found {len(md_files)} campaign ideas to process...")
    
    results = []
    errors = []
    
    for filepath in tqdm(md_files, desc="Processing campaigns"):
        filename = os.path.basename(filepath)
        slug = slugify_filename(filename)
        output_dir = os.path.join(output_base_dir, slug)
        
        if verbose:
            print(f"\n--- Processing: {filename} ---")
        
        try:
            if dry_run:
                # Mock result for dry run
                mock_result = CampaignOutput(
                    campaign=Campaign(
                        name=filename.replace('.md', '').title(),
                        description=f"Mock expansion of {filename}",
                        genre="Fantasy",
                        difficulty_level="medium",
                        campaign_length="full",
                        tone="epic"
                    ),
                    worlds=[World(
                        campaign_id="mock-id",
                        name="Mock World",
                        description="Generated during dry run",
                        climate_type="temperate",
                        magic_level="standard",
                        technology_level="medieval"
                    )],
                    npcs=[NPC(
                        world_id="mock-world-id",
                        name="Mock NPC",
                        race="Human",
                        class_="Fighter",
                        level=5,
                        description="Generated NPC",
                        personality="Brave",
                        stats={}
                    )],
                    quests=[Quest(
                        campaign_id="mock-id",
                        title="Mock Quest",
                        description="Sample quest",
                        difficulty="medium",
                        quest_type="main"
                    )],
                    locations=[Location(
                        world_id="mock-world-id",
                        name="Mock Location",
                        location_type="village",
                        description="Sample location"
                    )]
                )
                results.append({
                    'filename': filename,
                    'campaign_name': mock_result.campaign.name,
                    'output_dir': output_dir,
                    'worlds': len(mock_result.worlds),
                    'npcs': len(mock_result.npcs),
                    'quests': len(mock_result.quests)
                })
                # Create mock output files
                os.makedirs(output_dir, exist_ok=True)
                with open(os.path.join(output_dir, "expanded_campaign.json"), 'w') as f:
                    json.dump(mock_result.dict(), f, indent=2)
                with open(os.path.join(output_dir, "campaign_book.md"), 'w') as f:
                    f.write(f"# Mock Campaign: {mock_result.campaign.name}\n\nGenerated during dry run.")
            else:
                result = run_expansion(filepath, campaign_id, output_dir)
                results.append({
                    'filename': filename,
                    'campaign_name': result.campaign.name,
                    'output_dir': output_dir,
                    'worlds': len(result.worlds),
                    'npcs': len(result.npcs),
                    'quests': len(result.quests)
                })
                if verbose:
                    print(f"✅ {filename} completed: {result.campaign.name}")
        except Exception as e:
            error_msg = f"Failed to process {filename}: {str(e)}"
            errors.append(error_msg)
            if verbose:
                print(f"❌ {error_msg}")
    
    # Generate summary
    summary_path = os.path.join(output_base_dir, "batch_summary.md")
    with open(summary_path, 'w') as f:
        f.write(f"# Batch Processing Summary\n\n")
        f.write(f"**Mode:** {'Dry Run' if dry_run else 'Full'}\n")
        f.write(f"**Processed:** {len(results)} / {len(md_files)} campaigns\n")
        f.write(f"**Errors:** {len(errors)}\n")
        f.write(f"**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        if results:
            f.write("## Successful Campaigns\n\n")
            for r in results:
                f.write(f"- **{r['campaign_name']}** ({r['filename']})\n")
                f.write(f"  - Worlds: {r['worlds']} | NPCs: {r['npcs']} | Quests: {r['quests']}\n")
                f.write(f"  - Output: {r['output_dir']}/\n\n")
        
        if errors:
            f.write("## Errors\n\n")
            for error in errors:
                f.write(f"- {error}\n")
    
    print(f"\n✅ Batch complete! Summary: {summary_path}")
    if errors:
        print(f"⚠️  {len(errors)} errors encountered (see summary)")
    
    return 0 if not errors else 1

def main():
    parser = argparse.ArgumentParser(description="D&D Campaign Expander - Expand ideas into full 5E campaigns")
    parser.add_argument('path', nargs='?', help='Path to single campaign idea Markdown file')
    parser.add_argument('--batch', '-b', action='store_true', help='Batch process all .md files in input directory')
    parser.add_argument('--input-dir', '-i', default='../campaign-ideas/', help='Input directory for batch mode (default: ../campaign-ideas/)')
    parser.add_argument('--output-dir', '-o', default='output', help='Output directory (default: output)')
    parser.add_argument('--campaign-id', help='Existing campaign ID to update (default: generate new)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    parser.add_argument('--dry-run', action='store_true', help='Simulate run without LLM calls (batch only)')
    
    args = parser.parse_args()
    
    # Determine mode
    if args.batch:
        return run_batch_mode(args.input_dir, args.output_dir, args.campaign_id, args.verbose, args.dry_run)
    elif args.path:
        # Single file mode
        if not os.path.exists(args.path):
            print(f"Error: File '{args.path}' not found!")
            return 1
        try:
            result = run_expansion(args.path, args.campaign_id, args.output_dir)
            print(f"\n✅ Success! Campaign '{result.campaign.name}' generated in {args.output_dir}/")
            return 0
        except Exception as e:
            print(f"❌ Error: {e}")
            return 1
    else:
        # Interactive mode
        return run_interactive_mode()

if __name__ == "__main__":
    sys.exit(main())
