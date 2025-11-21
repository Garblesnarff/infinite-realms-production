### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Serpent Who Eats the Sun**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise. The campaign is a time-loop mystery with a cosmic horror climax.
*   **Content:** The players are visiting the remote island of Solmora for the "Sun-Swallowing Festival," a total eclipse. As darkness falls, a doomsday cult completes a ritual, a cosmic serpent rises from the sea, and the world ends. The players awaken at the start of the festival day, trapped in a time loop. They must use their foreknowledge to uncover the conspiracy and stop the ritual before the loop—and the world—ends for good.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of the island of Solmora and its unique traditions surrounding the eclipse.
    *   Write the mythology of the cosmic serpent. What is it, and why do the cultists worship it as "The Great Purifier"?
    *   Describe the mechanics of the time loop. Is it a deliberate spell, a divine intervention, or a side effect of the serpent's awakening?
    *   Explain the history of the Sunken Temple and its connection to the serpent.
    *   Detail the story of Kael, the lighthouse keeper, and the order he once belonged to.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Outsiders (The Players)** (Major)
        *   **Goals:** To understand the time loop, stop the ritual, and survive the apocalypse.
        *   **Hierarchy:** A small group of visitors, the only ones aware of the loop.
        *   **Public Agenda:** To enjoy the festival.
        *   **Secret Agenda:** To manipulate the day's events to gather clues and formulate a plan.
        *   **Assets:** Their retained memories of previous loops, the ability to experiment without permanent consequences.
        *   **Relationships:** The only ones who can save the world; viewed as normal tourists by everyone else.
    *   **The Solmora Cult** (Major)
        *   **Goals:** To successfully complete the ritual and summon the cosmic serpent.
        *   **Hierarchy:** The entire island population, secretly led by the beloved matriarch, Elder Maeve.
        *   **Public Agenda:** To host a joyous and memorable festival for all.
        *   **Secret Agenda:** To sacrifice themselves and the world in an act of ultimate, purifying worship.
        *   **Assets:** A whole island of fanatical followers, intimate knowledge of the island's secrets, magical wards against hostile intent.
        *   **Relationships:** The primary antagonists, completely unaware that the players are a threat.
    *   **The Watcher on the Cliff (Kael)** (Minor)
        *   **Goals:** To discover what is wrong on the island and stop it.
        *   **Hierarchy:** A single, isolated individual.
        *   **Public Agenda:** To be a grumpy, antisocial lighthouse keeper.
        *   **Secret Agenda:** To fulfill his duty to his old order and stop the cosmic threat he failed to prevent years ago.
        *   **Assets:** Deep knowledge of cosmic threats, a fortified lighthouse, years of observations on the villagers.
        *   **Relationships:** A potential ally who must be convinced of the truth each and every loop.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation. Each NPC must have a detailed daily schedule.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Elder Maeve:** The kindly, grandmotherly leader of the island and the cold, fanatical high priestess of the doomsday cult.
    *   **Kael, the Lighthouse Keeper:** The gruff, paranoid, and guilt-ridden former monster hunter.
    *   **The Laughing Child:** The silent, smiling, and unnerving child who is the nascent avatar of the serpent god.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Cheerful Villager (Secret Cultist)"
    *   "Suspicious Fisherman"
    *   "Festival Game Master"
    *   "Guardian of the Sunken Temple (Creature)"
    *   "A tourist enjoying the festival"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections. Each blueprint must include a timeline of key events that happen at that location during the day.
*   **Location Roster:**
    *   **The Village of Ouroboros:** A cheerful, idyllic fishing village with a dark secret.
        *   **Key Landmarks:** The central plaza with the festival stage, the docks, the tavern, Elder Maeve's house.
        *   **Primary Inhabitants:** Villagers (all cultists), tourists.
        *   **Available Goods & Services:** Festival food, souvenirs, boat rentals.
        *   **Timeline of Events:** 9 AM: Festival games begin. 12 PM: Elder Maeve gives a welcoming speech. 3 PM: The fishing boats bring in the "ritual feast." 6 PM: The villagers begin to gather at the cliffs for the eclipse.
        *   **Embedded Plot Hooks & Rumors (x3):** "The fish for the feast are a strange, deep-water species only caught on this day." "Elder Maeve meets with the fishermen at 3 PM sharp." "The Laughing Child is never seen eating or drinking."
        *   **Sensory Details:** Sight (Colorful banners, smiling faces, beautiful ocean views), Sound (Festival music, laughter, the cry of gulls), Smell (Salt air, cooking fish, flowers).
    *   **The Sunken Temple of the Serpent:** An ancient, underwater temple that is only accessible at low tide.
        *   **Key Landmarks:** The Tidal Entrance, the Chamber of Three Relics, the Altar of the Eclipse, the great serpent carving on the wall.
        *   **Primary Inhabitants:** Ancient guardians, tidal spirits, the elite of the cult during the final hours.
        *   **Available Goods & Services:** None. This is the final dungeon.
        *   **Timeline of Events:** 2 PM: Low tide reveals the entrance. 4 PM: The cult's elite guard arrives to prepare the temple. 5 PM: Elder Maeve arrives with the relics. 6 PM: The ritual begins as the eclipse starts.
        *   **Embedded Plot Hooks & Rumors (x3):** "The temple's guardian remembers intruders from previous loops." "The three relics must be placed on the altar in a specific order." "The serpent carving on the wall shows the true history of the cult."
        *   **Sensory Details:** Sight (Water-worn stone, ancient carvings, eerie light filtering through the water), Sound (Dripping water, the distant sound of the ocean, an oppressive silence), Smell (Brine, seaweed, ancient dust).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome within a single loop.
*   **Triggers:**
    *   **IF:** The players die or the world ends.
    *   **THEN:** The day resets. The players awaken in their beds with all their memories intact. All other world states and NPC memories are reset to the morning of the festival.
    *   **IF:** The players act with open hostility or reveal their foreknowledge to a cultist.
    *   **THEN:** The cult's magical wards are triggered. That specific cultist becomes suspicious and avoids the players for the rest of the day, and a group of cultist enforcers is dispatched to "deal with" the troublesome tourists.
    *   **IF:** The players successfully convince Kael, the Lighthouse Keeper, of the time loop.
    *   **THEN:** He becomes a powerful ally for that loop, providing them with information and resources. However, they must re-convince him every single morning.
    *   **IF:** The players steal one of the three ritual relics before the cult can retrieve it.
    *   **THEN:** The cult's daily schedule changes. They dispatch a search party for the missing relic, creating new NPC movements and opportunities for the players to learn more or intercept them.
    *   **IF:** In the finale, the players successfully disrupt the ritual but do not defeat the nascent avatar (The Laughing Child).
    *   **THEN:** The serpent is not summoned, and the world is saved. However, the child avatar escapes the island, and the epilogue describes a new, looming threat as the child begins to gather new followers in the wider world.
