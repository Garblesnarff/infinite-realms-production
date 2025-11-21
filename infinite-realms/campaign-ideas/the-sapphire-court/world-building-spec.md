### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Sapphire Court: Masks of Power**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The players are inducted into the secretive world of the Sapphire Court, a glittering nexus of noble houses where power is measured in whispered alliances and calculated betrayals. As agents for various noble houses, they navigate the treacherous waters of court politics, attending lavish balls, deciphering cryptic messages, and forging (or breaking) political marriages. But beneath the veneer of civility and elegance, a conspiracy threatens to topple the crown itself. The players must master the art of intrigue, choose their allegiances wisely, and decide whether to expose the conspiracy or use it to reshape the kingdom according to their own vision of power.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the founding of the Sapphire Court and its evolution from a royal advisory body to the center of noble power.
    *   Write the history of the great noble houses and their complex web of alliances, rivalries, and blood feuds.
    *   Describe the development of court protocol and the unwritten rules that govern noble behavior and political maneuvering.
    *   Explain the role of marriage in court politics and the various types of political unions throughout history.
    *   Detail the various scandals and conspiracies that have rocked the court over the centuries.
    *   Write about the "Court of Whispers" - the informal information network that operates parallel to official court structures.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Royal Household** (Major)
        *   **Goals:** To maintain the crown's authority while balancing the interests of competing noble houses.
        *   **Hierarchy:** Royal family and their most trusted advisors and functionaries.
        *   **Public Agenda:** We represent the kingdom's unity and the crown's benevolent authority.
        *   **Secret Agenda:** To identify and eliminate threats to royal authority, including the conspiracy.
        *   **Assets:** Royal guards, intelligence network, treasury resources.
        *   **Relationships:** Cautious toward all noble houses; dependent on their support for governance.
    *   **The Progressive Circle** (Major)
        *   **Goals:** To modernize the court and implement social reforms while maintaining noble privilege.
        *   **Hierarchy:** Coalition of reform-minded nobles from various houses.
        *   **Public Agenda:** The court must evolve to meet the challenges of the modern age.
        *   **Secret Agenda:** To redistribute power from traditional houses to rising families.
        *   **Assets:** Intellectual resources, connections to merchant classes, reformist literature.
        *   **Relationships:** Allied with houses seeking change; opposed by traditional conservative factions.
    *   **The Traditionalist Order** (Major)
        *   **Goals:** To preserve the court's ancient traditions and maintain the established hierarchy of noble houses.
        *   **Hierarchy:** Ancient noble houses with long pedigrees and conservative values.
        *   **Public Agenda:** Tradition and stability are the foundations of good governance.
        *   **Secret Agenda:** To prevent social mobility and maintain control of land and titles.
        *   **Assets:** Historical legitimacy, rural land holdings, military traditions.
        *   **Relationships:** Supportive of established houses; hostile toward reformist elements.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Duchess Elara Voss:** The ambitious hostess who leads the conspiracy from her position of social influence.
    *   **Lord Marcus Kane:** The honorable traditionalist whose house faces financial ruin.
    *   **Lady Lirael Crowe:** The foreign ambassador with mysterious goals and hidden agendas.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Ambitious Courtier"
    *   "Scheming Advisor"
    *   "Foreign Diplomat"
    *   "Royal Functionary"
    *   "Social Climber"
    *   "Disgraced Noble"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Sapphire Palace:** The glittering heart of the court.
        *   **Key Landmarks:** The Grand Ballroom, the Throne Room, the Royal Gardens, the Private Quarters.
        *   **Primary Inhabitants:** Royal family, courtiers, diplomats, servants, guards.
        *   **Available Goods & Services:** Political influence, social connections, royal favor.
        *   **Potential Random Encounters (x5):** A courtier seeks a private conversation, a servant delivers a mysterious message, discovery of a secret passage, a diplomatic incident occurs, a social event provides networking opportunities.
        *   **Embedded Plot Hooks & Rumors (x3):** "The palace has more secret passages than official rooms." "Some courtiers are secretly married to foreign agents." "The throne room contains mechanisms that test the worthiness of claimants."
        *   **Sensory Details:** Sight (Crystal chandeliers, polished marble), Sound (Polite conversations, distant music), Smell (Fresh flowers, expensive perfumes).
    *   **The Noble Houses:** The various estates and mansions.
        *   **Key Landmarks:** The Great Hall, the Private Library, the Servant's Quarters, the Garden Pavilions.
        *   **Primary Inhabitants:** Noble families, household staff, political advisors, guests.
        *   **Available Goods & Services:** Political alliances, financial support, insider information.
        *   **Potential Random Encounters (x5):** A family member seeks advice, a servant reveals a secret, discovery of hidden correspondence, a political rival pays a visit, a social call reveals tensions.
        *   **Embedded Plot Hooks & Rumors (x3):** "Every noble house has at least one secret passage to the palace." "Some houses maintain private intelligence networks." "The houses keep records of every political deal ever made."
        *   **Sensory Details:** Sight (Family portraits, antique furniture), Sound (Echoing halls, distant conversations), Smell (Aged wood, family scents).
    *   **The Royal Gardens:** A beautiful but politically charged space.
        *   **Key Landmarks:** The Central Fountain, the Hedge Maze, the Pavilion Alcoves, the Rose Garden.
        *   **Primary Inhabitants:** Courting couples, political operatives, gardeners, secret agents.
        *   **Available Goods & Services:** Private meeting spaces, romantic settings, hidden conversations.
        *   **Potential Random Encounters (x5):** A couple's conversation reveals political secrets, a hidden listener is discovered, discovery of a secret garden meeting, a gardener provides unexpected information, a romantic encounter becomes politically charged.
        *   **Embedded Plot Hooks & Rumors (x3):** "The gardens have been the site of more political deals than the palace." "Some paths in the maze lead to secret exits." "The fountains whisper secrets to those who listen."
        *   **Sensory Details:** Sight (Blooming flowers, winding paths), Sound (Fountain water, rustling leaves), Smell (Fresh blooms, morning dew).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players successfully arrange a politically advantageous marriage.
    *   **THEN:** Their house's influence grows, creating new opportunities. Generate scenarios where the marriage creates unexpected complications.
    *   **IF:** The players form a secret alliance with a rival house.
    *   **THEN:** They gain access to new information and resources. Generate scenarios where the alliance is tested by conflicting interests.
    *   **IF:** The players expose a courtier's secret publicly.
    *   **THEN:** Their reputation for discretion suffers but they gain grateful allies. Generate scenarios where the exposed courtier seeks revenge.
    *   **IF:** The players maintain excellent social standing throughout the campaign.
    *   **THEN:** They gain access to exclusive events and information. Generate opportunities for high-society intrigue and scandal.
    *   **IF:** The players choose to support the conspiracy.
    *   **THEN:** They gain significant power but risk everything if discovered. Generate scenarios where the conspiracy's plans conflict with their personal goals.
