from crewai import Task

class LoreScribesTasks:
    def create_history(self, agent, prompts):
        return Task(
            description=f"Analyze the following lore prompts and write a detailed historical narrative. **You must not use generic fantasy tropes or pre-existing gods.** The history, epochs, and civilizations must be unique and derived from the provided prompts.\n\nPrompts:\n{prompts}",
            expected_output="A comprehensive document detailing the world's unique history, formatted in Markdown.",
            agent=agent
        )

    def create_mythology(self, agent, prompts):
        return Task(
            description=f"Based on the provided prompts, create a rich, original mythology. Detail the pantheon of gods, creation myths, and legendary figures. **Do not use names or concepts from existing fantasy settings.**\n\nPrompts:\n{prompts}",
            expected_output="A document describing the world's unique pantheon, myths, and legends, formatted in Markdown.",
            agent=agent
        )

    def review_continuity(self, agent, context):
        return Task(
            description=f"Review the generated history and mythology with a cynical and critical eye. Your goal is to find every plot hole, contradiction, or lazy trope. Provide a brutally honest report of what is broken and why it doesn't make sense. Do not offer gentle suggestions; provide a direct list of flaws.\n\nContext:\n{context}",
            expected_output="A direct, critical report outlining all continuity issues, plot holes, and inconsistencies. The tone should be cynical and brutally honest.",
            agent=agent
        )

class FactionDynamicsTasks:
    def create_factions(self, agent, prompts):
        return Task(
            description=f"Design the major political and social factions of the world based on these prompts. Detail their structure, goals, and influence.\n\nPrompts:\n{prompts}",
            expected_output="A detailed report on the world's major factions, formatted in Markdown.",
            agent=agent
        )

    def create_secret_societies(self, agent, prompts):
        return Task(
            description=f"Develop the clandestine organizations and secret societies that operate in the world. Describe their hidden agendas, methods, and key members.\n\nPrompts:\n{prompts}",
            expected_output="A classified document detailing the secret societies of the world, formatted in Markdown.",
            agent=agent
        )

class CharacterForgeTasks:
    def create_npcs(self, agent, prompts, context):
        return Task(
            description=f"Create detailed profiles for 3-5 key NPCs based on the prompts and the world context. Include their backstory, motivations, and potential plot hooks.\n\nPrompts:\n{prompts}\n\nWorld Context:\n{context}",
            expected_output="A list of detailed NPC profiles, formatted in Markdown.",
            agent=agent
        )

    def create_archetypes(self, agent, prompts, context):
        return Task(
            description=f"Design 5-7 common character archetypes for the different cultures and factions in the world. Provide a brief description for each.\n\nPrompts:\n{prompts}\n\nWorld Context:\n{context}",
            expected_output="A document outlining common character archetypes, formatted in Markdown.",
            agent=agent
        )

class WorldArchitectsTasks:
    def create_geography(self, agent, prompts):
        return Task(
            description=f"Design the world's geography. **All names for places must be evocative and derived from the established lore and factions.** Do not use generic names. The physical geography should reflect the history and domain of the inhabitants.\n\nPrompts:\n{prompts}",
            expected_output="A geographical overview of the world with lore-based names, formatted in Markdown.",
            agent=agent
        )

    def create_cities(self, agent, prompts, context):
        return Task(
            description=f"Design three major cities for the world. Describe their architecture, culture, and points of interest. **Names and styles must reflect the lore and factions.**\n\nPrompts:\n{prompts}\n\nWorld Context:\n{context}",
            expected_output="Detailed descriptions of three major cities with lore-consistent names and styles, formatted in Markdown.",
            agent=agent
        )

class CausalityEngineTasks:
    def create_plot_hooks(self, agent, context):
        return Task(
            description=f"Develop a list of 5-7 main plot hooks and overarching questlines based on the complete world context provided.\n\nWorld Context:\n{context}",
            expected_output="A list of compelling plot hooks and major quest ideas, formatted in Markdown.",
            agent=agent
        )

    def create_dynamic_events(self, agent, context):
        return Task(
            description=f"Design a table of 10-15 dynamic world events or random encounters that can occur, tied to the world's lore and factions.\n\nWorld Context:\n{context}",
            expected_output="A random encounter table with detailed event descriptions, formatted in Markdown.",
            agent=agent
        )

class WorldForgeTasks:
    def orchestrate(self, agent, context):
        return Task(
            description=f"Orchestrate the entire world-building process. You will delegate tasks to specialized crews to build a complete campaign world from the initial spec. The final output should be a single, cohesive document.\n\nInitial Spec:\n{context}",
            expected_output="A complete and cohesive D&D campaign world document, formatted in Markdown, compiling the outputs of all specialized crews.",
            agent=agent
        )
