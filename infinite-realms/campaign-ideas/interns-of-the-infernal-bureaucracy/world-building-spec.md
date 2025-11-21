### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**Interns of the Infernal Bureaucracy**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The players are ambitious mortals who have signed a binding contract to become unpaid interns for the Department of Soul Acquisitions in the Nine Hells. Under a tyrannical devil manager, they must complete absurd and dangerous tasks, navigate infernal office politics, and survive the mind-numbing inanity of corporate life in hell, all in the hopes of earning a promotion to a low-level, paid position.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the corporate structure of the Department of Soul Acquisitions and its place in the hierarchy of the Nine Hells.
    *   Write the history of the "Internship Program" as a method for acquiring mortal talent.
    *   Describe the legend of the one intern who actually got promoted and what they had to do to achieve it.
    *   Explain the magical and legal mechanics of an infernal employment contract.
    *   Detail the story of Ol' Man Hemlock, the farmer who has successfully contested his damnation for 70 years on legal technicalities.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **Barzibub's Team (The Players)** (Minor)
        *   **Goals:** To get promoted to a paid position and survive the internship.
        *   **Hierarchy:** A flat structure of interns under the direct supervision of Barzibub.
        *   **Public Agenda:** To be the most efficient and productive intern team in the department.
        *   **Secret Agenda:** To expose Barzibub's incompetence and take his job.
        *   **Assets:** Their mortal ingenuity, a binding contract (which offers some protection), and a shared sense of desperation.
        *   **Relationships:** In direct competition with Sleezle and Gretch; cautiously allied with Brenda from Accounting.
    *   **The Rival Interns** (Minor)
        *   **Goals:** To get promoted by any means necessary, preferably by sabotaging the players.
        *   **Hierarchy:** A duo of imps, Sleezle and Gretch.
        *   **Public Agenda:** To show unwavering loyalty and dedication to Barzibub.
        *   **Secret Agenda:** To report Barzibub's embezzlement to his superiors and take his position.
        *   **Assets:** Innate knowledge of infernal politics, a network of impish spies, a lack of morals.
        *   **Relationships:** Hostile and treacherous towards the players.
    *   **Accounting Department** (Major)
        *   **Goals:** To audit and account for every single soul-shard in the Nine Hells.
        *   **Hierarchy:** A complex bureaucracy of its own, filled with surprisingly neutral and even pleasant monstrosities like Brenda the Gorgon.
        *   **Public Agenda:** To ensure fiscal responsibility and adherence to infernal financial regulations.
        *   **Secret Agenda:** They are the true power behind the throne, as they can freeze assets and launch devastating audits against any devil.
        *   **Assets:** Control over the flow of soul-shards, access to all financial records, an army of auditors.
        *   **Relationships:** Feared by all other departments.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Barzibub, Middle Manager of the Damned:** A stressed-out, coffee-addicted Chain Devil micro-manager who is terrified of his own boss.
    *   **Sleezle and Gretch:** A rival duo of conniving imps who are secretly a single hive-mind entity.
    *   **Brenda from Accounting:** A surprisingly cheerful and helpful Gorgon who is a source of office gossip and is not actually an employee.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Overworked Demon Cubicle-Worker"
    *   "Sycophantic Imp Lackey"
    *   "Gossip-loving Fiend from another Department"
    *   "Terrified Damned Soul (working in IT)"
    *   "Adorable but Troublesome Celestial Puppy (Creature)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Cubicle Farm of Despair:** An endless, grey landscape of cubicles where the party has their desks.
        *   **Key Landmarks:** The players' cubicle, Barzibub's slightly larger cubicle, the perpetually jammed printer, the water cooler that dispenses lukewarm, brackish water.
        *   **Primary Inhabitants:** Interns, low-level devils, damned souls working off their sentences.
        *   **Available Goods & Services:** Soul-shard-based vending machines (usually broken), access to infernal forms and paperwork.
        *   **Potential Random Encounters (x5):** A mandatory team-building exercise is announced, the printer jams yet again, a rival intern steals your stapler, Barzibub calls an impromptu meeting, a damned soul offers you a tip in exchange for a moment of peace.
        *   **Embedded Plot Hooks & Rumors (x3):** "Barzibub seems to be hiding something in his desk drawer." "Brenda in Accounting knows all the department's secrets." "The imps are planning to sabotage the morale event."
        *   **Sensory Details:** Sight (Endless grey, flickering fluorescent lights, piles of paperwork), Sound (The drone of computers, distant screaming, the click-clack of keyboards), Smell (Stale coffee, brimstone, quiet desperation).
    *   **The Great Archives:** A labyrinthine library of damned souls' contracts, where the paperwork is as dangerous as any monster.
        *   **Key landmarks:** The Section of Unreadable Fine Print, the Shelf of Contested Damnation, the Index of Lost Souls, the Paper Golem.
        *   **Primary Inhabitants:** Spectral librarians, paper elementals, dust bunnies the size of dogs.
        *   **Available Goods & Services:** Access to legal precedents and soul contracts (if you can find them).
        *   **Potential Random Encounters (x5):** A paper cut that requires a saving throw against soul-drain, a spectral librarian demands silence with terrifying force, a rival team is searching for the same document, a section of the archive shifts, trapping the party, a book bites a player.
        *   **Embedded Plot Hooks & Rumors (x3):** "Ol' Man Hemlock's original contract is here, and it has a loophole." "The Arch-Duke's contract is rumored to be stored in a secret vault." "Some of the contracts are sentient."
        *   **Sensory Details:** Sight (Towering shelves, floating books, swirling dust motes), Sound (Utter silence, the rustle of paper, ghostly whispers), Smell (Old paper, dust, ink).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players successfully file a piece of Infernal Paperwork.
    *   **THEN:** They gain KPIs and their request is processed. Generate the outcome of the request (e.g., a minor demon is summoned as requested).
    *   **IF:** The players fail to file a piece of Infernal Paperwork correctly.
    *   **THEN:** Generate a comedic, bureaucratic consequence. The request is denied, sent to the wrong department, or the wrong thing is summoned (e.g., a flock of celestial parakeets instead of a demon).
    *   **IF:** The players successfully organize the Scream-Fest morale event.
    *   **THEN:** Their KPIs skyrocket. The visiting Arch-Devil is impressed, putting them on the fast-track for promotion but also making them a bigger target for their rivals.
    *   **IF:** The players are caught harming one of the celestial puppies.
    *   **THEN:** They are in breach of their contract. Generate a legal-themed encounter where they must defend their actions to a celestial lawyer or face immediate termination (of their existence).
    *   **IF:** The players successfully expose Barzibub's embezzlement during their final performance review.
    *   **THEN:** The Arch-Duke is impressed by their ruthlessness. Barzibub is demoted to a soul-larva. Generate two final outcomes: 1) The players are promoted to Barzibub's now-vacant position, becoming the new mid-level managers. 2) The Arch-Duke promotes Sleezle and Gretch instead, creating a new set of rivals for the sequel.
