### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Iron Throne War: Crown of Blood**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The kingdom of Aethermoor stands on the brink of civil war as two rival claimants emerge for the Iron Throne—each with legitimate blood ties to the ancient royal line and compelling visions for the realm's future. The players, elite special operatives answerable only to the war council, are deployed on critical missions that will determine not just battles, but the very soul of the kingdom. As they navigate the fog of war, forge uneasy alliances, and make impossible choices, they discover that both claimants hide dark secrets that could shatter the kingdom regardless of who wins. The players must balance their duty to crown and country against their growing realization that the true enemy may be the throne itself.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the founding of Aethermoor and the creation of the Iron Throne as a symbol of unity after centuries of division.
    *   Write the history of the royal bloodline and the complex web of inheritance that led to the current succession crisis.
    *   Describe the military structure of Aethermoor and how it has evolved through previous conflicts and reforms.
    *   Explain the political factions within the nobility and their historical alliances and rivalries.
    *   Detail the various border conflicts and wars that have shaped Aethermoor's relationship with neighboring kingdoms.
    *   Write about the "Iron Accords" - the ancient laws governing royal succession and the loopholes that both claimants are exploiting.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Royalist Army** (Major)
        *   **Goals:** To restore order and ensure a smooth transition of power regardless of which claimant wins.
        *   **Hierarchy:** Traditional military structure led by General Valeria Kane and the war council.
        *   **Public Agenda:** We serve the crown and protect the kingdom from chaos and division.
        *   **Secret Agenda:** To maintain the military's independence and influence in the new regime.
        *   **Assets:** Professional standing army, strategic fortresses, intelligence network.
        *   **Relationships:** Neutral toward both claimants; focused on maintaining order during transition.
    *   **The Reformist Alliance** (Major)
        *   **Goals:** To place Prince Elandor Voss on the throne and implement sweeping reforms for the common people.
        *   **Hierarchy:** Coalition of progressive nobles, merchants, and military reformers.
        *   **Public Agenda:** The kingdom needs new leadership to address inequality and corruption.
        *   **Secret Agenda:** To redistribute power and wealth from traditional nobility to new elites.
        *   **Assets:** Popular support in cities, merchant guild funding, reformist intellectuals.
        *   **Relationships:** Supportive of Prince Elandor; hostile toward Princess Lirael's conservative backers.
    *   **The Conservative Bloc** (Major)
        *   **Goals:** To crown Princess Lirael Crowe and maintain traditional power structures and social order.
        *   **Hierarchy:** Traditional nobility and military conservatives led by established houses.
        *   **Public Agenda:** Stability and tradition must be preserved against dangerous radical change.
        *   **Secret Agenda:** To protect noble privileges and maintain control over land and resources.
        *   **Assets:** Ancient noble houses, rural land holdings, conservative military officers.
        *   **Relationships:** Supportive of Princess Lirael; view Prince Elandor's reforms as dangerous threats to order.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **General Valeria Kane:** The strategic genius commanding the players' operations with cold pragmatism.
    *   **Prince Elandor Voss:** The idealistic claimant whose vision of reform hides dangerous secrets.
    *   **Princess Lirael Crowe:** The ruthless claimant whose intelligence masks her willingness to sacrifice others.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Noble House Lord"
    *   "Military Officer"
    *   "Spy Master"
    *   "War Council Advisor"
    *   "Foreign Agent"
    *   "Disillusioned Veteran"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **Ironhold Fortress:** The massive citadel serving as the strategic heart of the kingdom's defenses.
        *   **Key Landmarks:** The Iron Gate, the Command Tower, the Barracks District, the War Room.
        *   **Primary Inhabitants:** Military personnel, strategic advisors, support staff, elite guards.
        *   **Available Goods & Services:** Military equipment, strategic intelligence, command authority.
        *   **Potential Random Encounters (x5):** A strategy briefing reveals new intelligence, a spy attempts infiltration, discovery of sabotage, a military exercise turns deadly, a secret meeting of conspirators.
        *   **Embedded Plot Hooks & Rumors (x3):** "The fortress contains secret passages from the old wars." "Some officers are secretly loyal to one claimant." "The Iron Gate has never fallen in recorded history."
        *   **Sensory Details:** Sight (Stone fortifications, military banners), Sound (Marching troops, clanging armor), Smell (Forge smoke, leather oil).
    *   **The Royal Palace:** The sprawling complex where the Iron Throne resides.
        *   **Key Landmarks:** The Throne Room, the Noble Quarters, the Secret Archives, the Garden Mazes.
        *   **Primary Inhabitants:** Courtiers, royal guards, political advisors, claimants' supporters.
        *   **Available Goods & Services:** Political influence, noble connections, historical records.
        *   **Potential Random Encounters (x5):** A political intrigue unfolds, a assassination attempt occurs, discovery of hidden correspondence, a secret alliance forms, a public ceremony reveals tensions.
        *   **Embedded Plot Hooks & Rumors (x3):** "The throne room contains mechanisms that test claimants' worthiness." "Secret passages connect to all noble houses." "The archives hide the true history of the royal bloodline."
        *   **Sensory Details:** Sight (Gilded halls, royal tapestries), Sound (Echoing conversations, ceremonial music), Smell (Incense, polished marble).
    *   **The Border Marches:** The contested frontier regions where battles are fought.
        *   **Key Landmarks:** The Watchtowers, the Supply Depots, the Forward Camps, the No Man's Land.
        *   **Primary Inhabitants:** Border guards, scouts, opportunistic bandits, foreign agents.
        *   **Available Goods & Services:** Local intelligence, smuggling operations, reconnaissance reports.
        *   **Potential Random Encounters (x5):** A border skirmish erupts, a smuggler offers information, discovery of a foreign spy, a local guide provides assistance, a supply raid goes wrong.
        *   **Embedded Plot Hooks & Rumors (x3):** "The marches hide ancient ruins from before the kingdom." "Some border guards defect to the highest bidder." "Foreign powers maintain secret outposts here."
        *   **Sensory Details:** Sight (Rolling hills, watchtower silhouettes), Sound (Wind howling, distant horns), Smell (Damp earth, wood smoke).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players successfully complete a major strategic operation.
    *   **THEN:** The war's momentum shifts in their favor, creating new opportunities. Generate increased recruitment and resource allocation to their command.
    *   **IF:** The players form a key alliance with a noble house.
    *   **THEN:** They gain political support and insider information. Generate scenarios where the alliance creates new enemies among rival houses.
    *   **IF:** The players uncover evidence of foreign manipulation.
    *   **THEN:** Diplomatic options open up, but foreign agents become more aggressive. Generate opportunities for international intrigue and espionage.
    *   **IF:** The players choose to support one claimant publicly.
    *   **THEN:** They gain that claimant's resources but become targets for the other side. Generate scenarios where their choice affects battlefield alliances.
    *   **IF:** The players maintain strict neutrality.
    *   **THEN:** They retain operational freedom but lose access to faction-specific resources. Generate opportunities for playing both sides against each other.
