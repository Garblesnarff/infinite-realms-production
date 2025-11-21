### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Star-Fallen Wound**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise. The tone is grim, high-lethality cosmic horror and survival.
*   **Content:** Inspired by the Tunguska Event, the players are hired to venture into the "Star-Fallen Wound," a quarantined wilderness created when a splinter of the Far Realm crashed into the world. The landscape itself is a hostile, alien entity where physics are warped and the air is thick with psionic radiation. The players must find the heart of the impact zone and seal the planar breach before it, and the maddening aberrations that spill from it, consume the world.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the "Star-Fall" event. What did eyewitnesses (from a distance) see and hear?
    *   Write a scientific/magical theory on the nature of the Far Realm and its splinters.
    *   Describe the effects of the Wound's psionic radiation on the native flora and fauna.
    *   Explain the history of the quarantine. Who enforces it, and how?
    *   Detail the story of the first failed expedition into the Wound and what became of them.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Expedition (The Players)** (Minor)
        *   **Goals:** To reach the heart of the Wound, seal the planar breach, and survive.
        *   **Hierarchy:** A small, specialized team of explorers or mercenaries.
        *   **Public Agenda:** To fulfill their contract with their patron.
        *   **Secret Agenda:** To maintain their sanity in a place designed to break it.
        *   **Assets:** Specialized gear for surviving in the Wound, their skills, and a fragile grip on reality.
        *   **Relationships:** At odds with everything in the Wound.
    *   **The Aberrations** (Major)
        *   **Goals:** Incomprehensible. Their actions may seem random and chaotic, but follow an alien logic.
        *   **Hierarchy:** None. They are a chaotic ecosystem of predators and prey from another reality.
        *   **Public Agenda:** None.
        *   **Secret Agenda:** To warp the Material Plane into a habitat more suitable for themselves.
        *   **Assets:** The ability to break the laws of physics, psionic powers, immunity to conventional logic.
        *   **Relationships:** The primary antagonists, hostile to all native life.
    *   **The First-Born** (Minor)
        *   **Goals:** To worship the Wound and achieve apotheosis by merging with it.
        *   **Hierarchy:** A cult of mutated survivors from the first expedition, led by a powerful, insane psychic.
        *   **Public Agenda:** To protect the "sacred ground" of the Wound from outsiders.
        *   **Secret Agenda:** To sabotage the players' mission to seal the breach, believing it will ascend them to godhood.
        *   **Assets:** A deep, insane knowledge of the Wound's layout; powerful psionic mutations; an immunity to the sanity-draining effects (as they are already mad).
        *   **Relationships:** Hostile to the players, whom they see as heretics.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **The Voice of the Wound:** A psychic manifestation of the Far Realm splinter, which communicates through whispers, hallucinations, and by speaking through mutated creatures.
    *   **The Elder Druid:** The aged guardian of the quarantine zone, who knows much about the Wound but is forbidden from entering.
    *   **The First-Born Prophet:** The insane, powerful, and tragically mutated leader of the cult, who was once a renowned scholar.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Gibbering Mouther (Creature)"
    *   "Mind Flayer (Creature)"
    *   "Star Spawn Mangler (Creature)"
    *   "Insane Cultist of the First-Born"
    *   "Twisted, crystalline flora (Creature/Hazard)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Crystalline Forest:** A forest near the edge of the Wound where the trees have been transformed into shifting, crystalline structures.
        *   **Key Landmarks:** A river of liquid time, a grove of whispering crystals, a petrified aberration, the ruins of a ranger outpost.
        *   **Primary Inhabitants:** Displacer beasts, phase spiders, lesser aberrations.
        *   **Available Goods & Services:** None. This is a hostile wilderness.
        *   **Potential Random Encounters (x5):** A mana storm rolls in, causing wild magic surges; the party is ambushed by a pack of displacer beasts; a player sees a vision of a possible, horrifying future; the party finds the journal of a dead ranger; gravity briefly shifts, causing the trees to bend at impossible angles.
        *   **Embedded Plot Hooks & Rumors (x3):** "The crystals sing a song that can drive you mad or show you the way." "The First-Born cultists harvest the crystals for their rituals." "There is a plant here that can brew a potion to protect your mind."
        *   **Sensory Details:** Sight (A forest of shimmering, multi-colored crystals; alien constellations in the sky), Sound (A constant, low humming; the chime of crystals knocking together), Smell (Ozone, a complete lack of any natural scent).
    *   **The Heart of the Wound:** The epicenter of the impact, a non-euclidean labyrinth of flesh, crystal, and thought.
        *   **Key Landmarks:** The crashed Far Realm splinter itself, a chamber where gravity is sideways, a room that is a living brain, the portal to the Far Realm.
        *   **Primary Inhabitants:** The most powerful aberrations (Beholders, Mind Flayers), the First-Born Prophet, the psychic echo of the splinter.
        *   **Available Goods & Services:** None. This is the final dungeon.
        *   **Potential Random Encounters (x5):** The layout of the labyrinth changes, a player must make a high-DC sanity save or gain a new form of madness, the party is confronted by a psychic projection of their greatest fear, a powerful artifact from another reality is found, the portal pulses, temporarily warping the laws of magic.
        *   **Embedded Plot Hooks & Rumors (x3):** "The only way to seal the breach is to use a specific, ancient ritual." "The First-Born Prophet seeks to throw himself into the portal." "The splinter is not a rock; it is an egg, and it is about to hatch."
        *   **Sensory Details:** Sight (Impossible geometry, shifting walls of flesh and crystal, colors you've never seen before), Sound (A constant, maddening whisper; the sound of your own blood pumping in your ears), Smell (The smell of thoughts, burning electricity, and something utterly alien).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** A player fails a Sanity saving throw after witnessing an aberration or an impossible event.
    *   **THEN:** The player gains a level of Madness. Generate a short-term or long-term madness effect from the DMG, but themed to the Far Realm (e.g., "You are convinced that you have an extra, invisible limb," or "You can only speak in questions").
    *   **IF:** The players are caught in a mana storm.
    *   **THEN:** All spells cast within the storm trigger a Wild Magic Surge. The DC for all Sanity saving throws is increased.
    *   **IF:** The players successfully kill a powerful aberration.
    *   **THEN:** The psychic death-scream of the creature alerts all other aberrations in a one-mile radius to the players' location, making the area significantly more dangerous for a period of time.
    *   **IF:** The players choose to parley with the First-Born Prophet.
    *   **THEN:** He offers them a "gift" of insight into the Far Realm, which grants them a powerful boon (e.g., a new psionic ability) but also a permanent form of madness.
    *   **IF:** In the finale, the players fail to seal the planar breach.
    *   **THEN:** The breach expands. The Star-Fallen Wound begins to grow, and the campaign shifts from exploration to a desperate, last-ditch defense of the nearest town against a full-scale invasion of aberrations.
