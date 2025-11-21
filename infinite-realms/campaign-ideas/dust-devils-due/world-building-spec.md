### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**Dust Devil's Due**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** A century after the "Great Scouring" boiled the oceans and turned the world into a vast desert, civilization clings to life in isolated oasis-settlements. The players, a crew of hardened "Dust-Runners," take a job to guide a strange scholar to forgotten ruins. This run drags them into a conspiracy involving ancient weather-controlling technology and a doomsday cult, the "Children of the Scouring," that believes the apocalypse didn't go far enough and seeks to finish the job.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the "Great Scouring": what was the world like before, and what exactly caused the cataclysm?
    *   Write the history of the Sunken City of Aeridor and the Weather-Engine at its heart.
    *   Describe the founding of the first oasis-settlements and the establishment of the Dust-Runner guilds.
    *   Explain the origins and dogma of the Children of the Scouring cult.
    *   Detail the legend of the Maelstrom, the perpetual continent-sized sandstorm, and what lies at its eye.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Dust-Runners Guild** (Major)
        *   **Goals:** To maintain the trade routes between oases and to profit from escorting caravans.
        *   **Hierarchy:** A loose confederation of local guild chapters, led by veteran runners like "One-Shot" Sal.
        *   **Public Agenda:** We keep the world connected. We are the lifeline of civilization.
        *   **Secret Agenda:** The guild leaders suppress knowledge of pre-Scouring technology to maintain their monopoly on travel and trade.
        *   **Assets:** Control of caravan routes, experienced guides, fortified guildhalls in major oases.
        *   **Relationships:** Business-like with all settlements; hostile towards dune-raiders; dismissive of the Children of the Scouring as desert lunatics.
    *   **The Children of the Scouring** (Major)
        *   **Goals:** To reactivate the Weather-Engine and complete the Great Scouring, bringing about a final, purifying drought.
        *   **Hierarchy:** Led by the charismatic psion, The First Son, and his inner circle of fanatics.
        *   **Public Agenda:** We are the true children of the desert, embracing the world as it is now.
        *   **Secret Agenda:** To acquire the power core of the Weather-Engine and install it in their fortress within the Maelstrom.
        *   **Assets:** Fanatical followers, psionic powers, knowledge of hidden desert paths, a fortress at the eye of the Maelstrom.
        *   **Relationships:** Hostile to all civilization; actively sabotage caravans and oasis water supplies.
    *   **Dune-Raider Clans** (Minor)
        *   **Goals:** To survive by preying on caravans and weaker settlements.
        *   **Hierarchy:** Numerous small, competing clans, each led by a ruthless chieftain.
        *   **Public Agenda:** Survival of the fittest.
        *   **Secret Agenda:** None. They are brutally straightforward.
        *   **Assets:** Fast sand-skiffs, knowledge of canyons and ambush points, salvaged weaponry.
        *   **Relationships:** Hostile to everyone, but can be hired as mercenaries by other factions.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **"One-Shot" Sal:** The grizzled, pragmatic leader of the Rust-Rock Dust-Runner's guild, who secretly knows the location of the Sunken City.
    *   **Professor Alistair Finch:** A frail but obsessive scholar who hires the party, driven by a need to atone for his ancestors' creation of the Weather-Engine.
    *   **The First Son:** The charismatic, messianic, and dying psionic leader of the Children of the Scouring.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Cynical Oasis Bartender"
    *   "Desperate Water Merchant"
    *   "Brutal Dune-Raider Chieftain"
    *   "Fanatical Cultist of the Scouring"
    *   "Mutated Desert Beast (Creature)"
    *   "Ancient Maintenance Automaton (Creature)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **Oasis of Rust-Rock:** A bustling, dirty hub of trade and survival, built around a single, precious spring.
        *   **Key Landmarks:** The Dust-Runner Guildhall, the Water Market, Sal's Cantina, the Scrap-Yard.
        *   **Primary Inhabitants:** Dust-Runners, merchants, scavengers, desperate settlers.
        *   **Available Goods & Services:** Caravan supplies, water (at high prices), weapon repair, sand-skiff parts.
        *   **Potential Random Encounters (x5):** A water riot breaks out, a rival Dust-Runner challenges the party, a merchant offers a shady side-job, a sandstorm forces the town into lockdown, the Children of the Scouring attempt to poison the spring.
        *   **Embedded Plot Hooks & Rumors (x3):** "One-Shot Sal hasn't led a run herself in years, not since her last crew vanished in the Salt-Pans." "They say the Children of the Scouring can talk to the sandstorms." "A scavenger found a map that supposedly leads to a pre-Scouring armory."
        *   **Sensory Details:** Sight (Dusty streets, patched-together buildings, long shadows from the harsh sun), Sound (Wind, haggling merchants, the clang of hammers on scrap metal), Smell (Sweat, dust, cooking fires).
    *   **The Sunken City of Aeridor:** A pre-Scouring metropolis buried by sand, a dungeon filled with lost technology and ghosts of the past.
        *   **Key Landmarks:** The Weather-Engine Chamber, the Central Command Spire, the Residential District ruins, the Automated Defense Factory.
        *   **Primary Inhabitants:** Malfunctioning maintenance drones, ghosts of former inhabitants, mutated creatures that have made the ruins their home.
        *   **Available Goods & Services:** Salvageable "Scoured Components" and pre-Scouring schematics.
        *   **Potential Random Encounters (x5):** A patrol of security automatons activates, a structural collapse reveals a hidden area, a psychic echo of the city's last moments plays out, the Children of the Scouring have left a trap, a valuable schematic is found on a skeletal corpse.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Engine was designed to be controlled by a specific genetic signature." "The city's archives might hold the key to stopping the Maelstrom." "Not all the city's inhabitants died in the Scouring; some sealed themselves in vaults."
        *   **Sensory Details:** Sight (Dark, sand-filled corridors, flickering holographic signs, skeletal remains), Sound (Eerie silence, the hum of ancient tech, the skittering of unseen things), Smell (Stale air, dust, ozone).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players' caravan runs out of water while crossing the desert.
    *   **THEN:** Generate a high-stakes skill challenge to find a new source of water. Failure results in the entire caravan suffering levels of exhaustion, and potentially the death of key NPCs.
    *   **IF:** The players successfully track the dune-raiders back to their hideout and eliminate their leader.
    *   **THEN:** The balance of power in the region shifts. Generate a scenario where a new, more dangerous leader takes over, or the remaining raiders offer their allegiance to the players.
    *   **IF:** The players fail to stop the Children of the Scouring from stealing the Weather-Engine's power core.
    *   **THEN:** The Sunken City of Aeridor begins to lose power, activating more dangerous security measures and making the dungeon crawl out much more difficult.
    *   **IF:** The players decide to try and use the Weather-Engine to restore the world, against Professor Finch's warnings.
    *   **THEN:** Generate a series of unintended, catastrophic consequences. The engine is unstable, causing blizzards in the desert, acid rain, or attracting colossal, storm-based creatures.
    *   **IF:** The players successfully defeat the First Son but fail to disable the reactivated Engine inside the Maelstrom.
    *   **THEN:** The Maelstrom begins to expand rapidly. Generate a final, desperate escape sequence as the storm consumes the entire region, permanently changing the world map.
