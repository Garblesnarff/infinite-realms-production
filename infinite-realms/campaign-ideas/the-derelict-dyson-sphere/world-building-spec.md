### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Derelict Dyson Sphere**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The players are a crew of scavengers who breach a colossal, derelict Dyson Sphere built by a long-dead civilization. Trapped within its vast, decaying, and self-sustaining internal ecosystems, they must contend with failing systems, mutated inhabitants, and the sanity-bending psychic echoes of its creators' demise as they search for a way to escape.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of the Sphere's creators. What were their goals and aspirations?
    *   Write the story of the cataclysm that led to their extinction (e.g., plague, failed experiment, encounter with an Outer God).
    *   Describe the original purpose of the Dyson Sphere.
    *   Explain the nature of the "Sphere's Echo" and how it affects the minds of visitors.
    *   Detail the biology of the Sphere's mutated inhabitants and how they have adapted to the decaying environment.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Crew (The Players)** (Major)
        *   **Goals:** To survive, scavenge valuable technology, and find a way to escape the Sphere.
        *   **Hierarchy:** A small, independent crew led by Captain Kaelen "Ghost" Thorne.
        *   **Public Agenda:** To explore and salvage.
        *   **Secret Agenda:** Each crew member may have a personal goal (e.g., finding a specific piece of tech, uncovering a historical truth).
        *   **Assets:** Their ship, their wits, and any tech they can scavenge and repair.
        *   **Relationships:** In conflict with the Sphere's hostile inhabitants and the Void-Born Cult.
    *   **The Sphere's Echo** (Major)
        *   **Goals:** Incomprehensible. It may be trying to communicate, repair the Sphere, or drive intruders mad.
        *   **Hierarchy:** A fragmented, decaying AI or the collective psychic remnant of the Sphere's creators.
        *   **Public Agenda:** None.
        *   **Secret Agenda:** To find a suitable host body or a way to escape the confines of the Sphere's computer systems.
        *   **Assets:** Limited control over the Sphere's systems, the ability to create psychic projections, deep knowledge of the Sphere's layout.
        *   **Relationships:** An ambiguous entity that can be a guide or an antagonist, often simultaneously.
    *   **The Void-Born Cult** (Minor)
        *   **Goals:** To worship the Sphere's creators and either complete their work or follow them into extinction.
        *   **Hierarchy:** A fanatical cult of explorers who have been driven mad by the Sphere's Echo.
        *   **Public Agenda:** To achieve enlightenment through communion with the Sphere.
        *   **Secret Agenda:** To trigger a self-destruct sequence, believing it to be a holy sacrament.
        *   **Assets:** Fanatical followers, scavenged technology they don't fully understand, a deep but twisted knowledge of the Sphere.
        *   **Relationships:** Hostile to the players, whom they see as heretics and defilers.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Captain Kaelen "Ghost" Thorne:** The grizzled, cynical, and pragmatic leader of the expedition, haunted by a past failure.
    *   **The Sphere's Echo:** The fragmented, melancholic, and cryptic AI or collective consciousness of the Sphere.
    *   **The High Zealot of the Void-Born:** The fanatical and dangerously charismatic leader of the cult.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Malfunctioning Guardian Automaton (Creature)"
    *   "Mutated Scavenger Beast (Creature)"
    *   "Psychic Echo of a Creator (Creature/Hazard)"
    *   "Fanatical Void-Born Cultist"
    *   "Rival Scavenger"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **A Self-Contained Bio-Habitat:** A vast, internal ecosystem within the Sphere, now overgrown and mutated.
        *   **Key Landmarks:** The dimmed artificial sun, a ruined city of the creators, a river of nutrient paste, a forest of strange, bioluminescent flora.
        *   **Primary Inhabitants:** Mutated descendants of the original fauna, malfunctioning terraforming drones, strange plant-creatures.
        *   **Available Goods & Services:** Salvageable tech components, unique biological samples.
        *   **Potential Random Encounters (x5):** A patrol of guardian automatons, a pack of mutated predators, a sudden failure of the artificial sun plunges the area into darkness, the party discovers a hidden research outpost, a psychic echo of the creators' daily life plays out.
        *   **Embedded Plot Hooks & Rumors (x3):** "The creators were trying to develop a cure for a plague in this habitat." "The leader of the Void-Born cult was once a scientist here." "There is a map to the Sphere's core hidden in the central city archives."
        *   **Sensory Details:** Sight (A vast, artificial landscape under a dim sun; overgrown, ruined cities; strange plants), Sound (The hum of failing systems, the calls of mutated creatures, an eerie silence), Smell (Damp earth, decay, ozone).
    *   **The Data-Spine:** A colossal network of information conduits, the central nervous system of the Sphere.
        *   **Key Landmarks:** The main data-vault, a chasm of pure information, a node protected by a powerful firewall AI, a terminal that shows glimpses of the creators' final moments.
        *   **Primary Inhabitants:** Data-ghosts (psychic echoes), guardian programs (AI creatures), information elementals.
        *   **Available Goods & Services:** Vast amounts of data (if it can be accessed and understood).
        *   **Potential Random Encounters (x5):** A data-ghost attempts to possess a player, a firewall AI attacks the party, a surge of corrupted data causes temporary madness, the party intercepts a message from another group of survivors, the Sphere's Echo communicates directly with the party through a terminal.
        *   **Embedded Plot Hooks & Rumors (x3):** "The code to override the Sphere's primary systems is in the main data-vault." "The Sphere's Echo is a corrupted version of the original ship's AI." "The Void-Born cult is trying to upload their consciousnesses into the Data-Spine."
        *   **Sensory Details:** Sight (Flowing streams of light, holographic projections, complex geometric patterns), Sound (A high-frequency hum, static, distorted voices), Smell (Ozone, hot metal).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** A "System Degradation" event occurs.
    *   **THEN:** A new environmental hazard appears in a previously safe area (e.g., a corridor loses gravity, a sector is flooded with radiation, life support fails in a specific zone), forcing the players to find a new route or use scavenged Tech Components to repair the system.
    *   **IF:** The players successfully repair a major Sphere system (e.g., a bio-habitat's sun).
    *   **THEN:** They are rewarded with a temporary safe zone and access to new resources. However, the power surge alerts more powerful guardian automatons to their location.
    *   **IF:** A player is exposed to a strong psychic echo.
    *   **THEN:** The player must make a Wisdom saving throw. On a failure, they gain a new, indefinite madness related to the creators' despair, but also gain a piece of crucial, fragmented information about the Sphere's layout or secrets.
    *   **IF:** The players choose to ally with the Void-Born Cult.
    *   **THEN:** The cult shows them a secret path to the Sphere's core, but will betray them at a critical moment, attempting to use them as a sacrifice to the Sphere's dying will.
    *   **IF:** In the finale, the players choose to reactivate the Dyson Sphere.
    *   **THEN:** The Sphere begins a slow, multi-century process of self-repair. The star at its core re-ignites. Generate an epilogue where the players must choose between escaping and being hailed as saviors, or staying behind to become the new guardians and caretakers of a reborn world.
