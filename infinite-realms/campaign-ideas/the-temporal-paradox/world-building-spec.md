### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Temporal Paradox: Threads of Time**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The players discover an ancient chronal device that allows limited time travel, initially using it to prevent a personal tragedy but accidentally creating a paradox that threatens the timeline itself. As they journey through different historical eras, they must repair the damage they've caused while preventing greater catastrophes from occurring. But with each temporal intervention, the players risk creating worse paradoxes, meeting alternate versions of themselves, and unraveling the fundamental laws of cause and effect. The campaign becomes a delicate balance between fixing history and preserving the timeline's integrity, all while questioning whether some events are destined to happen.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the discovery of temporal mechanics and the development of time travel technology throughout history.
    *   Write the history of the Chrono Guardian and their role in maintaining temporal coherence across civilizations.
    *   Describe the nature of paradoxes and how they have shaped (and been shaped by) historical events.
    *   Explain the physics of temporal travel and the limitations that prevent unlimited time manipulation.
    *   Detail the various historical eras accessible through temporal travel and their unique challenges.
    *   Write about the "Temporal Accord" - the ethical guidelines that govern time travel and the consequences of violating them.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Chrono Wardens** (Major)
        *   **Goals:** To maintain temporal coherence and prevent catastrophic paradoxes while studying historical patterns.
        *   **Hierarchy:** Council of experienced temporal guardians led by the most knowledgeable wardens.
        *   **Public Agenda:** We protect the integrity of time for the benefit of all eras.
        *   **Secret Agenda:** To harness temporal energy for controlling historical outcomes.
        *   **Assets:** Temporal monitoring equipment, historical databases, paradox resolution tools.
        *   **Relationships:** Allied with responsible time travelers; antagonistic toward paradox creators.
    *   **The Timeline Divers** (Major)
        *   **Goals:** To explore alternate timelines and collect unique historical knowledge for personal gain.
        *   **Hierarchy:** Guild structure led by successful divers with extensive temporal experience.
        *   **Public Agenda:** Knowledge of alternate histories benefits everyone.
        *   **Secret Agenda:** To create new timelines where they hold positions of power.
        *   **Assets:** Timeline maps, temporal camouflage, historical artifact collections.
        *   **Relationships:** Competitive with other divers; willing to trade with responsible time travelers.
    *   **The Paradox Cult** (Minor)
        *   **Goals:** To embrace temporal chaos and create a new reality free from linear time constraints.
        *   **Hierarchy:** Theocratic structure led by "Enlightened" individuals who have experienced total temporal freedom.
        *   **Public Agenda:** Linear time is an illusion that must be shattered.
        *   **Secret Agenda:** To collapse all timelines into a single, perfect moment.
        *   **Assets:** Paradox generation devices, temporal anomaly control, mind-altering substances.
        *   **Relationships:** Hostile toward all who maintain temporal order; seek to convert time travelers.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **The Chrono Guardian:** The ancient being who maintains temporal coherence and guides the players.
    *   **Dr. Elara Voss:** The brilliant temporal physicist who provides scientific understanding of time mechanics.
    *   **The Paradox Echo:** The temporal duplicate representing the consequences of the players' choices.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Temporal Researcher"
    *   "Timeline Diver"
    *   "Paradox Cultist"
    *   "Historical Figure"
    *   "Temporal Guardian"
    *   "Paradox Survivor"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Chrono Nexus:** The central hub where all timelines converge.
        *   **Key Landmarks:** The Timeline Core, the Paradox Containment Field, the Historical Archives, the Guardian Sanctum.
        *   **Primary Inhabitants:** Chrono Wardens, temporal researchers, timeline divers, paradox entities.
        *   **Available Goods & Services:** Temporal coordinates, historical data, paradox resolution.
        *   **Potential Random Encounters (x5):** A timeline shift occurs, a paradox entity manifests, discovery of a temporal artifact, a fellow time traveler seeks collaboration, a guardian patrol investigates anomalies.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Nexus contains the original timeline from which all others diverged." "Some guardians are secretly timeline divers." "The core can show every possible future."
        *   **Sensory Details:** Sight (Branching timeline displays, shifting architecture), Sound (Echoing voices from all eras, humming temporal energy), Smell (Ozone from temporal fields, aged parchment).
    *   **The Historical Vaults:** A library of temporal artifacts and documents.
        *   **Key Landmarks:** The Artifact Wing, the Document Archives, the Research Stations, the Conservation Labs.
        *   **Primary Inhabitants:** Historical scholars, artifact conservators, temporal archaeologists.
        *   **Available Goods & Services:** Historical documents, temporal artifacts, research assistance.
        *   **Potential Random Encounters (x5):** An artifact activates unexpectedly, a document reveals a hidden timeline, discovery of a paradox-tainted item, a researcher requests help with a temporal puzzle, a conservation effort goes wrong.
        *   **Embedded Plot Hooks & Rumors (x3):** "The vaults contain items from timelines that never existed." "Some artifacts remember being used in different ways." "The archives hide the true history of time travel."
        *   **Sensory Details:** Sight (Ancient artifacts, glowing data screens), Sound (Page turning, humming scanners), Smell (Dust, old leather).
    *   **The Paradox Realm:** A liminal space where broken timelines manifest.
        *   **Key Landmarks:** The Echo Pools, the Timeline Fragments, the Possibility Storms, the Memory Caves.
        *   **Primary Inhabitants:** Paradox entities, lost time travelers, temporal echoes.
        *   **Available Goods & Services:** Paradox energy, forgotten memories, temporal insights.
        *   **Potential Random Encounters (x5):** A possibility storm reveals alternate choices, an echo pool shows a possible future, discovery of a lost traveler's camp, a paradox entity demands resolution, a memory cave reveals hidden truths.
        *   **Embedded Plot Hooks & Rumors (x3):** "The realm contains every choice that was never made." "Some who enter the memory caves can change their past." "The possibility storms show what could have been."
        *   **Sensory Details:** Sight (Shifting possibilities, fragmented realities), Sound (Whispering choices, echoing memories), Smell (Nothingness, potential).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players successfully resolve a major paradox.
    *   **THEN:** Timeline stability improves, creating new opportunities. Generate decreased paradox activity but increased guardian scrutiny.
    *   **IF:** The players form an alliance with the Chrono Wardens.
    *   **THEN:** They gain access to advanced temporal technology and safe houses. Generate scenarios where the wardens' strict rules create complications.
    *   **IF:** The players create a new timeline branch.
    *   **THEN:** They gain unique resources but attract paradox entities. Generate opportunities to explore the new timeline's possibilities.
    *   **IF:** The players encounter and help their paradox echo.
    *   **THEN:** They gain temporal insights but risk identity confusion. Generate scenarios where the echo's knowledge creates moral dilemmas.
    *   **IF:** The players choose to embrace temporal chaos.
    *   **THEN:** They gain powerful abilities but risk total temporal collapse. Generate scenarios where chaos creates unpredictable opportunities and dangers.
