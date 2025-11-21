### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Long Look**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise. The tone is a slow-burn psychological thriller with occult and conspiracy elements.
*   **Content:** The players are descendants of the original remote viewers from the CIA's real-life "Stargate Project." They inherit a faint echo of psychic talent, which makes them targets for otherworldly entities leaking through the psychic breaches the project created. Recruited by the program's paranoid survivors, they must learn to control their powers to seal these breaches before reality unravels.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the "true" history of the Stargate Project, focusing on its successes and the first contact with the "sideways" realities.
    *   Write a profile on the first entity that was contacted and the immediate, disastrous results.
    *   Describe the nature of "The Breach"—the psychic space between realities.
    *   Explain the different types of entities that leak through (e.g., Echoes, Static Men, Tulpamancers) and the laws that govern them.
    *   Detail the official cover-up of the Stargate Project and the creation of the underground "Network."

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Network (The Players)** (Major)
        *   **Goals:** To identify and seal psychic breaches and protect humanity from otherworldly entities.
        *   **Hierarchy:** A decentralized, underground network of "sensitives" (the players) and grizzled ex-agents.
        *   **Public Agenda:** None. They exist in the shadows.
        *   **Secret Agenda:** To find a permanent way to close the doors opened by the Stargate Project.
        *   **Assets:** Their psychic abilities ("The Sight"), a network of safe houses, and fragmented knowledge from the original project.
        *   **Relationships:** Hunted by government remnants and otherworldly entities.
    *   **The Unwitting (Government Remnants)** (Major)
        *   **Goals:** To erase all evidence of the Stargate Project, including its descendants (the players) and its consequences (the entities).
        *   **Hierarchy:** A black-ops government agency that inherited the Stargate files, but not the full understanding of the threat.
        *   **Public Agenda:** None.
        *   **Secret Agenda:** To capture and weaponize the otherworldly entities, believing them to be a new frontier of espionage.
        *   **Assets:** Government resources, advanced surveillance technology, highly-trained but ignorant field agents.
        *   **Relationships:** A primary antagonist, viewing the players as loose ends or potential assets to be captured.
    *   **The Entities** (Major)
        *   **Goals:** Varies by entity. Some are predatory, some are curious, some are simply lost. Their goals are fundamentally alien.
        *   **Hierarchy:** None. They are disparate beings from different realities.
        *   **Public Agenda:** None.
        *   **Secret Agenda:** To find a way to manifest more fully in our reality, which often has destructive side effects.
        *   **Assets:** The ability to bend or break the laws of physics, psychic powers, the fact that most humans cannot perceive them.
        *   **Relationships:** The primary source of conflict, drawn to the players' psychic "scent."

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **"Codename: Watcher":** An aging, paranoid ex-agent from the original Stargate Project who recruits the players.
    *   **Agent Thorne:** A cold, ruthless field agent from the government remnant agency, tasked with hunting the players.
    *   **The Static Man:** A recurring entity of pure data that corrupts technology and communicates through white noise.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Confused person experiencing a reality glitch"
    *   "G-Man in a black suit"
    *   "An Echo (a person stuck in a time loop)"
    *   "A Tulpa (a physical manifestation of a strong fear)"
    *   "Fellow psychic in the Network"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **A Breach Site (e.g., a public library):** A mundane location where the walls of reality are thin, causing strange phenomena.
        *   **Key Landmarks:** The specific book that acts as an anchor for the breach, a section where the Dewey Decimal System has become non-Euclidean, a reflection in a window that shows a different reality, a corner where time moves slower.
        *   **Primary Inhabitants:** Normal library patrons (oblivious), a single, terrified librarian who knows something is wrong, the entity causing the breach.
        *   **Available Goods & Services:** Books, public records, a growing sense of dread.
        *   **Potential Random Encounters (x5):** A book flies off the shelf, a player sees something impossible in a mirror, a government agent is seen investigating, a person asks for help finding a book that doesn't exist, the entity tries to communicate through the text on a page.
        *   **Embedded Plot Hooks & Rumors (x3):** "The library was built on a place of psychic significance." "The entity was drawn here by a specific, powerful memory stored in a historical document." "The original Stargate Project had a safe house in the basement."
        *   **Sensory Details:** Sight (Flickering lights, books out of order, subtle visual distortions), Sound (An unnatural silence, whispers that aren't there, the hum of fluorescent lights), Smell (Old paper, dust, a faint smell of ozone).
    *   **A Network Safe House:** A hidden, protected location for the players to rest and train.
        *   **Key Landmarks:** The lead-lined meditation chamber, the wall of conspiracy theories and connections, the short-wave radio for contacting other sensitives, the hidden armory.
        *   **Primary Inhabitants:** The players, other Network members.
        *   **Available Goods & Services:** A place to rest without attracting entities, training in psychic abilities, cryptic mission briefings.
        *   **Potential Random Encounters (x5):** "Watcher" contacts them with a new lead, a fellow sensitive is having a psychic breakdown, a government surveillance team is spotted nearby, a new piece of Stargate Project tech is delivered, the safe house's psychic wards fail temporarily.
        *   **Embedded Plot Hooks & Rumors (x3):** "'Watcher' isn't his real codename." "The Network has a mole." "There's a way to permanently close a breach, but the original project files are in a government black site."
        *   **Sensory Details:** Sight (A cramped, cluttered space; maps with red string; old technology), Sound (The crackle of a radio, hushed conversations), Smell (Stale coffee, old electronics).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** A player uses "The Sight" to view a location.
    *   **THEN:** They gain a crucial piece of information, but the mental strain is taxing. They must make a Wisdom saving throw or suffer a level of exhaustion.
    *   **IF:** A player pushes their use of "The Sight" too far (e.g., by failing the saving throw).
    *   **THEN:** They attract the attention of a hostile entity. Generate a new, personal haunting for that player, where the entity subtly manipulates their perception of reality.
    *   **IF:** The players successfully seal a psychic breach.
    *   **THEN:** The strange phenomena in that location cease. The local population feels a sense of relief they can't explain. However, the psychic energy released alerts the government agency to the players' location.
    *   **IF:** The players are captured by Agent Thorne and the government agency.
    *   **THEN:** Do not end the campaign. Generate a new story arc where the players must escape a government black site, and they now know that the agency is trying to weaponize the very entities they are fighting.
    *   **IF:** The players discover the location of the original Stargate Project files.
    *   **THEN:** Generate a heist-style mission where the players must infiltrate a secure government facility to retrieve the data, which holds the key to permanently closing the breaches.