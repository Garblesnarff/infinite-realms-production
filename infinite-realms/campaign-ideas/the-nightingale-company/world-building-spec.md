### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Nightingale Company**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** Based on WWII's "Ghost Army," the players are members of a company of illusionists who, during a great war, accidentally brought one of their phantom dragons to life through collective belief. Now disavowed and hunted, they must track their own creation—a creature of pure belief—across a war-scarred world and either dispel it or bring it under control before it triggers another war.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of the great war against the hobgoblin empire.
    *   Write the story of the founding of the Nightingale Company and its most famous deceptions.
    *   Describe the magical theory behind "Thought-Forms." How does collective belief create a tangible entity?
    *   Explain the events of the final battle where the phantom dragon was brought to life.
    *   Detail the current political climate of the post-war world, including the fragile truce and the reasons for the kingdom disavowing the players.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Nightingale Company (The Players)** (Minor)
        *   **Goals:** To track and neutralize the phantom dragon, clear their names, and survive.
        *   **Hierarchy:** A small, independent special operations team.
        *   **Public Agenda:** None. They are officially fugitives.
        *   **Secret Agenda:** To understand the nature of their creation and atone for the chaos it is causing.
        *   **Assets:** Mastery of illusion and deception, their wits, and a shared, unbreakable bond.
        *   **Relationships:** Hunted by their former kingdom and the hobgoblin remnants; viewed as dangerous anomalies.
    *   **The Kingdom's Crown** (Major)
        *   **Goals:** To maintain the fragile peace and eliminate any threats to stability, including the players and their creation.
        *   **Hierarchy:** A monarchy served by a military and intelligence apparatus.
        *   **Public Agenda:** To rebuild and ensure peace.
        *   **Secret Agenda:** To capture the players and learn how to replicate the creation of Thought-Forms for their own use.
        *   **Assets:** The kingdom's army, a network of spies, royal authority.
        *   **Relationships:** The players' former employers, now their hunters.
    *   **The Hobgoblin Remnants** (Major)
        *   **Goals:** To rebuild their empire and get revenge on the kingdom that defeated them.
        *   **Hierarchy:** A fractured collection of military legions, each led by a warlord.
        *   **Public Agenda:** To reclaim their ancestral lands.
        *   **Secret Agenda:** To capture and control the phantom dragon, which they now see as the ultimate weapon of war.
        *   **Assets:** Disciplined military units, knowledge of the war-scarred terrain, a burning desire for vengeance.
        *   **Relationships:** Hostile to both the kingdom and the players.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **The Phantom Dragon:** The party's creation, an intelligent but alien Thought-Form that acts on a logic of belief and emotion.
    *   **General Varrus:** The party's former commanding officer, now tasked with hunting them down, torn between his duty and his loyalty to his old unit.
    *   **Warlord Grol'nok:** A cunning hobgoblin leader who seeks to capture the dragon.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Suspicious Village Elder"
    *   "Bounty Hunter looking for the players"
    *   "War-weary Veteran Soldier"
    *   "Hobgoblin Scout"
    *   "Person who has witnessed the phantom dragon and now believes in it fervently"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **A War-Scarred Battlefield:** A desolate landscape littered with the remnants of a major battle from the great war.
        *   **Key Landmarks:** A ruined fortress, a field of broken siege engines, a mass grave, an unexploded (and possibly magical) munition.
        *   **Primary Inhabitants:** Scavengers, ghosts of fallen soldiers, wild animals.
        *   **Available Goods & Services:** Salvageable weapons and armor.
        *   **Potential Random Encounters (x5):** A patrol from the kingdom or the hobgoblins, a group of desperate refugees, a sudden manifestation of battlefield trauma (a psychic echo), the phantom dragon is spotted flying overhead, the party finds the remains of a caravan destroyed by the dragon.
        *   **Embedded Plot Hooks & Rumors (x3):** "The dragon seems drawn to places of strong emotion, like this battlefield." "A deserter from the Nightingale Company is said to be hiding in the ruins." "The hobgoblins are trying to recover a lost legion standard from the fortress."
        *   **Sensory Details:** Sight (Shattered weapons, old bones, craters, tattered banners), Sound (The wind whistling through ruins, the caw of crows, a profound silence), Smell (Old blood, rust, decay).
    *   **A Hidden Underground Safe House:** A secret base of operations for the players, perhaps an old hideout of the Nightingale Company.
        *   **Key Landmarks:** A map of the region with troop movements from the war, a workshop for creating illusions and disguises, a secret exit, a memorial to fallen company members.
        *   **Primary Inhabitants:** The players.
        *   **Available Goods & Services:** A safe place to rest and plan.
        *   **Potential Random Encounters (x5):** An old ally from the war seeks them out, a coded message arrives from a friendly spy, a bounty hunter discovers the safe house, the party finds a hidden cache of illusion components, a psychic echo from the dragon manifests briefly.
        *   **Embedded Plot Hooks & Rumors (x3):** "General Varrus is secretly leaving us coded messages." "The dragon isn't truly sentient; it's just an echo of our own fears from the war." "There is a counter-ritual that can unmake the dragon, but the components are in enemy territory."
        *   **Sensory Details:** Sight (Maps, disguise kits, old uniforms, dim lighting), Sound (Hushed conversations, the scratching of a quill on a map), Smell (Dust, old canvas, ink).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players use a large-scale illusion to deceive a group of people.
    *   **THEN:** The collective belief of the deceived group strengthens the phantom dragon, making it more powerful and harder to defeat in the next encounter.
    *   **IF:** The players successfully convince a town that the dragon is not real and was just a trick of the light.
    *   **THEN:** The phantom dragon cannot manifest in or near that town, creating a temporary safe zone for the players. However, the dragon's frustration causes it to lash out and attack a different, nearby location more violently.
    *   **IF:** The players are captured by General Varrus.
    *   **THEN:** He does not execute them. Instead, he gives them an off-the-books mission to hunt the dragon, providing them with resources but also a strict time limit and a magical tracker.
    *   **IF:** The players discover that the hobgoblins are attempting a ritual to control the dragon.
    *   **THEN:** They can choose to sabotage the ritual, which will cause the dragon to go on a rampage in hobgoblin territory, or they can try to hijack the ritual for themselves, a difficult and dangerous proposition.
    *   **IF:** In the finale, the players choose to try and redeem their creation instead of destroying it.
    *   **THEN:** Generate a complex, multi-stage skill challenge where the players must use their combined powers of illusion and persuasion to reshape the dragon's nature from a creature of fear into a guardian of peace.
