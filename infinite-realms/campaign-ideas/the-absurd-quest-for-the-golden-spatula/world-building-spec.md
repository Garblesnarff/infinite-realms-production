### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Absurd Quest for the Golden Spatula**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise. The primary directive is the "Rule of Funny"; logical consistency is secondary to comedic potential.
*   **Content:** The players are hapless "adventurers" hired by the eccentric Lord Flibbertigibbet to retrieve the legendary Golden Spatula. The quest takes them across a land governed by absurd logic, pitting them against spoon-hoarding dragons and philosophical goblins, to win the annual Great Bake-Off, where the Spatula is the grand prize.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. Prioritize humor and absurdity over epic lore.
*   **Prompts:**
    *   Detail the completely fabricated and contradictory history of the Golden Spatula.
    *   Write the story of the founding of the Adventurer's Guild, Local 42, and its transformation into a bureaucratic nightmare.
    *   Describe the legal precedent that led to the Forest Police arresting people for pronoun misuse.
    *   Explain the cultural significance and rules of the Great Bake-Off.
    *   Detail the life story of Baron von Strudel and his history of culinary villainy.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Adventurer's Guild, Local 42** (Major)
        *   **Goals:** To process paperwork, enforce regulations, and ensure all quests are filed in triplicate.
        *   **Hierarchy:** Led by a Guildmaster (a beholder obsessed with paperwork), with numerous clerks and functionaries.
        *   **Public Agenda:** To provide adventurers with sanctioned quests.
        *   **Secret Agenda:** To create more bureaucracy to justify its own existence.
        *   **Assets:** An endless supply of forms, a labyrinthine office building, a pet rust monster.
        *   **Relationships:** A necessary evil for all adventurers.
    *   **The Philosophical Goblins** (Minor)
        *   **Goals:** To ponder the great questions of existence, such as "Why is a raven like a writing desk?"
        *   **Hierarchy:** A leaderless collective where the goblin who makes the most interesting point is listened to for a few minutes.
        *   **Public Agenda:** To achieve enlightenment.
        *   **Secret Agenda:** To find someone who can settle a centuries-old debate about whether a hot dog is a sandwich.
        *   **Assets:** Deep thoughts, confusing questions, a surprising knowledge of logical fallacies.
        *   **Relationships:** Generally peaceful, but will argue with anyone about anything.
    *   **The Fork-Worshipping Dragons** (Minor)
        *   **Goals:** To acquire all the forks in the world.
        *   **Hierarchy:** Led by the silver dragon brother of Ignatius.
        *   **Public Agenda:** To promote the superiority of forks over all other utensils.
        *   **Secret Agenda:** To steal the Golden Spatula because it is technically a type of spoon, their mortal enemy.
        *   **Assets:** A hoard of forks, fire breath, the ability to fly.
        *   **Relationships:** Bitter rivals of the spoon-hoarding dragons.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Lord Flibbertigibbet:** The flamboyant, cheerful, and completely mad quest-giver who is a retired adventurer.
    *   **Baron von Strudel:** The snooty, cheating, and villainous rival of Lord Flibbertigibbet.
    *   **Ignatius the Spoon-Hoarder:** A grumpy, obsessive-compulsive dragon who is terrified of forks.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Contradictory Talking Tree"
    *   "Troll with Terrible Riddles"
    *   "Bureaucratic Beholder Guildmaster"
    *   "Pun-loving City Guard"
    *   "Eccentric Bake-Off Contestant"
    *   "Angry Cockatrice (Ingredient)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections. Prioritize whimsical and nonsensical details.
*   **Location Roster:**
    *   **The Forest of Misdirection:** A forest where all the trees are sentient and love to give contradictory and unhelpful directions.
        *   **Key Landmarks:** The Bridge of Riddles, the clearing of the Philosophical Goblins, a river that flows uphill, a signpost that points in all directions at once.
        *   **Primary Inhabitants:** Talking trees, philosophical goblins, a troll who tells bad jokes.
        *   **Available Goods & Services:** Bad advice, existential dread.
        *   **Potential Random Encounters (x5):** The party is arrested by the Forest Police, a squirrel tries to sell them insurance, they encounter a group of tourists who are hopelessly lost, a tree falls in love with a player, the path loops back on itself.
        *   **Embedded Plot Hooks & Rumors (x3):** "The troll's riddles are the key to a secret treasure." "The goblins know the one true path, but will only reveal it if you can beat them in a debate." "The trees are all lying."
        *   **Sensory Details:** Sight (Purple trees, smiling flowers, confusing signs), Sound (The chatter of trees, goblin debates, the groan of a bad punchline), Smell (Fresh earth, nonsense).
    *   **The Lair of Ignatius:** A cave filled with a truly staggering number of spoons.
        *   **Key Landmarks:** The Great Wall of Spoons, the meticulously organized display of soup ladles, the single, lonely spork kept in a cage, the Golden Spatula being used as a back-scratcher.
        *   **Primary Inhabitants:** Ignatius the dragon.
        *   **Available Goods & Services:** Spoons. So many spoons.
        *   **Potential Random Encounters (x5):** The dragon is polishing his collection, the dragon is having a nightmare about forks, a rival adventurer tries to steal a spoon, the dragon asks the party to appraise a new spoon, the dragon's fork-worshipping brother attacks.
        *   **Embedded Plot Hooks & Rumors (x3):** "Ignatius will trade the Golden Spatula for a legendary, undiscovered spoon." "He is terrified of forks." "He once had a fork, but he buried it in the forest."
        *   **Sensory Details:** Sight (Gleaming metal, spoons of every conceivable size and shape), Sound (The clinking of metal, the dragon's snores, the echo of the cave), Smell (Dragon, old metal, brimstone).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome, prioritizing the funniest possible result.
*   **Triggers:**
    *   **IF:** A player tells a particularly good joke or pun.
    *   **THEN:** Grant that player Inspiration. Generate a temporary, comical effect on the world (e.g., a nearby animal starts laughing uncontrollably).
    *   **IF:** The players fail to correctly fill out Form 27B/6.
    *   **THEN:** The form is sent to the wrong department. Generate a new, absurd side quest where the players must retrieve the form from the "Department of Unnecessary Quests."
    *   **IF:** The players try to fight the dragon Ignatius with forks.
    *   **THEN:** The dragon immediately surrenders and gives them whatever they want, provided they take the terrifying forks away.
    *   **IF:** The players lose the Great Bake-Off.
    *   **THEN:** Baron von Strudel wins. Lord Flibbertigibbet is heartbroken. Generate a new quest where the players must steal the Golden Spatula from the Baron in a farcical heist.
    *   **IF:** The players release the cockatrice during the final round of the bake-off.
    *   **THEN:** The cockatrice turns several judges and contestants to stone. The party is declared the winner by default, as they are the only ones left standing. The stone statues become a local tourist attraction.
