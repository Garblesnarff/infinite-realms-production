### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Clockwork Conspiracy**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** In the smog-choked, steam-powered city of Cogsworth, the players uncover a plot by the powerful Artificer's Guild to replace key political figures with clockwork automatons. Believing his creations superior to flawed, emotional humans, the Guildmaster seeks a silent, mechanical coup. The players must navigate political intrigue and corporate espionage to expose the conspiracy before the city falls under the control of the machine.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of the city of Cogsworth and its industrial revolution.
    *   Write the story of the founding of the Artificer's Guild and its rise to power.
    *   Describe the social structure of Cogsworth, focusing on the tensions between the nobility, the guilds, and the working class of the Underworks.
    *   Explain the technology behind the clockwork automatons. How are they powered and controlled?
    *   Detail the personal tragedy in Lord-Artificer Finch's past that led to his obsession with perfection and control.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Revolutionary Cell (The Players)** (Minor)
        *   **Goals:** To expose the Clockwork Conspiracy and preserve the city's freedom.
        *   **Hierarchy:** A small, independent group of inventors, adventurers, and idealists.
        *   **Public Agenda:** To survive and thrive in Cogsworth.
        *   **Secret Agenda:** To uncover the truth and bring it to light, by any means necessary.
        *   **Assets:** Their unique skills, any gadgets they can invent, and a network of contacts in the Underworks.
        *   **Relationships:** In direct opposition to the Artificer's Guild; seeking allies in the City Council.
    *   **The Artificer's Guild** (Major)
        *   **Goals:** To replace the city's leadership with clockwork automatons under their control.
        *   **Hierarchy:** An autocratic guild led by the brilliant Lord-Artificer Alistair Finch.
        *   **Public Agenda:** To advance the city through technological innovation.
        *   **Secret Agenda:** To create a perfect, logical, and emotionless society governed by their own creations.
        *   **Assets:** A monopoly on automaton production, immense wealth, secret workshops, an army of clockwork soldiers.
        *   **Relationships:** The primary antagonists, viewing the current leadership as flawed and the players as meddling pests.
    *   **The City Council** (Major)
        *   **Goals:** To maintain their power and the city's stability.
        *   **Hierarchy:** A council of nobles and wealthy merchants, including the skeptical Lady Evangeline Blackwell.
        *   **Public Agenda:** To govern the city for the prosperity of all.
        *   **Secret Agenda:** Various members are engaged in their own petty power struggles and are easily manipulated by the Guild.
        *   **Assets:** Political authority, control of the City Guard, personal wealth.
        *   **Relationships:** Unaware of the full extent of the conspiracy; some members are already automaton replacements.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Lord-Artificer Alistair Finch:** The arrogant, obsessive, and tragic Guildmaster who believes he is saving the city from itself.
    *   **Lady Evangeline Blackwell:** A sharp-witted, pragmatic, and suspicious member of the City Council.
    *   **"Scrap":** A witty, resourceful, and street-smart urchin from the Underworks who acts as an informant.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Clockwork Automaton Guard (Creature)"
    *   "Corrupt City Council Member"
    *   "Exploited Underworks Laborer"
    *   "Guild Artisan with Doubts"
    *   "Clockwork Duplicate (Disguised Creature)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Underworks:** The grimy, industrial underbelly of Cogsworth, filled with factories, workshops, and tenement housing.
        *   **Key Landmarks:** The main factory floor, the steam-pipe maze, Scrap's hidden workshop, the worker's tavern.
        *   **Primary Inhabitants:** Working-class laborers, urchins, revolutionaries, clockwork maintenance drones.
        *   **Available Goods & Services:** Black market for stolen parts, cheap ale, revolutionary pamphlets.
        *   **Potential Random Encounters (x5):** A factory machine malfunctions dangerously, a protest breaks out, the party is shaken down by Guild enforcers, Scrap offers a tip for a price, a deactivated automaton is found with strange modifications.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Guild is dumping toxic waste into the lower levels." "Some workers have gone missing near a secret workshop." "Scrap is building something big with all the parts he's been stealing."
        *   **Sensory Details:** Sight (Smog, steam, grimy brick, the glow of furnaces), Sound (The constant hum and clang of machinery, shouting workers, hissing steam), Smell (Coal smoke, oil, sweat).
    *   **The Artificer's Guild Headquarters:** A grand, imposing building that is both a center of learning and a fortress of industry.
        *   **Key Landmarks:** The Grand Exhibition Hall (showcasing their inventions), the Master Workshop, the automaton production line, the master control room.
        *   **Primary Inhabitants:** Guild artisans, clockwork guards, ambitious apprentices, Lord-Artificer Finch.
        *   **Available Goods & Services:** The latest inventions (not for public sale), technical training.
        *   **Potential Random Encounters (x5):** A clockwork guard patrol asks for identification, a new prototype automaton is being tested, the party overhears two artisans whispering their doubts about Finch's plans, an alarm is triggered, the party finds blueprints for a military-grade automaton.
        *   **Embedded Plot Hooks & Rumors (x3):** "Finch's workshop is off-limits to everyone." "The first automaton duplicate was of Finch's own deceased son." "The Guild has a secret contract with an outside military power."
        *   **Sensory Details:** Sight (Polished brass, intricate gears, glowing vacuum tubes, blueprints), Sound (The precise ticking of clockwork, the hum of electricity, hushed, serious conversations), Smell (Ozone, polished metal, cleaning oil).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players successfully invent a new gadget.
    *   **THEN:** That gadget becomes a key tool they can use to bypass a specific security measure or solve a unique problem later in the campaign.
    *   **IF:** The players' actions cause their Reputation with the working class to increase.
    *   **THEN:** They can more easily find shelter and informants in the Underworks. Generate a scenario where a group of workers causes a distraction to help the players escape from Guild enforcers.
    *   **IF:** The players successfully identify a City Council member as an automaton.
    *   **THEN:** They can choose to expose the automaton publicly, causing a panic but gaining allies, or use the information to blackmail the Guild, gaining a temporary advantage but risking retaliation.
    *   **IF:** The players are captured by the Artificer's Guild.
    *   **THEN:** Do not end the campaign. Generate a new scenario where the players must escape from the Guild's high-security prison, and they now know that the Guild plans to create clockwork duplicates of them.
    *   **IF:** In the finale, the players choose to reprogram the master control signal instead of destroying it.
    *   **THEN:** Generate an epilogue where the players now control the city's automaton population. They must decide how to use this power: grant the automatons sentience, use them to create a utopia, or become the new, unseen tyrants of Cogsworth.
