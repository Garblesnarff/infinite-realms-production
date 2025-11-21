### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Vanishing Village: Hunters in the Mist**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The remote village of Eldridge has vanished without a trace—every inhabitant gone, leaving behind only empty homes and the faint echo of otherworldly whispers. The players, whether driven by official investigation, personal connections, or sheer curiosity, arrive to find a ghost town that defies all logical explanation. As they piece together clues from scattered personal effects, cryptic journal entries, and strange environmental phenomena, they uncover a horrifying truth: the villagers weren't taken by human hands, but by predators from beyond reality itself. The investigation becomes a desperate race to understand these entities' methods before becoming their next victims.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the founding of Eldridge village and its history as a remote community isolated from mainstream society.
    *   Write the history of similar vanishing events throughout human history and the various explanations that have been proposed.
    *   Describe the nature of the otherworldly predators - their biology, psychology, hunting methods, and motivations.
    *   Explain the "Mist Shroud" phenomenon and its connection to the predators' hunting grounds.
    *   Detail the various investigators and researchers who have studied these phenomena and their ultimate fates.
    *   Write about the "Echo Phenomenon" - the residual psychic impressions left by the vanished and how they can be studied.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Echo Researchers** (Minor)
        *   **Goals:** To study and document the echo phenomenon while developing methods to communicate with otherworldly entities.
        *   **Hierarchy:** Academic council led by researchers with personal connections to vanishing events.
        *   **Public Agenda:** We seek to understand the universe's mysteries through scientific investigation.
        *   **Secret Agenda:** To weaponize echo technology for communication with other planes of existence.
        *   **Assets:** Recording equipment, research facilities, network of investigation sites.
        *   **Relationships:** Cooperative with serious investigators; dismissive of conspiracy theorists and opportunists.
    *   **The Mistwalkers** (Minor)
        *   **Goals:** To navigate and survive in mist-shrouded areas while protecting human settlements from otherworldly threats.
        *   **Hierarchy:** Guild structure led by experienced guides and mist survivors.
        *   **Public Agenda:** We provide safe passage through dangerous mists and protect against supernatural threats.
        *   **Secret Agenda:** To map and control mist phenomena for personal gain.
        *   **Assets:** Mist navigation expertise, protective equipment, hidden outposts.
        *   **Relationships:** Helpful to investigators who respect their expertise; hostile toward those who dismiss mist dangers.
    *   **The Hidden Observers** (Minor)
        *   **Goals:** To monitor otherworldly activity while concealing their existence from both humans and predators.
        *   **Hierarchy:** Secretive cell structure led by anonymous coordinators.
        *   **Public Agenda:** We watch and record, interfering only when necessary to preserve the balance.
        *   **Secret Agenda:** To learn from the predators and potentially establish communication.
        *   **Assets:** Advanced surveillance technology, hidden observation posts, encrypted archives.
        *   **Relationships:** Neutral toward all; willing to provide information to worthy investigators.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Dr. Elias Crowe:** The skeptical scientist providing methodical analysis of otherworldly phenomena.
    *   **The Whispering Guide:** The ambiguous ally existing in a liminal state between human and otherworldly.
    *   **The Lead Hunter:** The intelligent predator who sees the players as worthy prey.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Skeptical Local Official"
    *   "Echo Researcher Assistant"
    *   "Mistwalker Guide"
    *   "Hidden Observer Agent"
    *   "Conspiracy Theorist"
    *   "Vanishing Survivor"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **Eldridge Village:** The perfectly preserved but empty village.
        *   **Key Landmarks:** The Central Well, the Assembly Hall, the Archive Basement, the Outlying Farmsteads.
        *   **Primary Inhabitants:** Echoes of former villagers, occasional predators, investigating outsiders.
        *   **Available Goods & Services:** Abandoned personal effects, historical documents, echo recordings.
        *   **Potential Random Encounters (x5):** An echo manifestation, a predator scouting, discovery of a hidden journal, a fellow investigator seeking collaboration, a sudden mist bank revealing clues.
        *   **Embedded Plot Hooks & Rumors (x3):** "The villagers left messages in the architecture itself." "Some villagers survived by becoming predators." "The village archives contain forbidden knowledge about the entities."
        *   **Sensory Details:** Sight (Perfectly preserved interiors, subtle impossibilities), Sound (Echoing whispers, settling house noises), Smell (Stale air, faded cooking smells).
    *   **The Mist Shroud:** An unnatural fog surrounding the village.
        *   **Key Landmarks:** The Mist Boundary, the Echo Pools, the Predator Trails, the Visibility Rifts.
        *   **Primary Inhabitants:** Mist-adapted creatures, disoriented travelers, predatory entities.
        *   **Available Goods & Services:** Mist essence, echo crystals, navigation guidance.
        *   **Potential Random Encounters (x5):** A predator emerges from the mist, an echo pool reveals visions, discovery of a lost traveler's camp, a mistwalker offers assistance, a visibility rift shows other locations.
        *   **Embedded Plot Hooks & Rumors (x3):** "The mist remembers everything that ever happened here." "Some can use the mist to travel through time." "The predators communicate through the mist's whispers."
        *   **Sensory Details:** Sight (Swirling patterns, occasional glimpses of other places), Sound (Muffled whispers, echoing distortions), Smell (Damp earth, ozone).
    *   **The Archive Chamber:** A hidden basement containing historical records.
        *   **Key Landmarks:** The Record Vault, the Evidence Locker, the Analysis Station, the Secure Vault.
        *   **Primary Inhabitants:** Research equipment, archived documents, the occasional echo guardian.
        *   **Available Goods & Services:** Historical documents, research equipment, classified files.
        *   **Potential Random Encounters (x5):** An echo guardian activates, a document reveals a crucial clue, discovery of classified research, a fellow researcher seeks collaboration, a security system triggers.
        *   **Embedded Plot Hooks & Rumors (x3):** "The archives contain records of similar events dating back centuries." "Some documents were written by the predators themselves." "The chamber connects to other vanished locations."
        *   **Sensory Details:** Sight (Dusty documents, flickering fluorescent lights), Sound (Page turning, distant echoes), Smell (Old paper, dust).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players successfully record and analyze a significant echo.
    *   **THEN:** They gain crucial insights into the predators' methods. Generate increased predator awareness as the entities detect the echo disturbance.
    *   **IF:** The players ally with Dr. Elias Crowe.
    *   **THEN:** They gain access to scientific equipment and analysis. Generate scenarios where his personal vendetta creates complications.
    *   **IF:** The players develop effective anti-predator defenses.
    *   **THEN:** The predators adapt their hunting methods, creating new challenges. Generate opportunities to study the entities' intelligence and adaptability.
    *   **IF:** The players establish communication with the Whispering Guide.
    *   **THEN:** They receive cryptic but valuable guidance. Generate scenarios where the Guide's liminal nature creates unpredictable effects.
    *   **IF:** The players confront the Lead Hunter directly.
    *   **THEN:** They gain understanding of the predators' society and motivations. Generate a scenario where the Hunter attempts to recruit rather than eliminate them.
