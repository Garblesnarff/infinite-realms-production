### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Tempest's Gambit**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** Based on the real-life "Operation Popeye," two kingdoms are locked in a brutal war. One side has begun to weaponize the weather, but their massive ritual is losing control, tearing the veil to the Plane of Air and causing the weather itself to gain a malevolent sentience. The players are a squad of soldiers or spies who must journey into the heart of the enemy (or their own) kingdom to stop the ritual before it triggers a meteorological apocalypse.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of the war between the two kingdoms. What are they fighting over?
    *   Write the story of the "Tempest's Gambit" project. Who conceived of it, and how was it approved?
    *   Describe the nature of the Plane of Air in this setting and its relationship to the Material Plane.
    *   Explain the magical theory behind the weather-control ritual. Why is it failing?
    *   Detail the story of a past military disaster caused by uncontrolled magic.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Player's Kingdom** (Major)
        *   **Goals:** To win the war against the rival kingdom.
        *   **Hierarchy:** A standard military command structure.
        *   **Public Agenda:** To defend their borders and bring a swift end to the war.
        *   **Secret Agenda:** To win at any cost, even if it means using forbidden weather magic.
        *   **Assets:** A large army, fortified positions, the Tempest's Gambit conclave.
        *   **Relationships:** At war with the rival kingdom; the players are initially loyal to this faction.
    *   **The Rival Kingdom** (Major)
        *   **Goals:** To win the war.
        *   **Hierarchy:** A standard military command structure.
        *   **Public Agenda:** To defend themselves from aggression and reclaim lost territory.
        *   **Secret Agenda:** They are seeking their own super-weapon to counter the unnatural weather.
        *   **Assets:** A large army, a populace motivated by defense of their homeland.
        *   **Relationships:** The primary military antagonists.
    *   **The Conclave of Storms** (Major)
        *   **Goals:** To win the war for their kingdom using their weather-control magic.
        *   **Hierarchy:** A council of powerful storm sorcerers and druids.
        *   **Public Agenda:** To be the kingdom's greatest heroes and patriots.
        *   **Secret Agenda:** They are aware they are losing control but are too proud and desperate to admit it, and will eliminate anyone who tries to stop them.
        *   **Assets:** The ability to control the weather (for now), a hidden ritual site, the full backing of their kingdom's high command.
        *   **Relationships:** The primary magical antagonists, who see the players as traitors.
    *   **The Court of Air** (Minor)
        *   **Goals:** To stop the damage to the veil between planes and punish those responsible.
        *   **Hierarchy:** Led by an enraged Air Elemental prince or princess.
        *   **Public Agenda:** None.
        *   **Secret Agenda:** To cause the weather ritual to backfire catastrophically, destroying the offending kingdom.
        *   **Assets:** The ability to command air elementals and other airborne creatures, control over natural (but not magical) weather.
        *   **Relationships:** A potential, but dangerous and unpredictable, ally for the players.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Archdruid Kaelen:** The patriotic and dangerously proud leader of the Conclave of Storms.
    *   **General Valerius:** The players' commanding officer, who is torn between his duty to his country and his fear of the Tempest's Gambit.
    *   **Prince Aerion:** The enraged Air Elemental prince who seeks revenge on the Material Plane.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Patriotic Soldier"
    *   "Fanatical Storm Sorcerer"
    *   "Sentient Lightning Elemental (Creature)"
    *   "Fog Horror (Creature)"
    *   "Rival Kingdom Scout"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Muddy Front Lines:** A battlefield turned into an impassable quagmire by endless, magical rain.
        *   **Key Landmarks:** A half-sunken fortress, a trench network filled with water, a field of broken siege engines, no-man's-land.
        *   **Primary Inhabitants:** Soldiers from both kingdoms, mud mephits, carrion crawlers.
        *   **Available Goods & Services:** Military rations, ammunition (if you can find a dry supply).
        *   **Potential Random Encounters (x5):** A flash flood sweeps through the trenches, a patrol from the rival kingdom attacks, a sentient fog bank attempts to suffocate the party, a soldier is struck by a pinpoint lightning strike, the party finds a deserter from the Conclave.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Conclave's ritual site is hidden in the mountains to the east." "The rival kingdom is trying to build a magical device to disperse the storms." "The rain isn't just water; it's slowly draining the life from the land."
        *   **Sensory Details:** Sight (Endless mud, grey skies, rain), Sound (The constant drumming of rain, distant thunder, the shouts of soldiers), Smell (Mud, wet wool, decay).
    *   **The Ritual Site:** A hidden location high in the mountains where the Conclave performs their ritual.
        *   **Key Landmarks:** A ring of standing stones that act as amplifiers, a central altar with a map of the war, a swirling portal to the Plane of Air, the living quarters of the druids and sorcerers.
        *   **Primary Inhabitants:** The Conclave of Storms, their elemental guardians, elite soldiers.
        *   **Available Goods & Services:** None. This is the enemy stronghold.
        *   **Potential Random Encounters (x5):** A powerful member of the Conclave is performing a ritual, a patrol of air elementals attacks, the portal to the Plane of Air pulses, releasing a wave of chaotic energy, the party finds the Archdruid's journal detailing his growing fears, General Valerius arrives to confront the Conclave.
        *   **Embedded Plot Hooks & Rumors (x3):** "The ritual is powered by a captured Air Elemental." "The Archdruid knows he has lost control but is too proud to admit it." "Destroying one of the standing stones will disrupt the entire ritual."
        *   **Sensory Details:** Sight (A swirling vortex of clouds, crackling lightning, glowing runes), Sound (The roar of a hurricane, constant thunder, chanting), Smell (Ozone, rain, immense power).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players are caught in a magical weather event.
    *   **THEN:** Generate a unique combat or skill challenge based on the weather. A hailstorm might create difficult terrain and deal periodic damage, while a sentient thunderstorm might actively hunt the players with lightning strikes.
    *   **IF:** The players choose to report their findings to their commanding officer, General Valerius.
    *   **THEN:** Valerius is torn. He gives the players a secret, off-the-books mission to stop the Conclave, but warns them that if they are caught, the kingdom will disavow them.
    *   **IF:** The players choose to bargain with the Air Elemental prince, Aerion.
    *   **THEN:** Aerion agrees to help them stop the ritual, but his methods are extreme. He may try to shatter the entire mountain range, not caring about the mortals who live there, forcing the players to moderate his rage.
    *   **IF:** The players successfully destroy one of the Conclave's focusing stones.
    *   **THEN:** The weather in a large region becomes completely chaotic and unpredictable for a time, creating a massive wild magic zone that affects both armies.
    *   **IF:** In the finale, the players fail to stop the ritual and the veil to the Plane of Air is torn completely open.
    *   **THEN:** The war ends, as both kingdoms are now faced with a new, more terrifying threat: a full-scale invasion of elementals and other airborne creatures, leading to a new campaign arc focused on planar survival.
