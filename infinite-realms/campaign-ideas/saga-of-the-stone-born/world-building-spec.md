### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**Saga of the Stone-Born**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** In a world gripped by a relentless ice age, the players are the "Stone-Born," the first of their tribe to be born with nascent magical abilities. When a supernatural blizzard separates them from their people, they must master their strange new powers to survive the brutal wilderness, hunt megafauna, and seek the legendary "Sun-Stone," a relic said to hold the power to break the endless winter.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of the endless winter. Was it a natural event or the result of a magical cataclysm?
    *   Write the oral history of the Mammoth Tribe, including their key traditions and survival methods.
    *   Describe the nature of the "Nascent Powers." Are they divine gifts, psionic awakenings, or something else?
    *   Explain the legend of the Sun-Stone and why it is believed to have the power to end the winter.
    *   Detail the culture and beliefs of the Ice-Ghoul cannibals. Why do they worship the cold?

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Stone-Born (The Players)** (Minor)
        *   **Goals:** To survive, master their powers, and find the Sun-Stone to save their people.
        *   **Hierarchy:** A small, isolated group with no formal leader.
        *   **Public Agenda:** To reunite with the Mammoth Tribe.
        *   **Secret Agenda:** To understand the nature of their strange new powers.
        *   **Assets:** Their nascent powers, their survival skills, and the cryptic guidance of an Ancestor Spirit.
        *   **Relationships:** Separated from their tribe; hostile towards the Ice-Ghouls; wary of the Sabre-Tooth Clan.
    *   **The Ice-Ghouls** (Major)
        *   **Goals:** To survive by consuming the flesh of the strong and to serve the spirits of winter.
        *   **Hierarchy:** Led by the ruthless Kaelen One-Eye.
        *   **Public Agenda:** To survive and thrive in the endless winter.
        *   **Secret Agenda:** Kaelen One-Eye seeks to consume the players to steal their nascent powers.
        *   **Assets:** A large number of savage warriors, knowledge of the most brutal parts of the wilderness, a pact with dark winter spirits.
        *   **Relationships:** Hostile to all other tribes.
    *   **The Sabre-Tooth Clan** (Major)
        *   **Goals:** To survive the winter and protect their territory.
        *   **Hierarchy:** Led by the proud hunter, Lyra Swift-Spear.
        *   **Public Agenda:** To find enough food to last through the winter.
        *   **Secret Agenda:** They are considering a raid on the players' (presumed dead) tribe's territory.
        *   **Assets:** Skilled hunters, a strong warrior tradition, tamed sabre-tooth cats as companions.
        *   **Relationships:** Wary of and competitive with the Mammoth Tribe; hostile towards the Ice-Ghouls.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Kaelen One-Eye:** The cold, ruthless, and pragmatic leader of the Ice-Ghouls, an exiled former member of the players' tribe.
    *   **Lyra Swift-Spear:** The proud, suspicious, but honorable leader of the Sabre-Tooth Clan.
    *   **The Ancestor Spirit:** A formless, ancient chorus of ancestral spirits that guides the party through cryptic visions.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Savage Ice-Ghoul Cannibal"
    *   "Proud Sabre-Tooth Clan Hunter"
    *   "Starving Mammoth Tribe Refugee"
    *   "Woolly Mammoth (Creature)"
    *   "Sabre-Tooth Tiger (Creature)"
    *   "Undead Mammoth (Creature)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Weeping Glacier:** A constantly shifting glacier full of deep crevasses and ice caves.
        *   **Key Landmarks:** The entrance to the Heart of Winter, a frozen waterfall, a chasm that whispers with the voices of the wind, the lair of a Remorhaz.
        *   **Primary Inhabitants:** Ice-Ghouls, Remorhazes, Ice Mephits.
        *   **Available Goods & Services:** Clean water (ice), scarce frozen lichens.
        *   **Potential Random Encounters (x5):** A sudden avalanche, a crevasse opens under the party's feet, an Ice-Ghoul patrol, the party finds the frozen corpse of a hunter from another tribe, a powerful wind threatens to blow the party off the glacier.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Ice-Ghouls have a secret passage through the glacier." "The heart of the glacier is unnaturally warm." "The Sun-Stone is said to be guarded by the spirit of the First Winter."
        *   **Sensory Details:** Sight (Blinding white snow, deep blue ice, swirling snow), Sound (Howling wind, the groan and crack of shifting ice), Smell (Clean, cold air, nothing else).
    *   **The Valley of Lost Things:** A valley sheltered from the wind, where megafauna driven south by the ice have gathered in massive numbers.
        *   **Key Landmarks:** The Mammoth Graveyard, a hot spring surrounded by lush vegetation, a series of tar pits, a cave system used as a lair by a pack of Sabre-Tooth Tigers.
        *   **Primary Inhabitants:** Herds of mammoths, woolly rhinos, and other megafauna; packs of Sabre-Tooth Tigers and Dire Wolves; the Sabre-Tooth Clan.
        *   **Available Goods & Services:** Abundant food (if you can hunt it), fresh water, natural shelters.
        *   **Potential Random Encounters (x5):** A stampede of mammoths, a territorial dispute between two predator packs, the party finds a wounded megafauna, a hunting party from the Sabre-Tooth Clan, a sudden, localized warm spell causes a flash flood.
        *   **Embedded Plot Hooks & Rumors (x3):** "Lyra Swift-Spear will trade passage for the pelt of a legendary beast." "The mammoths always return to the graveyard to die." "The hot springs have healing properties."
        *   **Sensory Details:** Sight (Massive herds of animals, lush greenery around the springs, skeletal remains), Sound (The calls of megafauna, the bubbling of hot springs, the roar of predators), Smell (Animal musk, damp earth, sulphur).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** A player rolls a 1 on a Nascent Power check.
    *   **THEN:** Generate a significant, dangerous surge of wild power. The effect should be related to the player's ability but have a major, uncontrolled consequence (e.g., a fire mage causes a section of the glacier to melt, creating a new hazard).
    *   **IF:** The players choose to ally with the Sabre-Tooth Clan.
    *   **THEN:** They gain valuable allies and knowledge of the land, but they are now embroiled in the Sabre-Tooth Clan's rivalry with another tribe, creating a new set of enemies.
    *   **IF:** The players are defeated by the undead mammoth in the graveyard.
    *   **THEN:** They are not killed, but are captured by the Ice-Ghouls who worship the undead creature. Generate a new scenario where the players must escape the Ice-Ghoul camp.
    *   **IF:** The players manage to kill Kaelen One-Eye.
    *   **THEN:** The Ice-Ghoul tribe fractures into warring factions, making travel through their territory chaotic but also creating opportunities to turn them against each other.
    *   **IF:** The players successfully awaken the primordial entity of fire and end the endless winter.
    *   **THEN:** Generate an epilogue describing the great thaw. The world is saved, but the melting glaciers release ancient plagues, long-frozen monsters, and flood entire continents, creating a new set of challenges for the next generation.
