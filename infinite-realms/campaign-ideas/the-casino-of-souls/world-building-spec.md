### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Casino of Souls**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The players are a crew of elite thieves hired by a mysterious patron to rob the Casino of Souls, the most secure gambling den in the multiverse. The casino is owned by the archdevil Mammon, and its vault contains the souls of a thousand mortal kings. The party must pull off an impossible heist, outsmarting demonic security, magical traps, and a clientele of the multiverse's most powerful and dangerous beings.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of the city of Fortuna and its pact with the archdevil Mammon.
    *   Write the story of the construction of the Casino of Souls and the binding of the living casino entity.
    *   Describe the infernal laws that govern contracts and debts in Fortuna.
    *   Explain the nature of "Soul Gems" and how they are used as currency and power sources.
    *   Detail the legend of a previous thief who attempted to rob the casino and their terrible fate.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Heist Crew (The Players)** (Major)
        *   **Goals:** To steal the souls from the vault and escape with their lives and their own souls intact.
        *   **Hierarchy:** A team of specialists, likely with a de facto leader for the operation.
        *   **Public Agenda:** To be high-rolling gamblers and tourists.
        *   **Secret Agenda:** To execute the heist and fulfill their contract with their mysterious patron.
        *   **Assets:** Their specialized skills, a set of incomplete blueprints, a mysterious patron.
        *   **Relationships:** Employed by Asmodeus (secretly); targets of Mammon's security.
    *   **Mammon's Operations** (Major)
        *   **Goals:** To maintain the casino's security, profitability, and reputation.
        *   **Hierarchy:** Led by the archdevil Mammon, with Lilith as the head of security.
        *   **Public Agenda:** To provide the ultimate high-stakes entertainment experience.
        *   **Secret Agenda:** To collect rare and powerful souls to increase Mammon's power in the infernal hierarchy.
        *   **Assets:** The living casino itself, an army of demonic security, magical wards, a network of informants.
        *   **Relationships:** The primary antagonists, viewing the players as insects to be crushed.
    *   **Asmodeus's Conspiracy** (Major)
        *   **Goals:** To destabilize Mammon's operation and usurp his power.
        *   **Hierarchy:** Led by the archdevil Asmodeus, who operates through cut-outs and mysterious patrons.
        *   **Public Agenda:** None.
        *   **Secret Agenda:** To use the players as disposable pawns to steal Mammon's most valuable assets.
        *   **Assets:** Vast resources, deep knowledge of infernal politics, a willingness to sacrifice anyone.
        *   **Relationships:** The secret patron of the players and the true puppet master of the campaign.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Mammon:** The suave, sophisticated, and utterly evil archdevil owner of the casino.
    *   **Asmodeus:** The cunning, patient, and manipulative rival archdevil who acts as the party's secret patron.
    *   **Lilith:** The powerful, paranoid, and sadistic pit fiend head of security, who is secretly in love with a soul in the vault.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Disgruntled Croupier (Inside Man)"
    *   "High-Roller Whale (Mark)"
    *   "Infernal Bouncer (Guard)"
    *   "Soulless Bartender"
    *   "Rival Thief"
    *   "Obsidian Golem (Creature)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Main Casino Floor:** A massive, opulent space designed to overwhelm the senses and encourage reckless gambling.
        *   **Key Landmarks:** The Soul-Slot Machines, the River of Styx Roulette Table, the Gilded Cage (for high-limit poker), the Brass Minotaur Bar.
        *   **Primary Inhabitants:** High-rolling mortals, devils in disguise, succubus cocktail waitresses, eagle-eyed security demons.
        *   **Available Goods & Services:** Games of chance, magically-infused cocktails, the opportunity to wager your soul.
        *   **Potential Random Encounters (x5):** A high-roller has a dramatic, soul-losing meltdown; security detains a cheater; a rival thief tries to pickpocket a player; a player is offered a drink that is actually a truth serum; Lilith is seen observing the floor.
        *   **Embedded Plot Hooks & Rumors (x3):** "The head of security, Lilith, has a weakness for poetry." "The only person who ever won big and left with their soul was a bard who sang a song of true love." "The casino's plumbing system connects to the vault's cooling system."
        *   **Sensory Details:** Sight (Glittering lights, gold and brass fixtures, elegant but demonic clientele), Sound (The constant chime of slot machines, the clatter of chips, smooth jazz), Smell (Expensive perfume, cigar smoke, a faint hint of brimstone).
    *   **The Vault of Souls:** A high-security vault of obsidian and brass, located in the heart of the casino.
        *   **Key Landmarks:** The Three-Key Door, the Obsidian Golem Guardian, the racks of glowing Soul Gems, the central vault containing the thousand king-souls.
        *   **Primary Inhabitants:** The Obsidian Golem, magical traps, the trapped essence of the souls themselves.
        *   **Available Goods & Services:** None. This is the objective.
        *   **Potential Random Encounters (x5):** A magical ward triggers, a silent alarm is tripped, the ghost of a trapped soul manifests and begs for freedom, the vault door begins to close, a patrol of infernal guards phases through the wall.
        *   **Embedded Plot Hooks & Rumors (x3):** "One of the king-souls in the vault belongs to Lilith's mortal lover." "The vault is not just a room; it's a living creature that feeds on magical energy." "There is a secret emergency exit, but it leads directly to Mammon's office."
        *   **Sensory Details:** Sight (Gleaming obsidian, glowing gems, intricate locking mechanisms), Sound (A low, magical hum; the whispers of trapped souls; the party's own heartbeats), Smell (Cool, sterile air; ozone; ancient dust).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players take a risky action or fail a key skill check during the heist.
    *   **THEN:** The party's "Heat" level increases. Generate a corresponding security escalation (e.g., more guards on patrol, Lilith begins actively reviewing security footage, magical wards are intensified).
    *   **IF:** The players successfully recruit the disgruntled croupier as an inside man.
    *   **THEN:** The croupier provides a key piece of information or a security keycard, but also becomes a liability who might crack under pressure if the Heat gets too high.
    *   **IF:** The players discover Lilith's secret love for one of the souls in the vault.
    *   **THEN:** They can use this information to blackmail her, forcing her to look the other way at a critical moment. This will make her a powerful, vengeful enemy after the heist is over.
    *   **IF:** The party is caught before reaching the vault.
    *   **THEN:** Generate a social combat encounter where the party must talk their way out of it or make a deal with Mammon, likely resulting in a new, even more dangerous quest in his service.
    *   **IF:** The party chooses to free the souls instead of delivering them to their patron, Asmodeus.
    *   **THEN:** They complete the heist but fail their contract. Mammon is enraged, and Asmodeus is furious. Generate an epilogue where the party is now hunted by the forces of two of the most powerful archdevils in the multiverse.
