### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Silverhand Heist: The Vault of Eternity**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The players are recruited by a mysterious employer for the ultimate heist: stealing the legendary "Eternity Stone" from the most secure vault in the kingdom, protected by ancient magic, elite guards, and infallible mechanical defenses. As they assemble their crew of specialists and plan the intricate operation, they discover that multiple criminal organizations are after the same prize, each with their own agenda. The heist becomes a web of betrayals, double-crosses, and moral compromises as the players must decide whether to stick to the plan, go for a bigger score, or walk away from the criminal life entirely. But as the stakes rise and alliances shift, they realize the Eternity Stone may be more dangerous than any of them imagined.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the founding of the Eternity Vault and its history as the kingdom's most secure repository for dangerous magical artifacts.
    *   Write the history of the Eternity Stone itself - its discovery, powers, and the conflicts it has caused throughout history.
    *   Describe the development of vault security systems and how they have evolved to counter increasingly sophisticated criminal enterprises.
    *   Explain the structure of the criminal underworld and the various organizations that operate within it.
    *   Detail the various famous heists that have targeted the Eternity Vault and their outcomes.
    *   Write about the "Silverhand Guild" - the legendary thieves' organization that lends its name to the campaign.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Vault Security** (Major)
        *   **Goals:** To protect the Eternity Vault and its contents from all threats, maintaining the kingdom's magical security.
        *   **Hierarchy:** Military structure led by Marcus "The Vault" Kane and elite security specialists.
        *   **Public Agenda:** We safeguard dangerous magical artifacts for the good of the kingdom.
        *   **Secret Agenda:** To study the Eternity Stone's power for potential weaponization.
        *   **Assets:** Advanced security systems, elite guards, magical wards.
        *   **Relationships:** Antagonistic toward all criminal organizations; cooperative with legitimate authorities.
    *   **The Shadow Syndicate** (Major)
        *   **Goals:** To acquire the Eternity Stone and use its power to dominate the criminal underworld.
        *   **Hierarchy:** Criminal council led by the most successful and ruthless crime lords.
        *   **Public Agenda:** We provide opportunities for those willing to take risks.
        *   **Secret Agenda:** To establish a criminal empire that can challenge legitimate power structures.
        *   **Assets:** Network of criminal operatives, black market connections, insider information.
        *   **Relationships:** Competitive with other criminal factions; willing to form temporary alliances for major scores.
    *   **The Independent Operators** (Minor)
        *   **Goals:** To profit from the heist while maintaining independence from larger criminal organizations.
        *   **Hierarchy:** Loose association of freelance criminals and specialists.
        *   **Public Agenda:** We work for the highest bidder and keep our own counsel.
        *   **Secret Agenda:** To acquire enough wealth to retire from the criminal life.
        *   **Assets:** Specialized skills, flexibility, lack of organizational baggage.
        *   **Relationships:** Neutral toward most factions; willing to work with anyone who pays well.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **The Shadow Broker:** The mysterious employer with hidden motives and political connections.
    *   **Lira "Ghost" Voss:** The master infiltrator with a code of honor and personal history.
    *   **Marcus "The Vault" Kane:** The security expert who knows more than he reveals about the Eternity Stone.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Corrupt Guard"
    *   "Rival Thief"
    *   "Black Market Dealer"
    *   "Security Specialist"
    *   "Double Agent"
    *   "Wealthy Collector"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Eternity Vault:** The most secure repository in the kingdom.
        *   **Key Landmarks:** The Main Vault Chamber, the Security Control Room, the Artifact Display Hall, the Emergency Exit System.
        *   **Primary Inhabitants:** Security personnel, maintenance staff, the occasional authorized researcher.
        *   **Available Goods & Services:** High-level security clearance, emergency equipment, restricted information.
        *   **Potential Random Encounters (x5):** A security patrol passes by, a magical ward activates unexpectedly, discovery of a maintenance access point, a security camera feed reveals something important, a guard suspects the players' cover.
        *   **Embedded Plot Hooks & Rumors (x3):** "The vault contains artifacts that can bend reality itself." "Some guards have been bribed by criminal organizations." "The Eternity Stone calls to those with criminal intentions."
        *   **Sensory Details:** Sight (Gleaming metal surfaces, glowing magical displays), Sound (Humming security systems, echoing footsteps), Smell (Ozone from magical wards, polished metal).
    *   **The Thieves' Quarter:** A shadowy district where criminal organizations operate.
        *   **Key Landmarks:** The Black Cat Tavern, the Fence's Warehouse, the Safe House Network, the Underground Market.
        *   **Primary Inhabitants:** Criminals of all types, information brokers, black market dealers, undercover agents.
        *   **Available Goods & Services:** Stolen goods, criminal services, insider information.
        *   **Potential Random Encounters (x5):** A rival crew tries to recruit the players, a dealer offers a "too good to be true" deal, discovery of a police raid in progress, a contact provides crucial information, a pickpocket attempts to steal from the players.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Thieves' Quarter has tunnels that lead everywhere in the city." "Some criminals have gone straight and now work as consultants." "The quarter knows about every heist before it happens."
        *   **Sensory Details:** Sight (Shadowy figures, flickering neon signs), Sound (Muffled conversations, distant alarms), Smell (Cheap alcohol, cigarette smoke).
    *   **The Noble District:** The wealthy area for reconnaissance and cover.
        *   **Key Landmarks:** The Grand Ballroom, the High Society Club, the Art Gallery, the Private Estates.
        *   **Primary Inhabitants:** Wealthy nobles, socialites, private security, ambitious social climbers.
        *   **Available Goods & Services:** Social connections, investment opportunities, high-society gossip.
        *   **Potential Random Encounters (x5):** A socialite recognizes a player from their wanted poster, a noble offers a suspicious investment, discovery of a secret meeting, a security guard becomes suspicious, a social event provides perfect cover.
        *   **Embedded Plot Hooks & Rumors (x3):** "The nobility secretly fund criminal enterprises." "Some nobles collect dangerous magical artifacts." "The district has more secrets than the criminal underworld."
        *   **Sensory Details:** Sight (Elegant architecture, expensive jewelry), Sound (Polite laughter, classical music), Smell (Expensive perfumes, fresh flowers).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players successfully recruit a key specialist for their crew.
    *   **THEN:** They gain access to unique abilities and information. Generate scenarios where the specialist's reputation attracts unwanted attention.
    *   **IF:** The players form an alliance with a rival criminal organization.
    *   **THEN:** They gain additional resources but create enemies elsewhere. Generate opportunities for betrayal and double-crosses.
    *   **IF:** The players acquire insider information about vault security.
    *   **THEN:** Their heist planning becomes more effective. Generate increased security measures as the vault responds to the information leak.
    *   **IF:** The players maintain a low profile throughout the planning phase.
    *   **THEN:** They avoid detection but miss opportunities for better information. Generate a scenario where their caution causes them to miss a crucial deadline.
    *   **IF:** The players betray their employer or crew members.
    *   **THEN:** They gain short-term advantages but create long-term enemies. Generate scenarios where betrayal comes back to haunt them.
