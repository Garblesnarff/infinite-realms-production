### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Sand-Swallowed Legion**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** Based on the historical mystery of Cambyses' Lost Army, the players are hired to find a lost artifact carried by the army's general. They discover the 50,000 soldiers were not killed by a sandstorm but were imprisoned in a desert demiplane by a cruel Djinni. Now an undead army, the legion serves their genie master, and the players must enter this hostile plane to retrieve the artifact, either by fighting the legion, breaking their curse, or bargaining with the Djinni.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the historical account of Cambyses' army and its mission to the Oasis of Siwa.
    *   Write the story of the Djinni. Why was it in the desert, and what offense did the army commit to warrant their imprisonment?
    *   Describe the nature of the desert demiplane. What are its physical laws? How does time move differently there?
    *   Explain the curse of undeath that afflicts the legion. How does it work, and can it be broken?
    *   Detail the legend of the *Helm of the Unsetting Sun* and its powers.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Expedition (The Players)** (Minor)
        *   **Goals:** To find and retrieve the *Helm of the Unsetting Sun*.
        *   **Hierarchy:** A small, independent group of adventurers.
        *   **Public Agenda:** To find a lost historical artifact.
        *   **Secret Agenda:** To survive the horrors of the demiplane and escape with their lives.
        *   **Assets:** A magical compass, their skills, and any alliances they can forge within the demiplane.
        *   **Relationships:** In conflict with the Sand-Swallowed Legion; viewed as toys by the Djinni.
    *   **The Sand-Swallowed Legion** (Major)
        *   **Goals:** To serve the will of their Djinni master and defend their desert prison from intruders.
        *   **Hierarchy:** A disciplined undead army commanded by a Mummy Lord general.
        *   **Public Agenda:** To obey their master.
        *   **Secret Agenda:** The general and some of his officers retain a sliver of their former selves and secretly seek a way to break the curse or find honorable death.
        *   **Assets:** An army of 50,000 disciplined undead soldiers, centuries of tactical experience in their environment, sand-fused bronze armor.
        *   **Relationships:** The primary antagonists, but also tragic victims.
    *   **The Djinni** (Major)
        *   **Goals:** To alleviate its eternal boredom.
        *   **Hierarchy:** A single, immensely powerful, and cruel entity.
        *   **Public Agenda:** None.
        *   **Secret Agenda:** To find a new champion or plaything, as it has grown bored of the legion.
        *   **Assets:** God-like control over the desert demiplane, powerful magic, an army of undead.
        *   **Relationships:** The ultimate power in the demiplane, views all others as insignificant.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **The Djinni:** An ancient, powerful, cruel, and bored genie who rules the demiplane.
    *   **General Akhenaten:** The Mummy Lord commander of the legion, a brilliant tactician who longs for release.
    *   **The Oasis Spirit:** A benevolent water elemental or fey spirit that maintains the single safe haven in the demiplane.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Desiccated Legionary (Undead Creature)"
    *   "Undead Legion Centurion"
    *   "Mirage Beast (Creature)"
    *   "Sand-Burrowing Horror (Creature)"
    *   "Trapped Soul of a Soldier"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Brass Sky Desert:** The main environment of the demiplane, a vast desert of black sand under a burning brass sun.
        *   **Key Landmarks:** The skeletal remains of giant desert creatures, a field of glass created by the sun's heat, a canyon where the legion's archers practice, the Oasis of Lost Souls.
        *   **Primary Inhabitants:** The Sand-Swallowed Legion, sand-burrowing monsters, hostile mirages.
        *   **Available Goods & Services:** None. This is a hostile wilderness.
        *   **Potential Random Encounters (x5):** A patrol of legionaries, a sudden, life-draining sandstorm, a hostile mirage attacks, the party finds the remains of another creature that was trapped here, the Djinni speaks to the party on the wind.
        *   **Embedded Plot Hooks & Rumors (x3):** "The legion's general resides in the army's fortified command camp." "The Oasis of Lost Souls is the only place with clean water." "The Djinni sometimes forces his soldiers to fight each other for his amusement."
        *   **Sensory Details:** Sight (Black sand, a brass-colored sky, heat haze), Sound (The howling of the wind, the scrape of sand on armor), Smell (Hot air, sand, a complete lack of any organic scent).
    *   **The Legion's Command Camp:** A fortified camp that serves as the headquarters for the undead army.
        *   **Key Landmarks:** The general's command tent, the armory, the training grounds, the pens for captured desert beasts.
        *   **Primary Inhabitants:** The Mummy Lord general, his elite guard, thousands of legionaries.
        *   **Available Goods & Services:** None. This is the enemy stronghold.
        *   **Potential Random Encounters (x5):** The party witnesses a tactical briefing, a legionary is being punished for a minor infraction, the general is inspecting his troops, the party finds a hidden cache of ancient Persian artifacts, the Djinni appears to give the general new orders.
        *   **Embedded Plot Hooks & Rumors (x3):** "The *Helm of the Unsetting Sun* is worn by the general." "The general still keeps a journal, written in a long-dead language." "There is a faction within the legion that seeks to rebel against the Djinni."
        *   **Sensory Details:** Sight (Disciplined ranks of undead soldiers, ancient but well-maintained military equipment, military standards), Sound (The clatter of armor, shouted commands in an ancient language, an eerie silence), Smell (Dust, old bronze, embalming fluid).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players are caught in the open under the brass sun for too long.
    *   **THEN:** They must make Constitution saving throws against magical exhaustion, which cannot be removed by normal rest until they find shelter.
    *   **IF:** The players choose to bargain with the Djinni.
    *   **THEN:** The Djinni agrees to give them the Helm, but only if they complete an impossible and morally compromising task for his amusement (e.g., "Make my general feel true despair," or "Bring me the tears of the Oasis Spirit").
    *   **IF:** The players discover the rebellious faction within the legion.
    *   **THEN:** They can choose to aid this faction in their rebellion. This provides them with allies but also alerts the Djinni directly to their presence, causing him to take a personal, and dangerous, interest in them.
    *   **IF:** The players manage to defeat General Akhenaten in combat.
    *   **THEN:** The legion's command structure collapses into chaos, making it easier to navigate the demiplane. However, the Djinni, annoyed at the loss of his general, animates a new, even more powerful commander from the sand itself.
    *   **IF:** The players find a way to break the curse on the legion.
    *   **THEN:** The 50,000 soldiers are finally granted true death. Their souls, released all at once, tear a temporary hole in the demiplane, allowing the players to escape. The Djinni, now alone and bored, may seek revenge on the players in the future.
