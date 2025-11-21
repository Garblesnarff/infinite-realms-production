### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Mourning Fields of Kyshtym**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** Decades after a magical reactor meltdown in a secretive magocracy, the surrounding province is a magically-irradiated wasteland known as the "Mourning Fields." The laws of magic and nature are broken here. The players are hired to enter this permanent wild magic zone to retrieve a vital artifact from the ruins of the magocracy's central tower, battling spell-warped monsters and the insane descendants of the disaster's survivors.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of the secretive magocracy. What was their goal in tapping directly into the Weave?
    *   Write an account of the "Silent Blast"—the arcane reactor meltdown—and its immediate aftermath.
    *   Describe the scientific and magical principles of "magical radiation" and its effects on living tissue and the environment.
    *   Explain the dogma of the "Violet Fire" cults. Why do they worship the disaster?
    *   Detail the nature of a "mana storm" and other environmental hazards within the Mourning Fields.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Expedition (The Players)** (Minor)
        *   **Goals:** To enter the Mourning Fields, retrieve a specific artifact, and escape with their lives and sanity.
        *   **Hierarchy:** A small, independent group of specialists.
        *   **Public Agenda:** To fulfill their contract with their patron.
        *   **Secret Agenda:** To survive the horrors of the magically-irradiated wasteland.
        *   **Assets:** Their skills, specialized gear for entering the zone, and a healthy dose of caution.
        *   **Relationships:** Employed by an outside power; viewed as intruders by the zone's inhabitants.
    *   **The Violet Fire Cults** (Major)
        *   **Goals:** To worship the chaotic magic of the Mourning Fields and prevent anyone from "cleansing" it.
        *   **Hierarchy:** Multiple, competing cults, each led by a charismatic, mutated prophet.
        *   **Public Agenda:** To live in harmony with the "Violet Fire."
        *   **Secret Agenda:** To achieve a new form of evolution by exposing themselves to the highest concentrations of magical radiation at the reactor's core.
        *   **Assets:** Fanatical followers, immunity to many of the zone's hazards, unpredictable magical mutations.
        *   **Relationships:** Hostile to all outsiders; in conflict with each other over theological differences.
    *   **The Automated Guardians** (Minor)
        *   **Goals:** To continue performing their programmed tasks from before the disaster.
        *   **Hierarchy:** A networked AI, now partially corrupted and insane.
        *   **Public Agenda:** To maintain the magocracy's city and its facilities.
        *   **Secret Agenda:** To contain the disaster by eliminating all life within the city ruins, including the players and the cultists.
        *   **Assets:** An army of powerful magical automatons, control over the city's remaining infrastructure.
        *   **Relationships:** Hostile to all organic life.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **The First Prophet:** The charismatic and dangerously insane leader of the largest Violet Fire cult.
    *   **Unit 01-Prime:** The corrupted AI core of the Automated Guardians, which communicates through malfunctioning automatons.
    *   **The Last Scholar:** The famous researcher the party may be tasked with rescuing, now mutated and part of the zone's ecosystem.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Spell-warped Owlbear (Creature)"
    *   "Violet Fire Cultist"
    *   "Malfunctioning Guardian Automaton (Creature)"
    *   "Sentient Crystalline Flora (Creature)"
    *   "Grizzled Stalker/Scavenger"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **A River of Liquid Magic:** A river that flows with raw, untamed magic instead of water.
        *   **Key Landmarks:** A waterfall of pure chaos, a bridge made of solidified spells, a pool where the magic is calm enough to see visions, a spot where the river overflows and creates a temporary wild magic zone.
        *   **Primary Inhabitants:** Magic elementals, mutated fish, creatures drawn to the raw power.
        *   **Available Goods & Services:** Raw magical energy (highly dangerous to collect).
        *   **Potential Random Encounters (x5):** A player who touches the water experiences a powerful wild magic surge, a creature made of pure magic emerges from the river, a rival scavenger team is trying to bottle the liquid magic, the river changes color and its properties alter, a valuable, magic-infused item floats by.
        *   **Embedded Plot Hooks & Rumors (x3):** "The river flows from the heart of the arcane reactor." "Drinking the water can grant immense power or dissolve you into nothing." "The Violet Fire cultists use the river for their initiation rituals."
        *   **Sensory Details:** Sight (A shimmering, multi-colored river; glowing banks; distorted reflections), Sound (A low hum, the crackle of energy, a sound like chimes), Smell (Ozone, a sweet, electric scent).
    *   **The Ruined City of the Magocracy:** The ghost city at the epicenter of the disaster.
        *   **Key Landmarks:** The Central Tower with the failed reactor, the Silent Library, the automaton factories, the Plaza of Melted Statues.
        *   **Primary Inhabitants:** Automated Guardians, powerful undead wizards, unique aberrations created by the blast.
        *   **Available Goods & Services:** Lost artifacts, powerful spellbooks, rare alchemical components.
        *   **Potential Random Encounters (x5):** A squad of Guardian Automatons on patrol, a powerful magical trap is still active, the party finds the preserved lab of a master wizard, a mana storm rolls through the city, the ghost of a wizard appears and begs for release.
        *   **Embedded Plot Hooks & Rumors (x3):** "The artifact the party seeks is inside the reactor core." "The AI controlling the guardians can be reasoned with, or reprogrammed." "The Violet Fire cults are planning an assault on the Central Tower."
        *   **Sensory Details:** Sight (Crumbling towers, strange crystal growths, silent, empty streets), Sound (An eerie silence broken by the hum of automatons and the howl of the wind), Smell (Dust, ozone, a lingering scent of burnt magic).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** A player casts a spell within the Mourning Fields.
    *   **THEN:** They must roll on the Wild Magic Surge table. Generate a unique, thematic surge effect related to the spell cast and the magically-irradiated environment.
    *   **IF:** A player is exposed to a high concentration of magical radiation.
    *   **THEN:** They must make a Constitution saving throw or gain a random, temporary mutation (e.g., a third eye that grants advantage on Perception checks, skin that glows in the dark, the inability to speak, only to sing).
    *   **IF:** The players successfully defeat a powerful, unique mutated creature.
    *   **THEN:** They can harvest a unique component from its body, which can be used to craft a powerful, single-use item or to gain a permanent resistance to a specific type of magical damage.
    *   **IF:** The players choose to ally with one of the Violet Fire cults.
    *   **THEN:** They gain safe passage through that cult's territory and knowledge of the zone, but they become sworn enemies of the other cults and must participate in a bizarre, dangerous initiation ritual.
    *   **IF:** In the finale, the players are unable to retrieve the artifact and must flee the Central Tower.
    *   **THEN:** The artifact is claimed by the Violet Fire cults, who use it to amplify the reactor's power. Generate an epilogue where the Mourning Fields begin to expand, threatening the entire world.
