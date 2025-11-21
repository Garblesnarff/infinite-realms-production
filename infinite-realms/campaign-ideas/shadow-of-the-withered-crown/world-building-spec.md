### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**Shadow of the Withered Crown**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** In a kingdom ravaged by an eternal, supernatural blight, the players discover an ancient crown that promises to restore the land but corrupts its wearer with visions of forgotten horrors. As famine and undead hordes spread, the party must navigate alliances with desperate factions, uncover the crown's dark origins tied to a divine betrayal, and decide whether to wield the crown's power or destroy it, risking the kingdom's total collapse.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of the kingdom before the blight, describing its prosperity and its relationship with the gods.
    *   Write the full story of the divine betrayal that caused the blight. Which god was involved, and why?
    *   Describe the creation of the Withered Crown and its intended purpose.
    *   Explain the nature of the blight. How does it spread? What are its effects on flora, fauna, and people?
    *   Detail the story of the last hero who attempted to use the crown and became the corrupted antagonist, Sylas the Undying.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Bandit Confederacy** (Major)
        *   **Goals:** To survive and profit from the chaos.
        *   **Hierarchy:** A loose alliance of bandit gangs, led by the pragmatic Elara Voss.
        *   **Public Agenda:** We are survivors, taking what we need to live.
        *   **Secret Agenda:** Elara Voss is secretly afflicted by the blight and seeks the crown as a potential cure, regardless of the cost to the kingdom.
        *   **Assets:** Control of key trade routes, a network of spies and smugglers, a fortified hideout.
        *   **Relationships:** Wary of all other factions, but willing to make temporary alliances for profit.
    *   **The Circle of Thorns** (Major)
        *   **Goals:** To restore the kingdom by any means necessary, including wielding the crown's power.
        *   **Hierarchy:** A council of nobles and knights led by the manipulative Lord Garrick Hale.
        *   **Public Agenda:** To unite the survivors and find a cure for the blight.
        *   **Secret Agenda:** To seize the crown and establish a new dynasty under Lord Hale's rule, even if it means making pacts with dark powers.
        *   **Assets:** A small but well-equipped army, a fortified citadel, political legitimacy.
        *   **Relationships:** Views the bandits as criminals; sees the priesthood as weak and ineffective.
    *   **The Fading Priesthood** (Minor)
        *   **Goals:** To find a divine solution to the blight and ease the suffering of the people.
        *   **Hierarchy:** A scattered and broken church, loosely guided by the cynical Thrain Blackthorn.
        *   **Public Agenda:** To offer healing and hope.
        *   **Secret Agenda:** Thrain knows the blight is divine in origin and seeks to atone for the priesthood's past failures by destroying the crown, which he sees as an abomination.
        *   **Assets:** Ancient lore, hidden relics, the trust of the common folk.
        *   **Relationships:** Distrusts all other factions, believing they are too worldly to understand the true nature of the curse.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Elara Voss:** The ruthless and pragmatic Bandit Queen, secretly afflicted by the blight.
    *   **Thrain Blackthorn:** The cynical and brooding Fallen Priest, who knows the blight's true origin.
    *   **Lord Garrick Hale:** The charismatic and manipulative noble who seeks to use the crown to seize power.
    *   **Sylas the Undying:** The final antagonist, a former hero corrupted by the crown, who now believes the blight purifies the weak.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Desperate Village Refugee"
    *   "Ruthless Bandit Thug"
    *   "Hopeful but Naive Priest"
    *   "Blighted Zombie (Creature)"
    *   "Corrupted Wildlife (Creature)"
    *   "Scheming Noble"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Whispering Woods:** A fog-shrouded forest filled with illusory traps and corrupted wildlife.
        *   **Key Landmarks:** The Seer's Glade, a grove of weeping, blighted trees, the ruins of an ancient shrine, a bandit ambush point.
        *   **Primary Inhabitants:** Corrupted beasts, bandits, the enigmatic Seer Mirael.
        *   **Available Goods & Services:** Rare, blight-resistant herbs; secrets (for a price).
        *   **Potential Random Encounters (x5):** A pack of blight-hounds, a sudden, thick fog that causes confusion, the party stumbles upon a secret bandit cache, a ghostly vision of the past plays out, the trees themselves seem to whisper warnings.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Seer can only be found when the moon is full." "The bandits have a secret path through the woods." "The heart of the forest is the most blighted place in the kingdom, but it holds a great power."
        *   **Sensory Details:** Sight (Fog, twisted trees, sickly green moss), Sound (The rustle of dead leaves, the snap of twigs, an unnatural silence), Smell (Decay, damp earth, corruption).
    *   **Blackthorn Citadel:** An abandoned fortress atop a hill, riddled with puzzles and guardian spirits.
        *   **Key Landmarks:** The Hall of Heroes, the Grand Library (now in ruins), the Vault of the Forgotten Gods, the bell tower.
        *   **Primary Inhabitants:** Guardian spirits, ghosts of the citadel's former defenders, squatting bandits.
        *   **Available Goods & Services:** Salvageable ancient weapons, lore and historical records.
        *   **Potential Random Encounters (x5):** A patrol of ghostly guards, a collapsing floor reveals a hidden catacomb, a puzzle-locked door, the party finds the diary of a long-dead knight, a rival faction is also exploring the citadel.
        *   **Embedded Plot Hooks & Rumors (x3):** "The key to the vault is hidden in the library." "Lord Hale's ancestors were the last lords of this citadel." "The ghosts here are not hostile, but are trying to warn people away from a great evil."
        *   **Sensory Details:** Sight (Crumbling stone, dusty banners, ghostly apparitions), Sound (Echoing footsteps, the wind whistling through broken walls, faint whispers), Smell (Dust, old stone, regret).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** A player gains a Blight Corruption point.
    *   **THEN:** Generate a short, disturbing vision related to the crown's history. The player may gain a piece of information, but also suffers a minor penalty (e.g., disadvantage on the next Wisdom save).
    *   **IF:** The players choose to ally with Elara Voss and the bandits.
    *   **THEN:** They gain access to the bandits' network and resources, but their reputation with Lord Hale's faction plummets, leading to open hostility.
    *   **IF:** The players discover Thrain Blackthorn's role in spreading the blight.
    *   **THEN:** They can choose to expose him, shattering the morale of the Fading Priesthood, or use the information to blackmail him into helping them destroy the crown.
    *   **IF:** A player decides to wear the Withered Crown before the final confrontation.
    *   **THEN:** They gain immense power but must make a high-DC Wisdom saving throw each day. On a failure, the crown's consciousness takes over, turning the player into a temporary antagonist with their own dark goals.
    *   **IF:** The players successfully destroy the crown.
    *   **THEN:** The blight is not cleansed, but its spread is halted. The land is now free to heal naturally, but this will take generations. Generate an epilogue where the factions must now work together to rebuild the kingdom from scratch, a new and difficult challenge.
