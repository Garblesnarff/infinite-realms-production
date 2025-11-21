### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Forgotten Huntress: Legacy of the Hunt**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The players are drawn into the world of monster hunting when they discover the journal of Elara Voss, the legendary "Forgotten Huntress" who vanished while pursuing her greatest prey. As they follow in her footsteps, tracking the same creatures she hunted, they discover that her disappearance was no accident but part of a larger pattern of hunters becoming the hunted. Each monster they face reveals more about Elara's fate and the philosophical questions she grappled with: When does the hunter become the monster? Can some creatures be redeemed rather than destroyed? The players must decide whether to continue Elara's ruthless legacy or forge a new path that questions the very nature of the hunt.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of monster hunting as a profession and the various guilds and traditions that have developed over centuries.
    *   Write the biography of Elara Voss, from her rise as a legendary huntress to her disappearance and philosophical transformation.
    *   Describe the evolution of monsters from natural creatures to the intelligent beings that challenge hunting ethics.
    *   Explain the development of hunting technology and how it has changed the relationship between hunters and monsters.
    *   Detail the various monster species and their behavioral patterns, cultural structures, and potential for communication.
    *   Write about the "Hunter's Code" - the ethical guidelines that govern monster hunting and the debates about their relevance.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Traditional Hunters Guild** (Major)
        *   **Goals:** To maintain traditional hunting methods and protect humanity from monstrous threats at any cost.
        *   **Hierarchy:** Guild structure led by master hunters with proven track records.
        *   **Public Agenda:** Monsters are threats to be eliminated for the safety of all.
        *   **Secret Agenda:** To suppress knowledge of intelligent monsters to maintain the profession's necessity.
        *   **Assets:** Hunting expertise, monster lore, network of hunting lodges.
        *   **Relationships:** Supportive of traditional hunting; hostile toward those who question monster intelligence.
    *   **The Redemption Society** (Major)
        *   **Goals:** To study monsters and develop non-lethal solutions while protecting both humans and intelligent creatures.
        *   **Hierarchy:** Academic council of researchers, reformed hunters, and monster scholars.
        *   **Public Agenda:** Not all monsters are evil - some can be communicated with or redeemed.
        *   **Secret Agenda:** To establish peaceful coexistence between humans and intelligent monsters.
        *   **Assets:** Research facilities, communication technology, diplomatic connections.
        *   **Relationships:** Allied with monster researchers; opposed by traditional hunting guilds.
    *   **The Monster Collective** (Minor)
        *   **Goals:** To protect intelligent monsters from human hunters while maintaining secrecy about their intelligence.
        *   **Hierarchy:** Council of elder monsters representing different species.
        *   **Public Agenda:** We survive by any means necessary in a world that fears us.
        *   **Secret Agenda:** To reveal monster intelligence when humanity is ready to accept it.
        *   **Assets:** Monster abilities, hidden territories, ancient knowledge.
        *   **Relationships:** Cautious toward all humans; willing to communicate with ethical hunters.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **The Journal's Voice:** The manifested consciousness of Elara Voss sharing her philosophical journey.
    *   **Tracker Marcus Kane:** The traditional hunter representing the old ways of monster hunting.
    *   **The Elder Beast:** The intelligent creature that ended Elara's hunt with wisdom and power.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Veteran Hunter"
    *   "Monster Researcher"
    *   "Redemption Advocate"
    *   "Intelligent Monster"
    *   "Hunting Guide"
    *   "Ethical Philosopher"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **Elara's Lodge:** The abandoned hunting lodge containing her legacy.
        *   **Key Landmarks:** The Journal Library, the Trophy Room, the Preparation Chamber, the Meditation Garden.
        *   **Primary Inhabitants:** The Journal's Voice, visiting hunters, curious researchers.
        *   **Available Goods & Services:** Hunting lore, monster research, philosophical guidance.
        *   **Potential Random Encounters (x5):** The journal reveals a new entry, a trophy comes to life, discovery of a hidden research note, a fellow hunter seeks collaboration, a monster appears in the meditation garden.
        *   **Embedded Plot Hooks & Rumors (x3):** "The lodge remembers every hunt that ever started here." "Some trophies contain the spirits of the monsters they represent." "The meditation garden shows visions of possible hunts."
        *   **Sensory Details:** Sight (Dusty hunting equipment, faded monster trophies), Sound (Creaking floorboards, whispering pages), Smell (Aged leather, wood polish).
    *   **The Whispering Woods:** An ancient forest where hunter and hunted blur.
        *   **Key Landmarks:** The Ancient Grove, the Hunter's Trail, the Monster Glade, the Ethical Crossroads.
        *   **Primary Inhabitants:** Intelligent monsters, traditional hunters, redemption researchers.
        *   **Available Goods & Services:** Natural resources, monster intelligence, ethical guidance.
        *   **Potential Random Encounters (x5):** A monster observes from the shadows, a hunter's trap is discovered, discovery of a monster's cultural artifact, a researcher requests assistance, an ethical dilemma presents itself.
        *   **Embedded Plot Hooks & Rumors (x3):** "The woods judge those who enter based on their intentions." "Some monsters use the woods to communicate with hunters." "The ancient grove contains the original monster that started it all."
        *   **Sensory Details:** Sight (Towering ancient trees, subtle monster signs), Sound (Rustling leaves, distant animal calls), Smell (Damp earth, wild flowers).
    *   **The Beast's Lair:** The territory of the ultimate prey.
        *   **Key Landmarks:** The Crystal Cave, the Trophy Collection, the Wisdom Pool, the Final Chamber.
        *   **Primary Inhabitants:** The Elder Beast, lesser monsters, trapped spirits of previous hunters.
        *   **Available Goods & Services:** Ancient knowledge, monster wisdom, hunting redemption.
        *   **Potential Random Encounters (x5):** A trapped hunter's spirit seeks release, the Elder Beast tests the players' intentions, discovery of Elara's final camp, a monster guardian demands a philosophical debate, a vision reveals hunting truths.
        *   **Embedded Plot Hooks & Rumors (x3):** "The lair contains the memories of every hunter who ever entered." "The Elder Beast knows the true nature of monstrosity." "The wisdom pool shows what hunters could become."
        *   **Sensory Details:** Sight (Glowing crystals, ancient carvings), Sound (Echoing wisdom, dripping water), Smell (Mineral springs, ancient stone).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players successfully communicate with an intelligent monster.
    *   **THEN:** They gain unique knowledge and potential allies. Generate scenarios where this communication creates conflict with traditional hunters.
    *   **IF:** The players choose mercy over killing in a significant hunt.
    *   **THEN:** Their reputation with intelligent monsters improves. Generate opportunities for redemption and alliance with monster factions.
    *   **IF:** The players embrace traditional hunting philosophy.
    *   **THEN:** They gain support from hunting guilds but alienate monster researchers. Generate scenarios where this choice creates moral conflicts.
    *   **IF:** The players discover evidence of Elara's transformation.
    *   **THEN:** They gain philosophical insights but risk corruption. Generate scenarios where Elara's fate influences their own moral journey.
    *   **IF:** The players confront the Elder Beast with understanding rather than violence.
    *   **THEN:** They may achieve true redemption for Elara's legacy. Generate a scenario where the Beast reveals the ultimate truth about hunting and monstrosity.
