### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**Echoes of the First Dawn**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** In a prehistoric world, the players are members of a fledgling humanoid tribe. When a volcanic eruption destroys their homeland, they must lead the survivors on a perilous migration across an untamed continent. They will battle megafauna, contend with rival tribes, and uncover the secrets of a forgotten precursor race, all while searching for a new, safe valley to call home.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the creation myth of the tribe and their relationship with the natural world.
    *   Write the history of the precursor race. Who were they? What were the monoliths for? Why did they vanish?
    *   Describe the ecosystem of the Great River and the culture of the Lizardfolk who control it.
    *   Explain the origin of the psychic Tyrannosaurus Rex. Is it a natural mutation, or is it connected to the precursor monoliths?
    *   Detail the legend of the "Promised Valley" as told in the tribe's oral history.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Player's Tribe** (Major)
        *   **Goals:** To survive the migration and find a new home.
        *   **Hierarchy:** Led by Elder Kaya and the player characters.
        *   **Public Agenda:** To protect the tribe and preserve their traditions.
        *   **Secret Agenda:** Elder Kaya secretly believes the precursors are gods and seeks to lead the tribe to a holy site, which may not be the safest location.
        *   **Assets:** A small number of survivors (approx. 20-30), the collective knowledge of the elders, the skills of the players.
        *   **Relationships:** Wary of all outsiders; in direct competition for resources with other predators.
    *   **Koth's Hunters** (Minor)
        *   **Goals:** To ensure the tribe is led by strength and to prioritize hunting above all else.
        *   **Hierarchy:** A faction within the tribe, loyal to the rival hunter, Koth.
        *   **Public Agenda:** To provide for the tribe.
        *   **Secret Agenda:** To usurp leadership from the players and Elder Kaya, whom they see as weak.
        *   **Assets:** The tribe's most skilled (but reckless) hunters.
        *   **Relationships:** A rival faction within the main tribe.
    *   **The Great River Lizardfolk** (Major)
        *   **Goals:** To maintain control of the Great River and its resources.
        *   **Hierarchy:** Ruled by a Lizard King, with a shaman (S'slath) who holds significant influence.
        *   **Public Agenda:** To defend their territory from all intruders.
        *   **Secret Agenda:** The shaman S'slath seeks to harness the power of precursor artifacts to overthrow the king.
        *   **Assets:** A large warrior population, control of the river, knowledge of its currents and dangers.
        *   **Relationships:** Hostile and territorial towards outsiders.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Elder Kaya:** The tribe's wise and pragmatic elder, who holds the sacred map and guides the tribe spiritually.
    *   **Koth, the Lone Hunter:** A proud, arrogant, and highly skilled hunter who challenges the players' leadership.
    *   **S'slath, the River-Speaker:** The cunning and ambitious shaman of the Lizardfolk tribe.
    *   **The God-Lizard:** A hyper-intelligent Tyrannosaurus Rex that rules the Promised Valley with psychic power.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Grateful Tribal Elder"
    *   "Scared Tribal Child"
    *   "Loyal Hunter Follower"
    *   "Aggressive Lizardfolk Warrior"
    *   "Sabertooth Tiger (Creature)"
    *   "Dire Bear (Creature)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Ashen Plains:** The party's former home, now a grey desert of volcanic ash under a smoke-darkened sky.
        *   **Key Landmarks:** The Great Volcano, the ruins of the tribe's village, a petrified forest, the skeletal remains of a mammoth.
        *   **Primary Inhabitants:** Displaced predators (Sabertooth Tigers), ash-dwelling insects, ghosts of the dead.
        *   **Available Goods & Services:** Scarce, contaminated water sources; salvageable items from the old village.
        *   **Potential Random Encounters (x5):** A pack of starving Sabertooth Tigers, a sudden ash-storm reduces visibility to zero, a fissure in the earth releases poisonous gas, the party finds the tracks of another group of survivors, a lone, maddened survivor attacks.
        *   **Embedded Plot Hooks & Rumors (x3):** "The elders say the volcano's eruption was unnatural." "Koth claims to know a secret path through the plains." "A strange, humming sound can be heard at night, coming from beneath the ash."
        *   **Sensory Details:** Sight (Grey ash covering everything, skeletal trees, hazy red sun), Sound (Wind howling, the crunch of ash underfoot, eerie silence), Smell (Sulphur, smoke, decay).
    *   **The Monolith Field:** A strange, humming field of precursor artifacts that hum with latent magic.
        *   **Key Landmarks:** The Central Monolith, a ring of smaller humming stones, a cave system used as a den by a Dire Bear, a precursor altar.
        *   **Primary Inhabitants:** A territorial Dire Bear, strange energy-based lifeforms, latent magical echoes.
        *   **Available Goods & Services:** None. This is a place of discovery and danger.
        *   **Potential Random Encounters (x5):** A monolith activates, projecting a star-map, a player experiences a psychic vision of the precursors, a rival animal predator is drawn to the field's energy, a magical surge temporarily gives a player a cantrip, the ground becomes electrified.
        *   **Embedded Plot Hooks & Rumors (x3):** "Touching the central monolith can awaken great power, or kill you." "The symbols on the stones match the map on the mammoth hide." "The Lizardfolk fear this place and call it the 'Singing Stones.'"
        *   **Sensory Details:** Sight (Black, humming stones, distorted air, glowing symbols), Sound (A constant, low hum, crackling energy, the wind), Smell (Ozone, static electricity).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The tribe's Food supply drops to zero.
    *   **THEN:** The tribe's Morale drops significantly. Generate a scenario where a desperate hunting party, led by Koth, disobeys the players and attacks a creature far too dangerous for them.
    *   **IF:** The tribe's Morale drops to a critical level.
    *   **THEN:** A portion of the tribe, led by Koth, splinters off to follow their own path. The players must either let them go, or challenge Koth for leadership in ritual combat.
    *   **IF:** A player fails a Primal Magic spell check.
    *   **THEN:** Roll on the Primal Magic Surge table. Generate the immediate, unpredictable consequences for the player and the surrounding area.
    *   **IF:** The players choose to challenge the Lizard King's champion and win.
    *   **THEN:** The Lizard King grants them safe passage, but the shaman S'slath sees them as a threat to his own plans and begins plotting against them, sending assassins after the party.
    *   **IF:** The players reach the Promised Valley but attempt to coexist with the psychic T-Rex instead of fighting it.
    *   **THEN:** Generate a new narrative path focused on communication and understanding. The party must perform a series of tasks to prove their worth to the God-Lizard, such as clearing out a rival megafauna or cleansing a part of the valley tainted by a strange sickness.
