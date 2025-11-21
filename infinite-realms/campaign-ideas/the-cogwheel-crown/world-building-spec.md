### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Cogwheel Crown**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The city-state of Veridia is on the cusp of a magical industrial revolution powered by Aether-Crystals. This progress has created deep divisions between the old noble houses, the burgeoning merchant guilds, and the exploited working class. The players are caught in the middle of this conflict, hired to navigate a landscape of corporate espionage and political intrigue, only to uncover a shadowy cartel, the Aetherium Syndicate, that seeks to control the city by manipulating all sides.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the discovery of Aether-Crystals and the dawn of Veridia's magical industrial revolution.
    *   Write the history of the Volkov noble house and their traditionalist view of magic.
    *   Describe the rise of the merchant guilds and their role in pioneering Aether-Crystal technology.
    *   Explain the social and economic conditions of the Foundry District and the reasons for the growing workers' unrest.
    *   Detail the history and stated goals of the Aetherium Syndicate, as they are known to the outside world (if at all).

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Noble Houses (The Traditionalists)** (Major)
        *   **Goals:** To maintain their political power and preserve the traditions of "true" magic.
        *   **Hierarchy:** A council of noble families, led by the cunning Baroness Seraphina Volkov.
        *   **Public Agenda:** To ensure the city's progress is managed responsibly and safely.
        *   **Secret Agenda:** To sabotage Aether-Crystal technology, which they see as a threat to their magical dominance, and secretly fund Luddite mages.
        *   **Assets:** Ancestral wealth, political control of the City Council, traditional magic users, a private guard.
        *   **Relationships:** In a cold war with the Merchant Guilds; disdainful of the working class.
    *   **The Merchant Guilds (The Innovators)** (Major)
        *   **Goals:** To champion innovation, control the Aether-Crystal market, and usurp political power from the nobles.
        *   **Hierarchy:** A coalition of powerful guilds, with Master Inventor Silas Vane as their most prominent voice.
        *   **Public Agenda:** To bring prosperity to all through technology.
        *   **Secret Agenda:** To create a corporate oligarchy, replacing the nobility as the city's rulers.
        *   **Assets:** Control of factories and trade, vast wealth, cutting-edge technology, corporate spies.
        *   **Relationships:** In direct competition with the Noble Houses; exploit the working class.
    *   **The Aetherium Syndicate** (Major)
        *   **Goals:** To monopolize the world's Aether-Crystal supply.
        *   **Hierarchy:** A ruthless cartel led by a shadowy council, with Kael, the Silent Hand, as their Veridia operations chief.
        *   **Public Agenda:** None. They operate in complete secrecy.
        *   **Secret Agenda:** To destabilize Veridia by fueling the conflict between nobles and merchants, allowing them to seize the mines in the ensuing chaos.
        *   **Assets:** A network of saboteurs and assassins, advanced technology, deep financial reserves.
        *   **Relationships:** The secret antagonist, manipulating all other factions.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Baroness Seraphina Volkov:** The elegant, cunning, and ruthless leader of the noble faction.
    *   **Master Inventor Silas Vane:** The brilliant, idealistic, and unknowingly manipulated leader of the merchant guilds.
    *   **Kael, the Silent Hand:** The cold, calculating, and ruthless leader of the Aetherium Syndicate's local operations.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Disgruntled Factory Worker"
    *   "Ambitious Merchant Guild Apprentice"
    *   "Arrogant Noble Mage"
    *   "Syndicate Saboteur"
    *   "Clockwork Automaton Sentry (Creature)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Foundry District:** A sprawling, smoke-choked industrial zone filled with factories and worker housing.
        *   **Key Landmarks:** The main Aether-Crystal refinery, the automaton assembly line, the worker's tavern "The Grimy Cog," the union meeting hall.
        *   **Primary Inhabitants:** Factory workers, guild foremen, union organizers, urchins.
        *   **Available Goods & Services:** Black market for industrial parts, cheap food and lodging, a hotbed of revolutionary sentiment.
        *   **Potential Random Encounters (x5):** A factory machine goes haywire, a workers' strike turns into a riot, a Syndicate agent is seen sabotaging a conduit, a child has fallen into a dangerous part of the factory, the party is offered a bribe by a guild foreman.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Syndicate is paying workers to strike." "Silas Vane is planning to replace most of the workers with automatons." "There's a secret entrance to the Aether-Crystal mines in the oldest part of the district."
        *   **Sensory Details:** Sight (Smog, steam, glowing crystals, grimy faces), Sound (The constant clang and hum of machinery, shouting, steam whistles), Smell (Coal smoke, oil, metal, unwashed bodies).
    *   **The Whispering Veins:** The deep Aether-Crystal mines beneath Veridia, pulsing with raw, dangerous magic.
        *   **Key Landmarks:** The Primary Vein, a chasm filled with raw magical energy, an abandoned mining tunnel, the Syndicate's hidden headquarters.
        *   **Primary Inhabitants:** Miners, Syndicate guards, crystal-infused elementals, mutated creatures.
        *   **Available Goods & Services:** Raw Aether-Crystals.
        *   **Potential Random Encounters (x5):** A tunnel collapses, a pocket of raw magical energy is breached, the party finds the body of a missing miner, a Syndicate patrol attacks, a massive, crystalline creature awakens.
        *   **Embedded Plot Hooks & Rumors (x3):** "The largest Aether-Crystal, the 'Heart of the Mountain,' is the Syndicate's ultimate prize." "Kael, the Syndicate leader, was once a miner here." "The crystals whisper to those who spend too long in the mines."
        *   **Sensory Details:** Sight (Glowing crystals, dark tunnels, shimmering magical energy), Sound (The ring of pickaxes, the hum of raw magic, the skittering of unseen creatures), Smell (Ozone, damp earth, a strange, electric scent).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** A player chooses to use the "Aether-Crystal Overcharge" mechanic and rolls a 1.
    *   **THEN:** Generate a wild magic surge. The effect should be technological in nature (e.g., a player's weapon transforms into a useless but shiny object, a nearby automaton becomes sentient and friendly, a burst of energy shorts out all tech in a 30-foot radius).
    *   **IF:** The players choose to side with the Noble Houses.
    *   **THEN:** They gain access to powerful, traditional magic and political influence, but the Merchant Guilds brand them as enemies of progress, sending corporate spies and saboteurs after them.
    *   **IF:** The players successfully expose the Aetherium Syndicate's plot to the City Council.
    *   **THEN:** The Syndicate is forced to accelerate its plans, launching a direct, military-style assault on the Aether-Crystal mines, turning the political intrigue into an open war.
    *   **IF:** The players assassinate a key leader from either the Noble or Merchant factions.
    *   **THEN:** The fragile balance of power shatters. Generate a series of urban combat encounters as the city descends into open street fighting between the factions.
    *   **IF:** In the finale, the players seize control of the Aetherium Syndicate for themselves.
    *   **THEN:** Generate an epilogue where the players are now the secret rulers of Veridia's energy supply. They must contend with the remnants of the other factions and the international powers who want a piece of their new monopoly.
