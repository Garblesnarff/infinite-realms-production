### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**Objection, Your Infernal Honor!**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise. The tone is a dark comedy and cynical legal drama.
*   **Content:** The players are a new legal team in the infernal metropolis of Dis, where souls are currency and contracts are binding. They take on cases for mortals and minor devils who have been ensnared by the labyrinthine and corrupt legal system. They must outwit devilish prosecutors and navigate a nightmare bureaucracy to save their clients from eternal damnation, all while trying to make a name for themselves.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of the Infernal Bar Association and the structure of the courts in Dis.
    *   Write a summary of the key tenets of infernal law, focusing on contracts, souls, and property rights.
    *   Describe the case of the "Sandwich Pact," a landmark case involving a mortal who accidentally sold their soul for a sandwich.
    *   Explain the economy of Dis, particularly how souls are used as currency and the function of the Soul Market.
    *   Detail the story of a famous, disbarred infernal lawyer and the powerful enemy they made.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Legal Team (The Players)** (Minor)
        *   **Goals:** To win cases, save their clients' souls, and build a reputation.
        *   **Hierarchy:** A new, small law firm.
        *   **Public Agenda:** To provide legal services to the desperate.
        *   **Secret Agenda:** To find and exploit loopholes in infernal law to beat the system at its own game.
        *   **Assets:** Their legal knowledge, their wits, and a shared, desperate ambition.
        *   **Relationships:** Adversaries of the Prosecutor's office; reliant on the Archivist for information.
    *   **The Infernal Prosecutor's Office** (Major)
        *   **Goals:** To ensure all contracts are enforced to the letter, maximizing the number of souls condemned.
        *   **Hierarchy:** A department of devil lawyers led by the ruthless Prosecutor Malakor.
        *   **Public Agenda:** To uphold the laws of Hell.
        *   **Secret Agenda:** To meet their soul quotas and gain favor with the Archdevils.
        *   **Assets:** The full backing of the infernal judiciary, vast legal resources, an army of paralegal imps.
        *   **Relationships:** The primary antagonists in the courtroom.
    *   **The Infernal Archives** (Major)
        *   **Goals:** To catalog and preserve every contract, law, and legal precedent in the Nine Hells.
        *   **Hierarchy:** Managed by the ancient, neutral demon, Xylos.
        *   **Public Agenda:** To be a neutral repository of information.
        *   **Secret Agenda:** Xylos is secretly compiling a "Codex of Loopholes" and may help those who bring him new and interesting legal arguments.
        *   **Assets:** A library containing every contract ever signed, legal golems, sentient scrolls.
        *   **Relationships:** A neutral faction that can be a vital source of information for a price.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Prosecutor Malakor:** A cunning, charismatic, and ruthless devil lawyer who serves as the party's recurring rival.
    *   **Judge Abaddon:** An ancient, impartial, but easily bored infernal judge who values procedure and novelty.
    *   **Xylos, the Archivist:** A monotone, obsessive, and secretly helpful demon who guards the Archives of Damnation.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Desperate Mortal Client"
    *   "Conniving Imp Witness"
    *   "Corrupt Devilish Bailiff"
    *   "Legal Golem (Creature)"
    *   "Rival Defense Attorney"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Infernal Courthouse:** A towering, obsidian structure where trials are held.
        *   **Key Landmarks:** The main courtroom with its jury of tormented souls, the holding cells, the prosecutor's office, the judge's chambers.
        *   **Primary Inhabitants:** Devils, lawyers, judges, bailiffs, and the damned.
        *   **Available Goods & Services:** Justice (of a sort), legal filings, appeals (for a hefty fee).
        *   **Potential Random Encounters (x5):** A rival lawyer tries to steal a case file, a key witness is intimidated by a bailiff, a judge offers a hint in exchange for a bribe, a fight breaks out between two demonic litigants, a player is held in contempt of court.
        *   **Embedded Plot Hooks & Rumors (x3):** "Judge Abaddon can be swayed by a sufficiently dramatic and entertaining argument." "Prosecutor Malakor has a secret weakness for infernal gambling." "The jury is made up of souls who were all condemned by the same prosecutor."
        *   **Sensory Details:** Sight (Black marble, flickering hellfire, chains, suffering), Sound (The screams of the damned, the bang of a gavel, booming legal arguments), Smell (Brimstone, old parchment, fear).
    *   **The Archives of Damnation:** A vast, dusty library containing every contract ever signed.
        *   **Key Landmarks:** The section for soul-pacts, the aisle of broken promises, the vault of Archdevil contracts, Xylos's personal desk.
        *   **Primary Inhabitants:** Xylos the Archivist, sentient scrolls, legal golems, dust devils.
        *   **Available Goods & Services:** Access to legal precedents, contract verification, research.
        *   **Potential Random Encounters (x5):** A sentient contract tries to make a deal with a player, a legal golem challenges the party's authorization, a rival legal team is researching the same case, a key contract is misfiled, Xylos offers a cryptic clue in exchange for a new legal argument.
        *   **Embedded Plot Hooks & Rumors (x3):** "There's a loophole in the original contract that founded Dis." "Xylos is looking for a copy of a mortal's legal textbook." "A contract can be voided if it is eaten by a specific type of paper-eating demon."
        *   **Sensory Details:** Sight (Endless shelves, floating scrolls, glowing runes), Sound (A profound, dusty silence; the rustle of paper; the monotone voice of Xylos), Smell (Old paper, dust, ink, regret).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players win a case by exploiting a loophole.
    *   **THEN:** They gain "Legal Precedent" points. The infernal bureaucracy creates a new subcommittee to close the loophole, creating more red tape for future cases.
    *   **IF:** The players take on a case that has a high "Moral Cost" (e.g., defending a guilty but powerful client).
    *   **THEN:** Their Moral Cost tracker increases. This may cause them to have disadvantage on social checks with good-aligned celestials or mortals, but advantage on checks with devils.
    *   **IF:** The players successfully expose the corruption of a judge.
    *   **THEN:** The judge is demoted to a lower circle of Hell, but the entire judiciary becomes hostile to the players, assigning their cases to the strictest, most unforgiving judges.
    *   **IF:** The players lose a case and their client's soul is condemned.
    *   **THEN:** The client becomes a tormented soul who may appear later as a hostile spirit or a bitter witness in another case.
    *   **IF:** In the finale, the players successfully challenge the legality of soul contracts themselves.
    *   **THEN:** Generate two epilogues: 1) They win, causing the entire infernal economy to collapse into chaos and making them the most wanted mortals in the Nine Hells. 2) They lose, and as punishment, their own souls are placed under a new, unbreakable contract, binding them to serve as infernal prosecutors for a century.
