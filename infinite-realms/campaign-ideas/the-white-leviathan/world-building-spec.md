### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The White Leviathan**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise. The tone is sci-fi survival horror with themes of isolation and cosmic dread.
*   **Content:** Based on the real-world Project Habakkuk, the players are a specialist team sent to investigate a colossal, sentient ghost ship made of living ice that has awakened in the Arctic. They become trapped aboard the "White Leviathan" and must navigate its shifting, non-euclidean corridors, battle the crystalline monsters it creates, and destroy its frozen heart before it plunges the world into a new ice age.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the "true" history of Project Habakkuk and the secret construction of the prototype in the Arctic.
    *   Write a scientific explanation of the extremophilic microorganisms found in the ancient ice and how they formed a collective consciousness.
    *   Describe the biology of the "Cryo-Clones" and other ice-fauna. How are they created by the ship?
    *   Explain the nature of the ship's intelligence. Is it a single entity, a hive mind, or something else?
    *   Detail the fate of the original WWII-era crew, using fragmented logs and psychic echoes.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Specialist Team (The Players)** (Major)
        *   **Goals:** To neutralize the threat of the White Leviathan and survive.
        *   **Hierarchy:** A small, independent team of soldiers and scientists.
        *   **Public Agenda:** To investigate a strange meteorological phenomenon.
        *   **Secret Agenda:** To board the vessel and, if necessary, destroy it.
        *   **Assets:** Their specialized cold-weather gear, their skills, and a single transport vehicle/submarine.
        *   **Relationships:** The sole protagonists in a hostile environment.
    *   **The White Leviathan** (Major)
        *   **Goals:** To preserve itself, grow, and lower the global temperature to make the world more hospitable for its own existence.
        *   **Hierarchy:** A single, living, sentient entity that is the ship itself.
        *   **Public Agenda:** None. It is an alien force of nature.
        *   **Secret Agenda:** To reach a populated coastline and absorb new biomass and materials to repair its failing core.
        *   **Assets:** A colossal body made of nearly indestructible pykrete, the ability to generate Cryo-Clone monsters, control over its internal structure and temperature.
        *   **Relationships:** The primary antagonist and the dungeon itself.
    *   **The Original Crew's Echoes** (Minor)
        *   **Goals:** To warn new visitors away or to trick them into sharing their fate.
        *   **Hierarchy:** A fragmented collection of psychic remnants from the original crew.
        *   **Public Agenda:** None.
        *   **Secret Agenda:** Some echoes may retain enough of their former selves to want to help the players, while others have been corrupted and seek to serve the Leviathan.
        *   **Assets:** Knowledge of the ship's original layout and systems.
        *   **Relationships:** An unreliable and dangerous source of information.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **The Voice of the Leviathan:** The disembodied, alien intelligence of the ship, which communicates through the groaning of ice and psychic whispers.
    *   **The Ghost of Captain Thorne:** The psychic echo of the ship's original, stoic captain, who may try to guide or hinder the party.
    *   **The First Clone:** A perfectly preserved, but monstrously transformed, member of the original crew, now acting as the Leviathan's primary hunter.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Crystalline Ice-Spider (Creature)"
    *   "Ice-Mimic (Creature)"
    *   "Brute of Compressed Ice (Creature)"
    *   "Fragmented Psychic Echo (Hazard)"
    *   "Corrupted Maintenance Drone (Creature)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Shifting Ice Corridors:** The main hallways and passages of the Habakkuk, which are constantly, slowly, reconfiguring.
        *   **Key Landmarks:** A frozen mess hall with preserved meals on the tables, a communications room with a single, active radio, a section of the hull breached to the freezing ocean, a wall of ice containing the frozen, screaming faces of the original crew.
        *   **Primary Inhabitants:** Cryo-Clones, ice-spiders, spectral echoes of the crew.
        *   **Available Goods & Services:** Salvageable WWII-era equipment, frozen (but edible) rations.
        *   **Potential Random Encounters (x5):** A corridor freezes over, blocking the path; a section's gravity plating fails; a group of mimics disguised as equipment attacks; the party encounters a psychic echo of a crewman's final moments; the ship groans, causing a section of the ceiling to collapse.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Captain's logs are in his quarters, and they detail a weakness in the ship's core." "The original reactor is still active and is the only source of heat on the ship." "The creatures can't see you if you stand perfectly still."
        *   **Sensory Details:** Sight (Walls of ice and pykrete, frost, flickering emergency lights), Sound (The constant groaning and creaking of ice, the skittering of unseen things, the howl of wind), Smell (Cold, sterile air; a faint smell of ozone).
    *   **The Reactor Core:** The heart of the ship, once a naval reactor, now a vast cavern of glowing, sentient ice.
        *   **Key Landmarks:** The central, glowing ice-crystal (the "heart"), the original, frozen reactor, the control room encased in ice, the nests of the most powerful Cryo-Clones.
        *   **Primary Inhabitants:** The First Clone, powerful elemental guardians, the core intelligence of the Leviathan.
        *   **Available Goods & Services:** None. This is the final dungeon.
        *   **Potential Random Encounters (x5):** A wave of intense cold emanates from the core, a powerful guardian is birthed from the central crystal, the Leviathan speaks directly to the players' minds, the core begins to pulse rapidly, threatening to release a massive energy discharge, the ghosts of the original reactor crew appear.
        *   **Embedded Plot Hooks & Rumors (x3):** "The heart is vulnerable to sonic frequencies." "Destroying the heart will cause the entire ship to collapse." "The original crew tried to cause a reactor meltdown to destroy the entity, but failed."
        *   **Sensory Details:** Sight (A massive, pulsating, glowing crystal; walls of pure, clear ice; frozen machinery), Sound (A deep, powerful hum; a high-pitched, crystalline chime), Smell (Intense cold, ozone, raw power).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players spend too long in a sector without a heat source.
    *   **THEN:** They must begin making Constitution saving throws against the effects of extreme cold, gaining levels of exhaustion on a failure.
    *   **IF:** The players make a loud noise (e.g., use explosives).
    *   **THEN:** The ship's threat level increases. Generate a response, such as a new corridor freezing shut to block their retreat, or a powerful Cryo-Clone being dispatched to their location.
    *   **IF:** The players successfully restore power to a section of the ship.
    *   **THEN:** They gain a temporary safe zone with light and heat. However, the power surge also alerts the Leviathan to their exact location and methods.
    *   **IF:** The players manage to communicate with and appease the Ghost of Captain Thorne.
    *   **THEN:** The captain's echo provides them with a crucial piece of information (e.g., a security override code, the location of a hidden armory) before fading away permanently.
    *   **IF:** In the finale, the players place the explosive charge on the ship's heart but are unable to escape in time.
    *   **THEN:** Generate a final, cinematic scene where the players sacrifice themselves to destroy the White Leviathan, saving the world at the cost of their own lives. Their story becomes a classified legend.
