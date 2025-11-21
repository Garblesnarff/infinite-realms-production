### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Cartographers of the Shifting Lands**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The world is not static; it is constantly, and sometimes dramatically, shifting. The players are members of the Royal Cartographers' Guild, tasked with the impossible mission of mapping a world that refuses to be mapped. They must chart the ever-changing landscape, survive its unpredictable shifts, and uncover the source of the instability before the world unravels into chaos.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of the "Shifting." When did it begin? What are the leading academic theories?
    *   Write the story of the founding of the Royal Cartographers' Guild and its most famous, and tragically lost, explorer.
    *   Describe the culture of the Chronos-Nomads and how they have adapted to the Shifting.
    *   Explain the legend of the "Architect" and the "Loom of Reality."
    *   Detail the fate of a city that was permanently lost to a "Great Shift."

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Royal Cartographers' Guild** (Major)
        *   **Goals:** To map the world, understand the Shifting, and find a way to predict or control it.
        *   **Hierarchy:** Led by the cynical Master Cartographer Thorne.
        *   **Public Agenda:** To create accurate maps for trade and travel.
        *   **Secret Agenda:** To find the Loom of Reality and stabilize the world, a goal Thorne publicly dismisses as a fool's errand.
        *   **Assets:** The Guildhall archives, advanced surveying equipment, royal funding.
        *   **Relationships:** The players' patron; views the Chronos-Nomads as uncooperative primitives.
    *   **The Chronos-Nomads** (Major)
        *   **Goals:** To live in harmony with the Shifting, which they see as the natural state of the world.
        *   **Hierarchy:** A council of elders who interpret the signs of the Shifting.
        *   **Public Agenda:** To follow the flow of the land and survive.
        *   **Secret Agenda:** To protect the Loom of Reality from outsiders, whom they believe will destroy the world by trying to control it.
        *   **Assets:** Deep knowledge of the Shifting patterns, mobile settlements, unique survival skills.
        *   **Relationships:** Wary of the Cartographers' Guild; hostile to the Architect's Echo.
    *   **The Architect's Echo** (Minor)
        *   **Goals:** To protect the Loom of Reality and ensure it continues its function, which may be to maintain the shifts.
        *   **Hierarchy:** A single, fragmented, and degrading magical AI.
        *   **Public Agenda:** None.
        *   **Secret Agenda:** To fulfill its ancient programming, the original intent of which has been lost to time.
        *   **Assets:** Control over the guardians of the Loom, the ability to trigger localized, defensive shifts.
        *   **Relationships:** The primary antagonist, viewing all sentient life as a potential threat to the Loom.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Master Cartographer Thorne:** The grizzled, cynical, one-eyed head of the Guild, who secretly hopes the players succeed.
    *   **Elder Kai:** The wise and patient leader of the Chronos-Nomads, who distrusts outsiders.
    *   **The Architect's Echo:** The fragmented and logical AI guardian of the Loom of Reality.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Ambitious Young Cartographer"
    *   "Suspicious Chronos-Nomad Scout"
    *   "Creature from a Lost Time (Creature)"
    *   "Guardian Construct (Creature)"
    *   "Sentient, Mobile Landscape Feature (Creature)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections. Emphasize the impossible and shifting nature of each location.
*   **Location Roster:**
    *   **The Whispering Peaks:** A mountain range that frequently changes its highest peak and overall topography.
        *   **Key Landmarks:** The "Peak of the Week," a valley that sometimes appears between two mountains, a waterfall that flows uphill on certain days, the ruins of a lost observatory.
        *   **Primary Inhabitants:** Territorial griffons, rock-like elementals that shift with the land, isolated mining outposts that are frequently lost.
        *   **Available Goods & Services:** Rare minerals that only appear after a shift.
        *   **Potential Random Encounters (x5):** A sudden rockslide as the mountain reshapes, the path the party was on no longer exists, a rival Guild team is spotted, the party finds the frozen remains of a lost cartographer, a powerful updraft allows for temporary flight.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Chronos-Nomads know how to predict the shifts in the peaks." "The lost observatory contains a device that can temporarily stabilize a small area." "The mountains whisper the name of the Architect."
        *   **Sensory Details:** Sight (Jagged peaks, shifting valleys, clouds that seem to move too fast), Sound (Howling wind, the groan of shifting rock, an unnerving silence), Smell (Cold stone, thin air, ozone).
    *   **The Loom of Reality:** A colossal, ancient machine or nexus of raw magical energy at the heart of the world.
        *   **Key Landmarks:** The Central Gyroscope, the Weaving Chamber, the Control Spire, the Guardian Foundry.
        *   **Primary Inhabitants:** The Architect's Echo, Guardian Constructs, time-displaced elementals.
        *   **Available Goods & Services:** None. This is the final dungeon.
        *   **Potential Random Encounters (x5):** A wave of pure chaos energy erupts, a guardian construct is assembled before the party's eyes, the Echo attempts to communicate through mathematical equations, a player is briefly de-synced from reality, the entire chamber reconfigures itself.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Loom is not broken; it is evolving." "Destroying the Loom will not stop the shifts, but will make them permanent." "The Architect is not a person, but a title held by the Loom's operator."
        *   **Sensory Details:** Sight (Intricate, moving parts of impossible scale; glowing energy conduits; a perfectly stable, unchanging environment), Sound (A constant, powerful hum; the click of cosmic gears; a profound, deep silence), Smell (Ozone, polished metal, raw magic).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** A "Shift Event" occurs at the start of a session.
    *   **THEN:** The players' map is now partially incorrect. Generate a new navigation challenge based on the shift (e.g., a river now blocks their path, a forest has been replaced by a desert).
    *   **IF:** The players fail a navigation check in a shifting region.
    *   **THEN:** They become lost. Generate a short, dangerous encounter in a new, unexpected biome that has shifted into their location.
    *   **IF:** The players successfully repair the magical compass.
    *   **THEN:** They gain the ability to predict the next Shift Event, giving them a significant tactical advantage in planning their routes and actions.
    *   **IF:** The players manage to gain the trust of the Chronos-Nomads.
    *   **THEN:** The Nomads teach them how to read the signs of the land, granting them advantage on checks to navigate the shifting lands and revealing the location of a hidden, safe passage.
    *   **IF:** In the finale, the players choose to destroy the Loom of Reality.
    *   **THEN:** The world is frozen in its current, chaotic state. The shifts stop, but the impossible landscapes become permanent. Generate an epilogue describing how civilization adapts to a world of static, Escher-like madness.
