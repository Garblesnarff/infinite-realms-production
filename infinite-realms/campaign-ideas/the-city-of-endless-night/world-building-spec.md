### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The City of Endless Night**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** In the perpetually dark and rain-slicked metropolis of Gloomhaven, the players are hard-boiled investigators hired to solve a series of ritualistic murders among the city's magical elite. They must navigate a world of femme fatales, corrupt politicians, and ancient curses to find the killer before a secret society's dark ritual plunges the city into a war between its most powerful factions.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of Gloomhaven. Why is it in a state of endless night and perpetual rain?
    *   Write the story of the Order of the Black Sun and their beliefs regarding magical purity.
    *   Describe the nature of the ancient entity the Order seeks to summon.
    *   Explain the relationship between the city's magical elite and the mundane authorities like the city guard.
    *   Detail a famous, unsolved case from Gloomhaven's past that sets the tone for the city's corruption.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Investigators (The Players)** (Minor)
        *   **Goals:** To solve the murders, get paid, and not get killed.
        *   **Hierarchy:** A small, independent agency or a loose-knit group of specialists.
        *   **Public Agenda:** To find the truth.
        *   **Secret Agenda:** Each player may have a personal motivation (redemption, revenge, wealth) that complicates their pursuit of the case.
        *   **Assets:** Their wits, their contacts, and a shared office that smells of stale coffee and rain.
        *   **Relationships:** Adversarial with the City Guard; navigating a web of lies spun by all other factions.
    *   **The Order of the Black Sun** (Major)
        *   **Goals:** To summon a powerful entity to "cleanse" the city of all but the most powerful magic-users.
        *   **Hierarchy:** A secret society led by a council, with influential members like Seraphina in key positions.
        *   **Public Agenda:** To be upstanding members of the magical elite.
        *   **Secret Agenda:** To perform a series of ritualistic murders to power their summoning ritual.
        *   **Assets:** Powerful magic, political influence, a hidden temple in the city's catacombs.
        *   **Relationships:** The primary antagonists, manipulating the city from the shadows.
    *   **The City Guard** (Major)
        *   **Goals:** To maintain a semblance of order and collect their bribes.
        *   **Hierarchy:** A standard police force structure, but rife with corruption. Led by precinct captains like Valerius.
        *   **Public Agenda:** To enforce the law.
        *   **Secret Agenda:** Captain Valerius is being blackmailed by the Order and is actively covering up their involvement in the murders.
        *   **Assets:** The authority of the law, a network of street-level enforcers, the city's holding cells.
        *   **Relationships:** A corrupt and obstructive force that the players must work around.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Seraphina:** The beautiful, ruthless, and deceptive femme fatale who hires the party and is a high-ranking member of the Order.
    *   **Captain Valerius:** The cynical and corrupt captain of the city guard, who is being blackmailed by the Order.
    *   **The Oracle in the Rain:** An enigmatic water elemental information broker who lives in the city's sewer system.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Shady Underworld Informant"
    *   "Arrogant Magical Elite Wizard"
    *   "World-weary Jazz Club Singer"
    *   "Brutal Thug Enforcer"
    *   "Magical Construct Guardian (Creature)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Black Cat Club:** A smoky, underground jazz club that is a popular haunt for the city's magical underworld.
        *   **Key Landmarks:** The stage where a torch singer performs, the bar manned by a goblin, the private back rooms for illicit deals, the secret exit to the sewers.
        *   **Primary Inhabitants:** Off-duty wizards, criminals, informants, femme fatales.
        *   **Available Goods & Services:** Strong drinks, illegal magical components, rumors.
        *   **Potential Random Encounters (x5):** A bar fight breaks out using magic, an informant offers a clue then gets murdered, the party is ambushed by thugs, a corrupt guard is seen taking a bribe, Seraphina is seen meeting with a rival wizard.
        *   **Embedded Plot Hooks & Rumors (x3):** "The singer on stage is the ex-lover of the first victim." "The owner of the club is a retired assassin." "The Order of the Black Sun recruits new members here."
        *   **Sensory Details:** Sight (Dim lighting, thick cigar smoke, neon signs reflecting in puddles), Sound (Smooth jazz, clinking glasses, hushed conversations), Smell (Stale alcohol, cheap perfume, rain).
    *   **The Hidden Temple of the Black Sun:** Located in the ancient catacombs beneath the city.
        *   **Key Landmarks:** The ritual chamber with the summoning circle, the sacrificial altar, the library of forbidden texts, the cells for holding future victims.
        *   **Primary Inhabitants:** Order cultists, magical guardians, undead servants.
        *   **Available Goods & Services:** None. This is the enemy stronghold.
        *   **Potential Random Encounters (x5):** A patrol of cultists, a magical trap is triggered, the party finds evidence implicating a new, powerful figure, the ghost of a past victim appears, the entity being summoned briefly manifests.
        *   **Embedded Plot Hooks & Rumors (x3):** "The counter-ritual requires an item from the first victim." "The entity feeds on magical energy." "Not all members of the Order agree with the plan to summon the entity."
        *   **Sensory Details:** Sight (Flickering candlelight, arcane symbols painted in blood, dark, damp stone), Sound (Distant chanting, dripping water, skittering noises in the dark), Smell (Incense, decay, blood).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players successfully connect two clues on their Clue Board.
    *   **THEN:** A "Moment of Insight" is generated. Reveal a new location to investigate or a new line of questioning that forces an NPC to reveal a secret during their next interrogation.
    *   **IF:** A player chooses to use a "Flashback."
    *   **THEN:** Generate a short, playable scene from that character's past that reveals a new clue or a personal connection to a current NPC, but also gives the DM a new piece of leverage to use against that character.
    *   **IF:** The players present evidence of Captain Valerius's corruption to his superiors.
    *   **THEN:** Valerius is arrested, but the City Guard becomes openly hostile to the party, refusing to cooperate and actively obstructing their investigation.
    *   **IF:** The players confront Seraphina with evidence of her involvement before the final act.
    *   **THEN:** She does not fight them. Instead, she offers them a place in the Order, revealing the "benefits" of her new world order and creating a major moral choice for the party.
    *   **IF:** The players fail to stop the ritual and the entity is summoned.
    *   **THEN:** Do not end the campaign. Instead, generate a new final act where the city is plunged into chaos. The players must now lead a desperate resistance against the entity and the Order in a city that has become a living nightmare.
