### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**Journey to the Inner World**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** Following the trail of a lost expedition, the party discovers a passage to a hidden world deep within the planet's core—a primeval wilderness of strange flora, dinosaurs, and subterranean civilizations. This inner world is dying. Its central crystalline sun is fading, and the party must brave its dangers to find a way to reignite it before this lost world is plunged into eternal darkness and chaos.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of the Elder race, the creators of the Inner World and the Crystalline Sun.
    *   Write the story of the last great war between the Serpent Men and the Abolethic Sovereignty.
    *   Describe the ecosystem of the Inner World. How has life adapted to the Crystalline Sun?
    *   Explain the nature of the Crystalline Sun and the Crystal Heart that powers it.
    *   Detail the story of Professor Alistair Finch's expedition and what led to their demise.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Serpent Men of Ss'tharr** (Major)
        *   **Goals:** To maintain their dominance and survive the Fading.
        *   **Hierarchy:** Ruled by the brutal King Sss'tharr, who is advised by a council of shamans.
        *   **Public Agenda:** To protect their city and their people from the dangers of the Inner World.
        *   **Secret Agenda:** King Sss'tharr is secretly a puppet of an Aboleth, who has promised him survival in exchange for tribute and control.
        *   **Assets:** A large army of warriors, a fortified city, knowledge of the local flora and fauna.
        *   **Relationships:** Hostile to all outsiders; at war with the Aboleth's other servants.
    *   **The Abolethic Sovereignty** (Major)
        *   **Goals:** To hasten the Fading of the sun, plunging the world into a darkness they can control.
        *   **Hierarchy:** A single, ancient Aboleth and its mind-controlled servants (including King Sss'tharr).
        *   **Public Agenda:** None. They operate from the shadows.
        *   **Secret Agenda:** To transform the Inner World into a new watery domain for their species.
        *   **Assets:** A powerful, ancient Aboleth, control of the Sunken City, an army of enslaved creatures.
        *   **Relationships:** The primary antagonistic force, manipulating events from behind the scenes.
    *   **Finch's Survivors** (Minor)
        *   **Goals:** To survive and continue Professor Finch's research.
        *   **Hierarchy:** A small, desperate group of explorers and scientists, led by a surviving member of the expedition.
        *   **Public Agenda:** To find a way back to the surface.
        *   **Secret Agenda:** They believe the Crystal Heart can be used as an unlimited power source for the surface world and want to steal it.
        *   **Assets:** Some pre-expedition technology, detailed research notes from Professor Finch.
        *   **Relationships:** Wary of the Serpent Men; unaware of the Aboleth's influence.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Professor Alistair Finch:** The lost explorer, now living among a primitive tribe, who holds a key piece of the puzzle to reigniting the sun.
    *   **King Sss'tharr:** The brutal and paranoid ruler of the Serpent Men, secretly a puppet of a greater power.
    *   **The Last Elder:** A psychic echo of an ancient being bound to the Crystal Heart, who speaks in riddles.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Brutal Serpent Man Warrior"
    *   "Cunning Serpent Man Shaman"
    *   "Mind-Controlled Servant of the Aboleth"
    *   "Deinonychus Pack Hunter (Creature)"
    *   "Massive Subterranean Dinosaur (Creature)"
    *   "Desperate Survivor of Finch's Expedition"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Primeval Jungle:** A vast, subterranean jungle filled with strange, bioluminescent flora and dangerous prehistoric creatures.
        *   **Key Landmarks:** The Great Chasm entrance, a grove of giant, glowing mushrooms, a tar pit filled with fossilized remains, the ruins of Finch's first camp.
        *   **Primary Inhabitants:** Dinosaurs, giant insects, undiscovered beasts, primitive human tribes.
        *   **Available Goods & Services:** Forageable food, clean water sources, valuable alchemical ingredients.
        *   **Potential Random Encounters (x5):** A pack of deinonychus on the hunt, a territorial triceratops, a stampede of giant herbivores, a patch of poisonous, glowing plants, the discovery of a strange, edible fruit.
        *   **Embedded Plot Hooks & Rumors (x3):** "The native tribes speak of a 'Sunken City' that holds the key to the world's light." "The Serpent Men capture outsiders on sight." "Professor Finch was last seen heading towards the great volcano."
        *   **Sensory Details:** Sight (Bioluminescent plants, giant ferns, strange creatures), Sound (Dinosaur roars, insect buzzing, dripping water), Smell (Damp earth, strange flowers, decay).
    *   **The Sunken City of the Elders:** The beautiful and mysterious ruins of the ancient civilization that created the Inner World, now submerged in a vast underground ocean.
        *   **Key Landmarks:** The Crystal Heart chamber, the Hall of Echoes, the Elder's Observatory, the Great Seal.
        *   **Primary Inhabitants:** The Aboleth and its guardians, psychic echoes of the Elders, aquatic monstrosities.
        *   **Available Goods & Services:** None. This is the central dungeon.
        *   **Potential Random Encounters (x5):** A patrol of mind-controlled fish-men, a psychic trap left by the Elders, a sudden underwater current, a vision of the city in its prime, the Aboleth attempts to telepathically dominate a player.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Crystal Heart can only be activated by a being from the surface world." "The Aboleth is controlling the Serpent King." "The Last Elder is not a guardian, but a prisoner."
        *   **Sensory Details:** Sight (Crystalline architecture, shimmering water, glowing glyphs), Sound (Muffled silence, the flow of water, distant, alien whispers), Smell (Clean water, ozone, ancient dust).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players take too long to reach the Crystal Heart.
    *   **THEN:** The Fading Sun mechanic advances. The world grows darker, temperatures drop, new cold-based creatures emerge, and some factions become more desperate and aggressive.
    *   **IF:** The players kill King Sss'tharr.
    *   **THEN:** The Serpent Men fall into civil war. Generate a scenario where the players must navigate the chaotic city, potentially allying with a faction that opposes the Aboleth.
    *   **IF:** The players manage to free King Sss'tharr from the Aboleth's control instead of killing him.
    *   **THEN:** The Serpent Men become powerful, if reluctant, allies. Generate a new mission where the players lead a Serpent Man army against the Sunken City.
    *   **IF:** The players attempt to take the Crystal Heart for themselves, as Finch's survivors want.
    *   **THEN:** The Last Elder turns against them, activating the city's full defensive capabilities. The Aboleth sees an opportunity and offers the party a deal: the Heart in exchange for servitude.
    *   **IF:** The players successfully perform the ritual to reignite the sun.
    *   **THEN:** The Inner World is saved, but the massive energy release creates new, permanent passages to the surface world. Generate an epilogue where the creatures and civilizations of the Inner World begin to emerge onto the surface, creating a new era of conflict and discovery.
