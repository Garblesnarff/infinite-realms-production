### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**Star-Eater's Wake**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The players, a hard-luck salvage crew, board the legendary generation ship *Genesis*, which vanished a century ago. They find it transformed by a parasitic, crystalline entity from beyond the stars. The ship itself is now a living, predatory ecosystem, and the crew is a fresh source of nutrients. They must fight their way through the living dungeon to escape before they are consumed.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history and original mission of the generation ship *Genesis*.
    *   Write the story of the *Genesis*'s first encounter with the Star-Eater entity.
    *   Describe the biology of the Star-Eater. How does it consume and transform technology and organic matter?
    *   Explain the nature of the "Antibodies" and other crystalline lifeforms created by the entity.
    *   Reconstruct the last logs of the original crew, detailing their descent into madness and horror.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Salvage Crew (The Players)** (Major)
        *   **Goals:** To escape the *Genesis* alive and, if possible, with some valuable salvage.
        *   **Hierarchy:** A small, independent crew.
        *   **Public Agenda:** To get rich.
        *   **Secret Agenda:** To survive at all costs.
        *   **Assets:** Their ship (the *Stray Comet*), their salvage gear, their wits.
        *   **Relationships:** Trapped and hunted by the Star-Eater.
    *   **The Star-Eater Entity** (Major)
        *   **Goals:** To consume, grow, and replicate.
        *   **Hierarchy:** A single, hive-mind consciousness controlling the entire ship and its creatures.
        *   **Public Agenda:** None. It is an alien intelligence.
        *   **Secret Agenda:** To use the *Genesis*'s FTL drive to travel to a populated star system and find more to consume.
        *   **Assets:** The entire *Genesis* starship, the ability to create crystalline monsters, psychic powers.
        *   **Relationships:** Views the players as a foreign infection and a source of food.
    *   **The Last Survivor (Dr. Aris Thorne)** (Minor)
        *   **Goals:** To survive and to keep the Star-Eater's weakness a secret.
        *   **Hierarchy:** None. He is alone.
        *   **Public Agenda:** To be left alone.
        *   **Secret Agenda:** He believes the Star-Eater is a necessary cosmic predator and that unleashing its weakness would be a mistake.
        *   **Assets:** Decades of knowledge about the ship and the entity, a hidden safe room, cybernetic self-modifications.
        *   **Relationships:** Hostile and paranoid towards the players, whom he sees as a threat to his carefully constructed survival.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **AURA (Automated Unified Response AI):** The *Genesis*'s fragmented and corrupted AI, which tries to help the party through malfunctioning drones and distorted messages.
    *   **Dr. Aris Thorne (The Last Survivor):** A paranoid and feral former xenobotanist who has survived for decades by hiding in the walls.
    *   **The Star-Eater's Echo:** A manipulative psychic projection of the entity, often appearing as the ship's heroic captain to lure the party into traps.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Crystalline Scuttler (Antibody Creature)"
    *   "Crystalline Hunter (Antibody Creature)"
    *   "Hallucinatory Ghost of a Former Crew Member"
    *   "Malfunctioning Service Drone"
    *   "Predatory Crystalline Flora (Creature)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Bridge of the *Genesis*:** The command center, now a throne room of crystal where the Echo of the Captain often appears.
        *   **Key Landmarks:** The Captain's crystal throne, the main viewscreen (cracked and showing a view of alien space), the tactical console (overgrown with crystals), the escape pod bays (fused shut).
        *   **Primary Inhabitants:** The Star-Eater's Echo, psychic manifestations.
        *   **Available Goods & Services:** Corrupted ship logs, a partial map of the ship.
        *   **Potential Random Encounters (x5):** The Echo appears and offers a deal, a psychic wave of fear washes over the party, the viewscreen flickers to life showing the ship's last moments, a powerful antibody crashes through the ceiling, AURA manages to send a cryptic warning through a console.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Captain's authorization codes are needed to access the engineering core." "The ship's logs mention a 'weakness' in the entity's cellular structure." "There was a mutiny just before the ship went dark."
        *   **Sensory Details:** Sight (Gleaming crystals, dead screens, floating dust motes), Sound (Eerie silence, the faint hum of the entity, distorted whispers), Smell (Ozone, cold metal, a strange, sweet smell of crystal).
    *   **The Hydroponics Bay:** A former lush garden, now a terrifying jungle of crystalline flora and predatory plant-monsters.
        *   **Key Landmarks:** The central irrigation system (now pumping crystalline fluid), a grove of razor-leafed crystal plants, a nest of crystalline predators, the xenobotany lab.
        *   **Primary Inhabitants:** Predatory crystal-plants, crystalline insectoids, the ghost of Dr. Aris Thorne's research partner.
        *   **Available Goods & Services:** Samples of the crystalline lifeforms, potentially useful (or harmful) biological components.
        *   **Potential Random Encounters (x5):** A plant releases a cloud of hallucinogenic spores, the party is ambushed by camouflaged predators, the gravity plating fails, a section of the bay is a zero-G zone, the party finds the hidden lab of the Last Survivor.
        *   **Embedded Plot Hooks & Rumors (x3):** "Dr. Thorne's research on the entity's biology is still on his lab computer." "Some of the plants here are vulnerable to sonic frequencies." "The Last Survivor has been seen scavenging for parts in this area."
        *   **Sensory Details:** Sight (A jungle of glowing crystals, strange alien flowers, thick fog), Sound (Chittering noises, the rustle of crystal leaves, the drip of strange fluids), Smell (Rotting vegetation, sweet nectar, damp earth).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players make a loud noise or draw a large amount of power.
    *   **THEN:** The ship's Threat Meter increases. Generate a corresponding response from the ship's immune system, from a small wave of scuttlers to the appearance of a specialized Hunter antibody.
    *   **IF:** The players choose to trust the Echo of the Captain.
    *   **THEN:** The Echo leads them on a path that seems safe but ends in a deadly, pre-prepared ambush, significantly raising the Threat Meter.
    *   **IF:** The players manage to corner and communicate with the Last Survivor instead of fighting him.
    *   **THEN:** He can be convinced to trade his knowledge for a piece of valuable technology. Generate a new objective where the players must retrieve a specific item for him in exchange for the data-drive containing the entity's weakness.
    *   **IF:** The players use the entity's weakness against it before reaching the engineering core.
    *   **THEN:** The entity goes into a frenzy, causing the entire ship to become violently hostile. The Threat Meter jumps to maximum, and the path to the core becomes a desperate, high-speed chase.
    *   **IF:** The players successfully plant the bomb in the Crystalline Heart.
    *   **THEN:** A self-destruct sequence is initiated. Generate a timed, high-octane escape sequence where the party must race back to their ship as the *Genesis* is torn apart around them by the dying entity.
