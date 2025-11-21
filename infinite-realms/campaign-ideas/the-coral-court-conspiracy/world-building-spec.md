### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Coral Court Conspiracy**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** In the bioluminescent underwater city of Aquatica, a fragile peace between the Merfolk, the Kuo-Toa, and an Abolethic cult is shattered when a Merfolk elder is murdered. The players, as envoys or guards, are tasked with finding the killer. They must navigate treacherous court politics and ancient grudges to prevent a civil war, all while under the subtle, oppressive influence of the deep sea.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the founding of Aquatica and the formation of the Coral Council.
    *   Write the history of the first conflict between the Merfolk and the Kuo-Toa.
    *   Describe the nature of the Abolethic cult and their relationship with the Veiled Oracle.
    *   Explain the cultural significance of the bioluminescent gardens and the Coral Council chambers.
    *   Detail the legend of the Abyss Gate and the horrors it is said to hold back.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Merfolk Aristocracy** (Major)
        *   **Goals:** To maintain their political and cultural dominance in Aquatica.
        *   **Hierarchy:** A council of elders, with influential diplomats like Ambassador Coralyn.
        *   **Public Agenda:** To uphold peace, tradition, and the rule of law.
        *   **Secret Agenda:** To curb the growing influence of the Kuo-Toa and maintain the status quo that benefits them.
        *   **Assets:** Political control of the Coral Council, a highly-trained royal guard, ancient water-shaping magic.
        *   **Relationships:** Suspicious of the Kuo-Toa; view the Abolethic cult as a distasteful but necessary part of the city's balance.
    *   **The Kuo-Toa Workers' Union** (Major)
        *   **Goals:** To gain more rights, respect, and political power for the Kuo-Toa.
        *   **Hierarchy:** Led by a council of clan chiefs and speakers, such as Chief Speaker Grok.
        *   **Public Agenda:** To seek justice for their people and demand fair treatment.
        *   **Secret Agenda:** To secure control of key industrial and trade sectors, even if it means making deals with surface-dwellers.
        *   **Assets:** Control of the city's industry and infrastructure, a large and hardy population, practical engineering skills.
        *   **Relationships:** Resentful of the Merfolk's dominance; easily manipulated by the Abolethic cult.
    *   **The Abolethic Cult** (Major)
        *   **Goals:** To sow discord and slowly gain control over the city's leaders through psychic manipulation.
        *   **Hierarchy:** A secretive cult with the Veiled Oracle as its spiritual center.
        *   **Public Agenda:** To offer wisdom and guidance through the Oracle's prophecies.
        *   **Secret Agenda:** To weaken the other two factions until the city is ripe for an Abolethic takeover.
        *   **Assets:** Powerful psychic magic, a network of mind-controlled agents (thralls), ancient and forbidden knowledge.
        *   **Relationships:** The secret antagonists, manipulating all sides of the conflict.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Ambassador Coralyn:** A graceful and diplomatic Merfolk leader, torn between her duty and a secret love.
    *   **Chief Speaker Grok:** A gruff, pragmatic, and protective Kuo-Toa leader.
    *   **The Veiled Oracle:** An ancient, enigmatic, and manipulative Aboleth who speaks in riddles.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Arrogant Merfolk Noble"
    *   "Hard-working Kuo-Toa Engineer"
    *   "Secretive Abolethic Cultist"
    *   "Giant Shark (Creature)"
    *   "Mind-Controlled Thrall (Creature)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Coral Council Chambers:** A grand hall carved from living coral, where the fate of Aquatica is decided.
        *   **Key Landmarks:** The Throne of Tides, the Speaker's Podium, the glowing pearl of testimony, the balcony overlooking the city.
        *   **Primary Inhabitants:** Merfolk elders, Kuo-Toa representatives, Abolethic observers, guards.
        *   **Available Goods & Services:** Justice, political debate, formal declarations.
        *   **Potential Random Encounters (x5):** A heated argument breaks out between factions, a key witness is intimidated into silence, the Veiled Oracle delivers a cryptic prophecy, a player is challenged to a formal duel of honor, evidence is presented that changes the course of the investigation.
        *   **Embedded Plot Hooks & Rumors (x3):** "The murder weapon was crafted from a rare black coral found only near the Abyss Gate." "Ambassador Coralyn has been seen meeting secretly with a Kuo-Toa." "The Abolethic cult has a secret entrance to the chambers."
        *   **Sensory Details:** Sight (Shimmering bioluminescent light, intricate coral architecture, flowing robes), Sound (Muffled, echoing voices; the gentle hum of the city; the bubbling of water), Smell (Salt, coral, a faint ozone scent).
    *   **The Sunken Market:** A bustling marketplace where goods from across the ocean floor are traded.
        *   **Key Landmarks:** The giant clam-shell stalls, the kraken-ink tattoo parlor, the shark-tooth weaponsmith, the information broker's grotto.
        *   **Primary Inhabitants:** Traders of all aquatic races, smugglers, city guards on patrol, giant crab merchants.
        *   **Available Goods & Services:** Exotic sea-creature mounts, crafted goods, food, rumors.
        *   **Potential Random Encounters (x5):** A pickpocket tries to steal from the party, a rare creature escapes from a vendor, a fight breaks out between a Merfolk and a Kuo-Toa, a city guard patrol demands a "tax," an Abolethic cultist tries to subtly influence a player's mind.
        *   **Embedded Plot Hooks & Rumors (x3):** "There's a black market for items recovered from the Abyss Gate." "The Kuo-Toa assassin was seen buying a specific poison here." "The Oracle's attendants buy a rare type of seaweed here every week."
        *   **Sensory Details:** Sight (A chaotic mix of glowing stalls, strange aquatic goods, diverse species), Sound (The cacophony of haggling, the clicks and whistles of different languages), Smell (Brine, fish, strange spices).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** A player fails a Wisdom saving throw against "Pressure Sickness" in a high-stress or psychically charged area.
    *   **THEN:** Generate a short, unsettling hallucination for that player, which may contain a cryptic clue or a red herring.
    *   **IF:** The players present evidence that exonerates the Kuo-Toa assassin.
    *   **THEN:** Tensions with the Kuo-Toa faction ease, and Chief Speaker Grok becomes a potential ally, offering them access to the industrial district. However, the Merfolk nobility becomes more suspicious of the players.
    *   **IF:** The players discover Ambassador Coralyn's secret love affair.
    *   **THEN:** They can use this information to blackmail her for political favors, or they can choose to protect her secret, earning her unwavering (but secret) loyalty.
    *   **IF:** The players openly accuse the Abolethic cult of manipulation without concrete proof.
    *   **THEN:** The cult uses its influence to brand the players as dangerous heretics. The city guard becomes hostile, and the players are barred from the Coral Council chambers.
    *   **IF:** In the finale, the players fail to prevent the civil war from breaking out.
    *   **THEN:** The campaign shifts. Generate a new set of objectives focused on surviving the war, protecting key neighborhoods, and trying to expose the Abolethic cult amidst the chaos of open battle between the Merfolk and Kuo-Toa.
