### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**Objection, Your Honorificence!**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** In the city of Lex, where the Law is a literal, magical force, the players are a team of "Advocates" (part-lawyer, part-investigator). They take on an impossible case: defending a hapless imp named Fizzle, who is accused of murdering a powerful merchant prince. They must navigate the city's arcane legal system, uncover a deep-seated conspiracy, and face a ruthless prosecutor in a trial where losing means being magically written out of existence.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the founding of the city of Lex and the creation of its magic-infused legal code.
    *   Write the history of the Justicar, the ancient stone golem judge. Who created it and why?
    *   Describe the structure and rules of the Aetheneum of Law, the magical law library.
    *   Explain the magical mechanics of a "Zone of Truth" and how it can be legally circumvented or manipulated.
    *   Detail a famous past case that set a major precedent in Lex's legal system.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Advocate's Guild (The Players)** (Minor)
        *   **Goals:** To prove their client, Fizzle, innocent and expose the real killer.
        *   **Hierarchy:** A small, independent legal practice.
        *   **Public Agenda:** To provide legal representation for the downtrodden and wrongly accused.
        *   **Secret Agenda:** To make a name for themselves and expose the corruption within the city's elite.
        *   **Assets:** Their law office (The Gilded Scales), their wits, and any evidence they can gather.
        *   **Relationships:** Adversarial with the Prosecutor's Office; reliant on underworld contacts for information.
    *   **The Prosecutor's Office** (Major)
        *   **Goals:** To secure convictions and maintain a high success rate.
        *   **Hierarchy:** Led by the Advocate General, with a team of junior prosecutors and investigators.
        *   **Public Agenda:** To uphold the Law and punish the guilty.
        *   **Secret Agenda:** Advocate General Cassian is driven by a need to maintain his perfect record, leading him to ignore contradictory evidence.
        *   **Assets:** The resources of the city guard, access to certified evidence, a powerful reputation.
        *   **Relationships:** The primary antagonists in the courtroom.
    *   **The Merchant's Consortium** (Major)
        *   **Goals:** To protect their business interests and maintain their influence over the city.
        *   **Hierarchy:** A council of powerful merchant princes.
        *   **Public Agenda:** To promote trade and prosperity in Lex.
        *   **Secret Agenda:** The murder victim was their rival, and they are secretly manipulating the trial to frame Fizzle and hide their own involvement.
        *   **Assets:** Immense wealth, political influence, hired thugs, and memory-modifying wizards.
        *   **Relationships:** Secretly the true antagonists; they try to appear as concerned, neutral parties.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Fizzle:** The cowardly, lying imp client who is innocent of murder but guilty of a lesser crime.
    *   **Advocate General Cassian:** The brilliant, pious, and prideful Aasimar prosecutor who has never lost a case.
    *   **The Justicar:** The ancient, silent, and utterly impartial stone golem judge.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Corrupt City Guard"
    *   "Unreliable Underworld Informant"
    *   "Spectral Librarian"
    *   "Rival Merchant Prince"
    *   "Black Market Magic-Dealer"
    *   "Garrulous Gargoyle Witness"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The High Court of the Justicar:** An intimidating, cathedral-like courtroom where the trial takes place.
        *   **Key Landmarks:** The Justicar's massive throne, the Witness Stand (glowing with a Zone of Truth), the floating Evidence Podium, the vast public gallery.
        *   **Primary Inhabitants:** The Justicar, lawyers, prosecutors, city guards, public spectators.
        *   **Available Goods & Services:** Justice (in theory).
        *   **Potential Random Encounters (x5):** The prosecution raises a surprise objection, a key piece of evidence is magically contested, a witness has a sudden panic attack on the stand, the Justicar issues a stern warning, a riot breaks out in the gallery.
        *   **Embedded Plot Hooks & Rumors (x3):** "They say the Justicar has a hidden override command." "Cassian's last opponent was written out of existence for contempt of court." "The acoustics in this room are magically perfect; no whisper goes unheard."
        *   **Sensory Details:** Sight (Towering pillars, glowing runes, stern faces), Sound (Echoing voices, the heavy silence of deliberation, the magical hum of the Zone of Truth), Smell (Old stone, polished wood, nervous sweat).
    *   **The Aetheneum of Law:** A magical law library where knowledge is power and the librarians are constructs.
        *   **Key Landmarks:** The Precedent Archives, the Section of Magical Loopholes, the Hall of Disbarred Advocates, the Riddle-Guarded Tomes.
        *   **Primary Inhabitants:** Spectral Librarians, Law Elementals, student advocates.
        *   **Available Goods & Services:** Legal research, precedent analysis, access to historical case files.
        *   **Potential Random Encounters (x5):** A Spectral Librarian demands a riddle be solved for access, a book of contracts animates and attacks, the party finds notes from a previous, failed defense of a similar case, the prosecution team is also here researching, a Law Elemental offers a cryptic clue.
        *   **Embedded Plot Hooks & Rumors (x3):** "There's a forbidden section that details how to legally summon a demon." "A loophole exists that could invalidate the entire case against Fizzle." "The library keeps a record of every contract ever signed in the city."
        *   **Sensory Details:** Sight (Floating books, glowing text, endless shelves), Sound (Profound silence, the rustling of pages, whispered riddles), Smell (Old parchment, dust, magic).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players successfully certify a piece of evidence.
    *   **THEN:** The evidence is added to their Evidence Board and can be presented in court. Generate a short scene of the prosecution team reacting to this new threat.
    *   **IF:** The players fail to certify a piece of evidence before a court deadline.
    *   **THEN:** The evidence is ruled inadmissible. The party must find a new angle or a different piece of evidence to make their point.
    *   **IF:** The players present a compelling piece of evidence in court.
    *   **THEN:** The prosecution's "Case Strength" score is reduced. Describe the reaction of the Justicar, the gallery, and Advocate Cassian.
    *   **IF:** The players successfully discredit a key prosecution witness.
    *   **THEN:** That witness's testimony is struck from the record. Generate a new opportunity for the players to investigate the witness further outside of court, as they are now a loose end.
    *   **IF:** The players can prove in court that the Merchant's Consortium tampered with the investigation.
    *   **THEN:** The Justicar immediately opens a new case against the Consortium. The Consortium panics and sends assassins to eliminate the players and Fizzle before they can testify in a new trial.
