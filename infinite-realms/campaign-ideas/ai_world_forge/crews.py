from crewai import Crew, Process, Task
from agents import LoreScribesAgents, FactionDynamicsAgents, CharacterForgeAgents, WorldArchitectsAgents, CausalityEngineAgents, WorldForgeAgents
from tasks import LoreScribesTasks, FactionDynamicsTasks, CharacterForgeTasks, WorldArchitectsTasks, CausalityEngineTasks, WorldForgeTasks
from llm_config import get_gemini_llm, get_openrouter_llm

def create_lore_scribes_crew(llm, prompts):
    agents = LoreScribesAgents()
    tasks = LoreScribesTasks()

    historian_agent = agents.historian(llm)
    mythologist_agent = agents.mythologist(llm)
    continuity_editor_agent = agents.continuity_editor(llm)

    history_task = tasks.create_history(historian_agent, prompts)
    mythology_task = tasks.create_mythology(mythologist_agent, prompts)
    
    # The continuity task should depend on the outputs of the first two
    continuity_task = tasks.review_continuity(
        agent=continuity_editor_agent,
        context=[history_task, mythology_task]
    )

    crew = Crew(
        agents=[historian_agent, mythologist_agent, continuity_editor_agent],
        tasks=[history_task, mythology_task, continuity_task],
        process=Process.sequential,
        verbose=True
    )
    return crew

def create_faction_dynamics_crew(llm, prompts):
    agents = FactionDynamicsAgents()
    tasks = FactionDynamicsTasks()

    political_analyst_agent = agents.political_analyst(llm)
    covert_operative_agent = agents.covert_operative(llm)

    factions_task = tasks.create_factions(political_analyst_agent, prompts)
    secret_societies_task = tasks.create_secret_societies(covert_operative_agent, prompts)

    crew = Crew(
        agents=[political_analyst_agent, covert_operative_agent],
        tasks=[factions_task, secret_societies_task],
        process=Process.sequential,
        verbose=True
    )
    return crew

def create_character_forge_crew(llm, prompts, context):
    agents = CharacterForgeAgents()
    tasks = CharacterForgeTasks()

    character_profiler_agent = agents.character_profiler(llm)
    archetype_designer_agent = agents.archetype_designer(llm)

    npcs_task = tasks.create_npcs(character_profiler_agent, prompts, context)
    archetypes_task = tasks.create_archetypes(archetype_designer_agent, prompts, context)

    crew = Crew(
        agents=[character_profiler_agent, archetype_designer_agent],
        tasks=[npcs_task, archetypes_task],
        process=Process.sequential,
        verbose=True
    )
    return crew

def create_world_architects_crew(llm, prompts, context):
    agents = WorldArchitectsAgents()
    tasks = WorldArchitectsTasks()

    lead_architect_agent = agents.lead_architect(llm)
    urban_planner_agent = agents.urban_planner(llm)

    geography_task = tasks.create_geography(lead_architect_agent, prompts)
    cities_task = tasks.create_cities(urban_planner_agent, prompts, context)

    crew = Crew(
        agents=[lead_architect_agent, urban_planner_agent],
        tasks=[geography_task, cities_task],
        process=Process.sequential,
        verbose=True
    )
    return crew

def create_causality_engine_crew(llm, context):
    agents = CausalityEngineAgents()
    tasks = CausalityEngineTasks()

    lead_scripter_agent = agents.lead_scripter(llm)
    event_planner_agent = agents.event_planner(llm)

    plot_hooks_task = tasks.create_plot_hooks(lead_scripter_agent, context)
    dynamic_events_task = tasks.create_dynamic_events(event_planner_agent, context)

    crew = Crew(
        agents=[lead_scripter_agent, event_planner_agent],
        tasks=[plot_hooks_task, dynamic_events_task],
        process=Process.sequential,
        verbose=True
    )
    return crew


class WorldForgeCrew:
    def __init__(self, markdown_content, gemini_llm_instance, openrouter_llm_configs):
        self.markdown_content = markdown_content
        self.gemini_llm_instance = gemini_llm_instance
        self.openrouter_llm_configs = openrouter_llm_configs
        self.prompts = self._parse_markdown(markdown_content)

    def _parse_markdown(self, content):
        sections = content.split('## ')
        prompts = {section.split('\n')[0].strip(): '\n'.join(section.split('\n')[1:]).strip() for section in sections if section}
        return prompts

    def run(self):
        # Initialize specific LLMs for each crew
        # Re-adding 'openrouter/' prefix as required by ChatLiteLLM for OpenRouter models
        lore_llm = get_openrouter_llm(self.openrouter_llm_configs["Lore Scribes Crew"])
        faction_llm = get_openrouter_llm(self.openrouter_llm_configs["Faction Dynamics Crew"])
        character_llm = get_openrouter_llm(self.openrouter_llm_configs["Character Forge Crew"])
        world_llm = get_openrouter_llm(self.openrouter_llm_configs["World Architects Crew"])
        causality_llm = get_openrouter_llm(self.openrouter_llm_configs["Causality Engine Crew"])
        master_llm = get_openrouter_llm(self.openrouter_llm_configs["World-Forge Crew"])

        # 1. Lore Scribes Crew (now includes continuity review)
        lore_crew = create_lore_scribes_crew(lore_llm, self.prompts.get("Lore", ""))
        lore_result = lore_crew.kickoff()
        
        # The result from the crew will be the output of the last task, which is the continuity review.
        # We need to reconstruct the full lore including the initial history and mythology.
        # Assuming the continuity task output is just the review, we need the outputs from the other tasks.
        # A better way is to have the continuity agent return the *full corrected text*.
        # For now, let's grab the outputs from the tasks directly.
        history_output = lore_crew.tasks[0].output.raw
        mythology_output = lore_crew.tasks[1].output.raw
        continuity_output = lore_crew.tasks[2].output.raw

        full_lore = f"{history_output}\n\n{mythology_output}\n\n## Continuity Review\n{continuity_output}"

        # 2. Faction Dynamics
        faction_crew = create_faction_dynamics_crew(faction_llm, self.prompts.get("Factions", ""))
        faction_result = faction_crew.kickoff()

        # 3. World Architects
        world_architects_crew = create_world_architects_crew(world_llm, self.prompts.get("World", ""), full_lore)
        world_architects_result = world_architects_crew.kickoff()

        # 4. Character Forge
        character_context = f"{full_lore}\n\n{faction_result}\n\n{world_architects_result}"
        character_forge_crew = create_character_forge_crew(character_llm, self.prompts.get("Characters", ""), character_context)
        character_forge_result = character_forge_crew.kickoff()

        # 5. Causality Engine
        final_context = f"{character_context}\n\n{character_forge_result}"
        causality_engine_crew = create_causality_engine_crew(causality_llm, final_context)
        causality_engine_result = causality_engine_crew.kickoff()

        # Final Compilation
        final_world = f"""
# The Campaign World

## World Lore and History
{full_lore}

## Factions and Secret Societies
{faction_result}

## Geography and Locations
{world_architects_result}

## Key NPCs and Archetypes
{character_forge_result}

## Plot Hooks and Dynamic Events
{causality_engine_result}
"""
        return final_world