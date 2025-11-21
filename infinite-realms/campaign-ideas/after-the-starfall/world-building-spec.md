### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**After the Starfall: Embers of Hope**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** Five years after the magical "stars" fell from the sky, the world lies in ruins, its lands corrupted by wild magic and inhabited by dangerous mutated creatures. The players emerge as survivors in this broken world, initially focused on personal survival but gradually drawn into a larger purpose: helping rebuild civilization from the ashes. As they journey across the corrupted wasteland, they discover that the starfall wasn't a random catastrophe but part of a larger pattern that threatens to repeat. The players must balance immediate survival needs with long-term rebuilding efforts while uncovering the starfall's true cause and preventing it from happening again.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the world before the starfall and the society that existed prior to the catastrophe.
    *   Write the history of the starfall event itself - the signs, the impact, and the immediate aftermath.
    *   Describe the evolution of starfall corruption and how it has changed both the landscape and surviving creatures.
    *   Explain the formation of survivor settlements and the various models of post-starfall governance.
    *   Detail the mutated creatures that emerged after the starfall and their behavioral patterns.
    *   Write about the "Starfall Cults" - groups that worship or seek to harness the starfall's power.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Rebuilders Alliance** (Major)
        *   **Goals:** To rebuild civilization while studying and controlling starfall energy for the benefit of all survivors.
        *   **Hierarchy:** Council of settlement leaders, scientists, and community organizers.
        *   **Public Agenda:** We will rebuild a better world from the ashes of the old.
        *   **Secret Agenda:** To harness starfall energy as a power source for the new society.
        *   **Assets:** Network of allied settlements, scientific knowledge, rebuilding expertise.
        *   **Relationships:** Cooperative with most survivor groups; cautious toward starfall cults.
    *   **The Wasteland Nomads** (Major)
        *   **Goals:** To survive in the corrupted wilds while maintaining freedom from settlement constraints.
        *   **Hierarchy:** Tribal structure led by the most experienced survivors and guides.
        *   **Public Agenda:** The wilds provide all we need - settlements are just traps.
        *   **Secret Agenda:** To discover and control the purest sources of starfall energy.
        *   **Assets:** Survival expertise, knowledge of corrupted territories, mobility.
        *   **Relationships:** Trade with settlements when convenient; raid when necessary.
    *   **The Starfall Cult** (Minor)
        *   **Goals:** To embrace starfall corruption as the next stage of evolution and spread it to all survivors.
        *   **Hierarchy:** Theocratic structure led by "Enlightened" individuals who have embraced corruption.
        *   **Public Agenda:** The starfall was a blessing that will remake us all.
        *   **Secret Agenda:** To accelerate the next starfall event for maximum transformation.
        *   **Assets:** Corruption-based powers, mutated followers, hidden corruption sites.
        *   **Relationships:** Hostile toward all who resist corruption; seek to "enlighten" others.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Dr. Elara Voss:** The starfall expert with scientific knowledge and potential culpability.
    *   **Captain Marcus Kane:** The settlement leader with military experience and personal losses.
    *   **The Corrupted Oracle:** The mutated guide who can see possible futures.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Settlement Guard"
    *   "Wasteland Scout"
    *   "Starfall Cultist"
    *   "Mutated Creature Handler"
    *   "Rebuilding Specialist"
    *   "Corruption Researcher"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Impact Crater:** Ground zero of the starfall.
        *   **Key Landmarks:** The Central Pit, the Crystal Spires, the Radiation Fields, the Survivor Camps.
        *   **Primary Inhabitants:** Mutated creatures, brave scavengers, scientific researchers.
        *   **Available Goods & Services:** Rare starfall crystals, pre-starfall technology, survival gear.
        *   **Potential Random Encounters (x5):** A crystal spire pulses with energy, a mutated creature emerges from the pit, discovery of a pre-starfall artifact, a radiation storm forces shelter, a fellow scavenger offers a trade.
        *   **Embedded Plot Hooks & Rumors (x3):** "The crater is growing larger every year." "Some who enter the central pit never return." "The crystals can be used to predict starfall events."
        *   **Sensory Details:** Sight (Shimmering crystal formations, iridescent dust), Sound (Low humming energy, cracking crystals), Smell (Ozone, heated stone).
    *   **New Haven Settlement:** A growing community hub.
        *   **Key Landmarks:** The Central Market, the Defensive Walls, the Community Hall, the Greenhouse Domes.
        *   **Primary Inhabitants:** Survivors of all types, families, workers, guards.
        *   **Available Goods & Services:** Food and water, crafted goods, community services.
        *   **Potential Random Encounters (x5):** A community meeting turns heated, a child discovers a strange artifact, discovery of a theft, a newcomer arrives with news, a celebration brings the community together.
        *   **Embedded Plot Hooks & Rumors (x3):** "The settlement was built on the site of a pre-starfall town." "Some settlers have developed strange abilities." "The greenhouse domes hide a secret research project."
        *   **Sensory Details:** Sight (Makeshift buildings, growing plants), Sound (Community chatter, construction noise), Smell (Cooking food, fresh earth).
    *   **The Corrupted Wilds:** Vast areas transformed by starfall energy.
        *   **Key Landmarks:** The Crystal Forest, the Mutated River, the Echo Caves, the Storm Plains.
        *   **Primary Inhabitants:** Mutated creatures, nomadic survivors, corrupted wildlife.
        *   **Available Goods & Services:** Rare mutated plants, natural resources, survival knowledge.
        *   **Potential Random Encounters (x5):** A mutated creature migration, a starfall storm approaches, discovery of a hidden oasis, a nomad tribe offers guidance, a corrupted area reveals pre-starfall ruins.
        *   **Embedded Plot Hooks & Rumors (x3):** "The wilds remember the old world in strange ways." "Some corrupted areas are actually safer than they appear." "The wilds are evolving toward a new balance."
        *   **Sensory Details:** Sight (Twisted landscapes, glowing mutations), Sound (Strange animal calls, whispering winds), Smell (Damp earth, unknown flowers).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players successfully establish a new settlement.
    *   **THEN:** Other survivors flock to the area, creating opportunities and complications. Generate increased corruption activity as the settlement attracts mutated creatures.
    *   **IF:** The players form an alliance with the Wasteland Nomads.
    *   **THEN:** They gain mobility and survival expertise. Generate scenarios where the nomads' independence creates diplomatic challenges.
    *   **IF:** The players acquire a significant starfall artifact.
    *   **THEN:** Their corruption resistance increases but they attract cult attention. Generate opportunities to study the artifact's properties.
    *   **IF:** The players help a settlement survive a major crisis.
    *   **THEN:** Their reputation grows, leading to more alliance offers. Generate a scenario where their success inspires a larger rebuilding movement.
    *   **IF:** The players embrace corruption for power.
    *   **THEN:** They gain unique abilities but risk losing their humanity. Generate scenarios where their corruption affects their relationships with other survivors.
