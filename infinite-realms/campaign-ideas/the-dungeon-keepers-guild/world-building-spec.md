### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Dungeon Keepers' Guild**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise. The tone is dark comedy, and the players are the underdogs.
*   **Content:** The players are not heroes; they are low-level monsters hired by the incompetent Dungeon Keepers' Guild. Their job is to maintain a dilapidated dungeon, manage its unruly monster population, set traps, and defend it from waves of increasingly annoying and powerful adventurers. The campaign is a reverse dungeon crawl focused on tactical defense, resource management, and dark, slapstick humor.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of the Dungeon Keepers' Guild. Why was it founded, and why is it so underfunded?
    *   Write the story of a legendary dungeon that successfully repelled all adventurers.
    *   Describe the culture and social hierarchy of the dungeon's goblin and kobold inhabitants.
    *   Explain the economics of dungeon keeping. Where does the Guild get its money? What is the pay scale for a goblin minion?
    *   Detail the backstory of Sir Reginald the Righteous and why he is so obsessed with clearing dungeons.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Dungeon Crew (The Players)** (Major)
        *   **Goals:** To keep their dungeon from being cleared, meet their Guild quotas, and maybe get a raise.
        *   **Hierarchy:** A newly-formed management team of low-level monsters.
        *   **Public Agenda:** To be terrifying dungeon monsters.
        *   **Secret Agenda:** To survive the week and stop the other goblins from stealing their lunch.
        *   **Assets:** A dilapidated dungeon, a handful of rusty traps, a population of unruly and cowardly minions.
        *   **Relationships:** Employees of the Guild; adversaries of all adventurers.
    *   **The Dungeon Keepers' Guild** (Major)
        *   **Goals:** To maintain a portfolio of profitable, semi-dangerous dungeons for the adventuring economy.
        *   **Hierarchy:** A sprawling bureaucracy of hobgoblins and other mid-level monsters, led by exasperated overseers like Grizelda.
        *   **Public Agenda:** To provide quality lairs for the discerning monster.
        *   **Secret Agenda:** To cut costs at every opportunity and to ensure that no dungeon becomes *too* successful, as that would upset the balance of the adventuring economy.
        *   **Assets:** A portfolio of failing dungeons, a complex system of forms and regulations, the ability to fire the players.
        *   **Relationships:** The players' employers and a constant source of bureaucratic headaches.
    *   **The Adventuring Parties** (Major)
        *   **Goals:** To get loot, gain experience, and be heroic.
        *   **Hierarchy:** Various independent parties, often led by an overly-charismatic leader like Sir Reginald.
        *   **Public Agenda:** To cleanse the world of evil (i.e., the players).
        *   **Secret Agenda:** To find the quickest path to wealth and fame.
        *   **Assets:** Shiny armor, powerful magic, a complete lack of respect for the players' property.
        *   **Relationships:** The primary antagonists, who keep breaking the players' stuff.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Grizelda, the Guild Overseer:** The perpetually exasperated and sarcastic hobgoblin who manages the players' dungeon.
    *   **Snivvel, the Head Goblin:** The cowardly, lazy, and complaining leader of the dungeon's goblin population.
    *   **Sir Reginald the Righteous:** The arrogant, self-righteous, and recurring adventurer antagonist.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Lazy Goblin Minion"
    *   "Cowardly but Cunning Kobold Trapper"
    *   "Grumpy Ogre Guard"
    *   "Overly Heroic Paladin Adventurer"
    *   "Loot-obsessed Rogue Adventurer"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Trap Workshop:** The grimy, chaotic workshop where the players design and build their traps.
        *   **Key Landmarks:** The blueprint table (covered in failed designs), the scrap pile, the forge, the cage of giant rats used for testing.
        *   **Primary Inhabitants:** The players, kobold assistants.
        *   **Available Goods & Services:** Trap components, tools, a place to experiment.
        *   **Potential Random Encounters (x5):** A trap accidentally triggers, the kobolds go on strike for better tools, the party runs out of a key component, a new, dangerous-looking component is delivered from the Guild, Snivvel tries to "help."
        *   **Embedded Plot Hooks & Rumors (x3):** "The Guild has a secret manual of legendary trap designs, but it's in the Guild library." "You can make a really nasty trap with the venom of a giant spider." "The last crew in this dungeon was wiped out because their own trap backfired."
        *   **Sensory Details:** Sight (Scrap metal, half-finished traps, blueprints), Sound (The clang of hammers, the squeak of rats, kobolds chattering), Smell (Oil, rust, smoke).
    *   **The Monster Barracks:** A chaotic, smelly area where the dungeon's inhabitants live.
        *   **Key Landmarks:** The goblin sleeping pile, the kobold warren, the ogre's corner, the mess hall.
        *   **Primary Inhabitants:** Goblins, kobolds, and any other monsters the players have recruited.
        *   **Available Goods & Services:** Monster recruitment, a source of endless complaints.
        *   **Potential Random Encounters (x5):** A fight breaks out over rations, a monster gets sick, a group of goblins tries to unionize, a monster has a brilliant (or terrible) idea for a new trap, Sir Reginald tries to give a heroic speech to the monsters, hoping to turn them to the side of good.
        *   **Embedded Plot Hooks & Rumors (x3):** "Snivvel is skimming rations from the stores." "The ogre is afraid of mice." "The kobolds have a secret tunnel that leads outside the dungeon."
        *   **Sensory Details:** Sight (Crude furniture, graffiti on the walls, piles of bones), Sound (Bickering, snoring, the sharpening of crude weapons), Smell (Unwashed monsters, stale food, damp stone).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players spend resources to improve the monster barracks.
    *   **THEN:** The dungeon's Monster Morale score increases. Minions are more effective in combat and are less likely to flee.
    *   **IF:** The players successfully defend the dungeon from an adventuring party.
    *   **THEN:** They receive a small resource bonus from the Guild, but the dungeon's "Fame" increases, attracting a more powerful adventuring party for the next wave.
    *   **IF:** The players fail to defend the dungeon and the adventurers reach the (empty) treasure vault.
    *   **THEN:** The adventurers leave, disappointed. The players' dungeon is put on probation by the Guild, and their budget is cut, making the next defense even harder.
    *   **IF:** The players successfully capture an adventurer instead of killing them.
    *   **THEN:** They can interrogate the adventurer for information about other adventuring parties' tactics and weaknesses. However, this also triggers a high-level "rescue mission" from a powerful hero.
    *   **IF:** In the finale, the players manage to defeat Sir Reginald the Righteous.
    *   **THEN:** Generate an epilogue where the players' dungeon is declared the "Most Improved Lair of the Year" by the Dungeon Keepers' Guild. Their reward is a promotion: they are now in charge of a much larger, more dangerous, and even more underfunded dungeon.