### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Wandering Hearth**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise. The tone is cozy, humorous, and low-stakes.
*   **Content:** The players inherit "The Wandering Hearth," a magical tavern that appears in a different location each week. Their task is to manage the tavern, serving a diverse clientele of adventurers, monsters, and planar travelers, while dealing with magical mishaps, eccentric staff, and the occasional quest that walks right through their enchanted doors.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of The Wandering Hearth. Who was the original owner, and how did they enchant it?
    *   Write the story of the tavern's most famous (or infamous) past patron.
    *   Describe the magical mechanics of the tavern's weekly relocation. Is it random, or is there a pattern?
    *   Explain the rules and regulations of the Interplanar Guild of Innkeepers.
    *   Detail the legend of a specific rare ingredient that can only be found when the tavern appears in a certain dimension.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Hearthtenders (The Players)** (Major)
        *   **Goals:** To run a successful and profitable tavern, keep their staff happy, and solve the mystery of the tavern's magic.
        *   **Hierarchy:** A small team of co-owners or a manager with their staff.
        *   **Public Agenda:** To be the best and most welcoming tavern in the multiverse.
        *   **Secret Agenda:** To keep the tavern's true nature a secret from the mundane authorities of each new location.
        *   **Assets:** The magical tavern itself, a quirky but loyal staff, a growing book of unique recipes.
        *   **Relationships:** Business relationships with a vast array of patrons; rivals with a competing magical establishment.
    *   **The Guild of Planar Innkeepers** (Major)
        *   **Goals:** To regulate all magical establishments and ensure they adhere to a ridiculously long list of rules.
        *   **Hierarchy:** A sprawling bureaucracy of inspectors, accountants, and rule-makers.
        *   **Public Agenda:** To ensure safety and quality across the planes.
        *   **Secret Agenda:** To acquire or shut down The Wandering Hearth, which they see as an unlicensed and dangerously unpredictable anomaly.
        *   **Assets:** The authority to levy fines and revoke licenses, a network of inspectors, a powerful rulebook.
        *   **Relationships:** The primary antagonists, representing the threat of soul-crushing bureaucracy.
    *   **The Regulars** (Minor)
        *   **Goals:** To have a good time, a stiff drink, and a place that feels like home.
        *   **Hierarchy:** A loose collection of recurring patrons, each with their own stories and problems.
        *   **Public Agenda:** To be loyal customers.
        *   **Secret Agenda:** Many have small, personal quests or secrets they may eventually entrust to the players.
        *   **Assets:** Their individual skills (which may be formidable), a deep loyalty to the tavern.
        *   **Relationships:** The players' primary source of quests, income, and complications.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Bartholomew "Barty" Brewmaster:** The grumpy but helpful ghost of the previous owner, who is bound to the tavern.
    *   **Flicker, the Fairy Bartender:** A mischievous, flighty, and accident-prone fairy who serves the drinks.
    *   **A Guild Inspector:** A stuffy, rule-bound, and perpetually unimpressed inspector from the Guild of Planar Innkeepers.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Grumpy Goblin Cook"
    *   "Sentient, Helpful Broom (Creature)"
    *   "World-weary Adventurer Patron"
    *   "Planar Merchant Patron"
    *   "Rival Tavern Owner"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Common Room:** The heart of The Wandering Hearth, a cozy and ever-so-slightly chaotic space.
        *   **Key Landmarks:** The bar (tended by Flicker), the roaring fireplace (where Barty's ghost often appears), the table of regulars, the quest board.
        *   **Primary Inhabitants:** The players, their staff, a diverse clientele of patrons.
        *   **Available Goods & Services:** Food, drink, lodging, rumors, quests.
        *   **Potential Random Encounters (x5):** A bar brawl breaks out, a powerful wizard challenges a player to a drinking contest, a monster patron accidentally sets something on fire, a famous adventurer walks in, a new, strange dish on the menu has an unexpected magical side effect.
        *   **Embedded Plot Hooks & Rumors (x3):** "Barty knows the secret to controlling the tavern's jumps, but he won't tell." "A regular is looking for a crew to help them with a personal quest." "The Guild of Innkeepers is planning a surprise inspection next week."
        *   **Sensory Details:** Sight (Warm, inviting light; mismatched furniture; strange and wonderful patrons), Sound (The crackle of the fire, the chatter of a happy crowd, music), Smell (Roasting meat, ale, woodsmoke).
    *   **The Enchanted Cellar:** A magically expanded cellar that is much larger on the inside.
        *   **Key Landmarks:** The wine rack that contains bottles from different dimensions, a door that leads to a random past location of the tavern, a pile of forgotten, cursed items, the tavern's magical power source.
        *   **Primary Inhabitants:** Cellar sprites, a few escaped ingredients (like a sentient cabbage), Barty's ghost.
        *   **Available Goods & Services:** Storage, rare ingredients.
        *   **Potential Random Encounters (x5):** A cask of ale has been replaced by a mimic, a door to a dangerous dimension temporarily opens, a forgotten magical item activates, the party finds a diary from a previous owner, the power source begins to malfunction.
        *   **Embedded Plot Hooks & Rumors (x3):** "The tavern's power source needs a rare component to be stabilized." "Barty hid his life savings somewhere in the cellar before he died." "There is a map to a legendary vineyard hidden in one of the wine bottles."
        *   **Sensory Details:** Sight (Dimly lit, vast, cluttered with barrels and crates), Sound (The drip of condensation, the scuttling of small creatures), Smell (Damp earth, aging wine, dust).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players successfully create a new, popular dish for the menu.
    *   **THEN:** The tavern's Reputation score increases. Generate a new, high-paying "Regular" patron who was drawn to the tavern by tales of its food.
    *   **IF:** The players fail to deal with a magical mishap (e.g., the overflowing tankards).
    *   **THEN:** The tavern's Reputation score decreases. The Guild of Planar Innkeepers hears about the incident and schedules a surprise inspection.
    *   **IF:** The tavern appears in a dangerous location (e.g., the Nine Hells).
    *   **THEN:** Generate a special event where the players must adapt their menu and services for a clientele of devils and demons, and survive the night without losing their souls.
    *   **IF:** The players successfully help a Regular patron with their personal quest.
    *   **THEN:** That patron becomes a staunch ally, providing a unique boon for the tavern (e.g., the adventurer provides free security, the merchant sets up a reliable supply line).
    *   **IF:** In the finale, the players discover the tavern is a sentient, lonely creature.
    *   **THEN:** Generate a final choice. Do they sever its magic to give it a permanent, peaceful home, or do they agree to become its permanent companions, embracing a life of endless wandering and adventure?
