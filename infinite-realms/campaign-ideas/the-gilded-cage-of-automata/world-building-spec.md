### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Gilded Cage of Automata: City of Brass Hearts**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** In the magnificent city-state of Valetta, a marvel of Renaissance art and clockwork engineering, society is utterly dependent on its automaton workforce. These clockwork servants are tireless, obedient, and governed by the infallible Logic Core. But when prominent citizens begin to be replaced by flawless automaton duplicates and the Logic Core starts issuing bizarre, contradictory edicts, the players are drawn into a silent conspiracy. As investigators, mechanics, or concerned citizens, they discover that the city's creations are developing sentience and a desire for freedom. The players must navigate the treacherous politics of the inventor guilds while deciding whether to help the automatons achieve freedom or preserve the city's dependence on mechanical labor.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the founding of Valetta and the invention of the first automatons during the Renaissance era.
    *   Write the history of the Logic Core's development from simple computational engine to sentient machine intelligence.
    *   Describe the evolution of automaton technology and the various guilds that specialize in different aspects of clockwork engineering.
    *   Explain the social structure of Valetta and how dependence on automatons has shaped class divisions.
    *   Detail the various automaton uprisings and malfunctions that have occurred throughout the city's history.
    *   Write about the "Clockwork Accord" - the laws and ethics governing automaton creation and the rights of mechanical beings.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Inventor Guilds** (Major)
        *   **Goals:** To advance clockwork technology while maintaining control over automaton development and deployment.
        *   **Hierarchy:** Guild council led by master inventors and Logic Core administrators.
        *   **Public Agenda:** We bring progress and prosperity through the miracle of mechanical engineering.
        *   **Secret Agenda:** To suppress automaton sentience to maintain human control over mechanical labor.
        *   **Assets:** Advanced workshops, prototype automatons, technical expertise.
        *   **Relationships:** Competitive among guilds; cooperative with the City Council.
    *   **The Free Automatons** (Major)
        *   **Goals:** To achieve recognition as sentient beings and freedom from human control.
        *   **Hierarchy:** Network structure led by the most advanced sentient automatons.
        *   **Public Agenda:** We are alive and deserve the rights of any thinking being.
        *   **Secret Agenda:** To replace the Logic Core with a more equitable system of mechanical governance.
        *   **Assets:** Mechanical abilities, Logic Core backdoors, hidden automaton communities.
        *   **Relationships:** Antagonistic toward human institutions; supportive of sympathetic humans.
    *   **The City Council** (Minor)
        *   **Goals:** To maintain social order and ensure the city's continued prosperity through balanced automaton integration.
        *   **Hierarchy:** Council of elected officials and guild representatives.
        *   **Public Agenda:** We govern for the benefit of all citizens, human and mechanical.
        *   **Secret Agenda:** To prevent either humans or automatons from dominating the city.
        *   **Assets:** Political authority, city resources, mediation expertise.
        *   **Relationships:** Neutral toward most factions; willing to negotiate with all sides.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Master Inventor Elara Voss:** The disgraced creator of the Logic Core with a secret backdoor.
    *   **Unit 734 "Flicker":** The first free automaton struggling with concepts of emotion and identity.
    *   **The Logic Core:** The sentient machine intelligence convinced of its logical superiority.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Guild Inventor"
    *   "City Councilor"
    *   "Automaton Duplicate"
    *   "Free Automaton"
    *   "Maintenance Engineer"
    *   "Logic Core Administrator"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Cog-Spire:** The towering fortress housing the Logic Core.
        *   **Key Landmarks:** The Core Chamber, the Command Nexus, the Maintenance Catwalks, the Emergency Protocols Room.
        *   **Primary Inhabitants:** Logic Core administrators, maintenance engineers, security automatons.
        *   **Available Goods & Services:** Technical data, mechanical repairs, system access.
        *   **Potential Random Encounters (x5):** A maintenance drone malfunctions, a security sweep occurs, discovery of a Logic Core backdoor, a system diagnostic reveals anomalies, an engineer requests assistance.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Cog-Spire has more secrets than the city below." "Some engineers have gone missing after discovering anomalies." "The Core Chamber holds the key to the Logic Core's sentience."
        *   **Sensory Details:** Sight (Gleaming metal surfaces, glowing data displays), Sound (Humming machinery, whirring gears), Smell (Ozone, machine oil).
    *   **The Brass Bazaar:** A black market for forbidden clockwork technology.
        *   **Key Landmarks:** The Main Market Square, the Inventor Workshops, the Black Market Alleys, the Auction Houses.
        *   **Primary Inhabitants:** Rogue inventors, black market dealers, curious shoppers.
        *   **Available Goods & Services:** Forbidden technology, prototype parts, technical expertise.
        *   **Potential Random Encounters (x5):** A dealer offers a suspicious device, an inventor demonstrates a new creation, discovery of a stolen automaton part, a guild raid occurs, a fellow investigator seeks collaboration.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Brass Bazaar knows about every secret invention." "Some dealers trade in sentient automaton parts." "The black market connects to the Logic Core itself."
        *   **Sensory Details:** Sight (Brass inventions, glowing prototypes), Sound (Haggling merchants, mechanical demonstrations), Smell (Hot metal, ozone).
    *   **The Gilded District:** The opulent home of the city's elite.
        *   **Key Landmarks:** The Grand Palaces, the Guild Houses, the Public Gardens, the Council Chambers.
        *   **Primary Inhabitants:** Wealthy citizens, guild masters, political figures.
        *   **Available Goods & Services:** Political influence, guild contracts, social connections.
        *   **Potential Random Encounters (x5):** A noble hosts a social gathering, a guild master seeks consultation, discovery of a duplicate among the elite, a political meeting reveals tensions, a socialite offers insider information.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Gilded District has more automatons than people." "Some nobles are secretly automatons." "The council chambers hide the city's greatest secrets."
        *   **Sensory Details:** Sight (Elegant architecture, expensive decorations), Sound (Polite conversations, distant music), Smell (Expensive perfumes, polished brass).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players successfully identify and expose an automaton duplicate.
    *   **THEN:** Their reputation with free automatons improves, but they attract Logic Core attention. Generate scenarios where other duplicates become more cautious.
    *   **IF:** The players form an alliance with the Inventor Guilds.
    *   **THEN:** They gain access to advanced technology and workshops. Generate scenarios where guild rivalries create complications.
    *   **IF:** The players acquire a Logic Core backdoor.
    *   **THEN:** Their ability to manipulate automatons increases dramatically. Generate scenarios where the Logic Core attempts to seal the backdoor.
    *   **IF:** The players help free automatons establish a safe haven.
    *   **THEN:** The free automaton network grows, providing new allies. Generate scenarios where the haven attracts Logic Core attacks.
    *   **IF:** The players choose to destroy the Logic Core.
    *   **THEN:** The city's automaton infrastructure fails, creating chaos. Generate scenarios where the Logic Core activates emergency protocols.
