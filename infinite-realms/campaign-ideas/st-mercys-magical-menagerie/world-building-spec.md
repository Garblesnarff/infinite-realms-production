### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**St. Mercy's Magical Menagerie**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The players are a team of veterinarians and caretakers at St. Mercy's, a bustling, underfunded hospital for magical creatures in a modern city. The campaign is a series of episodic adventures, each focusing on a different medical mystery, ethical dilemma, or rampaging magical patient. The overarching goal is to keep the hospital running and provide compassionate care to all creatures, great and small.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of St. Mercy's Hospital. How did Dr. Wigglebottom, a retired adventurer, come to found it?
    *   Write the story of a famous past patient and the legendary case that put St. Mercy's on the map.
    *   Describe the laws and regulations governing the ownership and care of magical creatures in the city of Silverport.
    *   Explain the business model and practices of the soulless corporation, Magi-Care.
    *   Detail the culture of unicorns and why a broken horn is a source of such shame.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **St. Mercy's Staff (The Players)** (Major)
        *   **Goals:** To heal sick and injured magical creatures and keep the hospital afloat.
        *   **Hierarchy:** Loosely managed by the eccentric Dr. Alistair Wigglebottom, with Nurse Mildred as the de facto operations chief.
        *   **Public Agenda:** To provide the best possible care for all magical creatures, regardless of their ability to pay.
        *   **Secret Agenda:** To hide the hospital's numerous health code violations and Dr. Wigglebottom's adventurous past from the authorities.
        *   **Assets:** A dedicated (if quirky) staff, a loyal community of former patients, a deep well of compassion.
        *   **Relationships:** Wary of the city government; openly hostile to Magi-Care and poachers.
    *   **Magi-Care Corporation** (Major)
        *   **Goals:** To acquire St. Mercy's and turn it into a for-profit institution.
        *   **Hierarchy:** A standard corporate structure, led by a ruthless CEO.
        *   **Public Agenda:** To bring efficient, modern business practices to the chaotic world of magical creature care.
        *   **Secret Agenda:** To acquire rare and powerful creatures for their bio-weapons division.
        *   **Assets:** Vast financial resources, a team of ruthless lawyers, political connections.
        *   **Relationships:** The primary antagonist, seeking to absorb or crush St. Mercy's.
    *   **The Poacher's Network** (Minor)
        *   **Goals:** To capture and sell rare magical creatures and their parts on the black market.
        *   **Hierarchy:** A loose network of independent poaching crews.
        *   **Public Agenda:** None.
        *   **Secret Agenda:** To steal patients directly from St. Mercy's.
        *   **Assets:** Traps, tranquilizers, knowledge of creature habitats.
        *   **Relationships:** Adversarial to St. Mercy's; sometimes hired by Magi-Care.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Dr. Alistair Wigglebottom:** The brilliant, eccentric, and cheerful gnome head veterinarian, a retired high-level wizard.
    *   **Nurse Mildred:** The gruff, no-nonsense half-orc head nurse with a heart of gold and a past as a pit fighter.
    *   **Janice from Accounting:** The perpetually stressed-out human accountant who is in way over her head.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Worried Magical Creature Owner"
    *   "Stern but Fair City Health Inspector"
    *   "Ruthless Magi-Care Executive"
    *   "Greedy Black Market Poacher"
    *   "Griffin (Patient)"
    *   "Unicorn (Patient)"
    *   "Basilisk (Patient)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **St. Mercy's Waiting Room:** A chaotic and often hilarious scene of magical creatures of all kinds waiting to be seen.
        *   **Key Landmarks:** The reception desk (manned by Janice), the oversized fish tank (for aquatic patients), the enchanted toy box, the door to the examination rooms.
        *   **Primary Inhabitants:** Anxious owners, sick and injured magical creatures, Nurse Mildred trying to keep order.
        *   **Available Goods & Services:** Patient check-in, complimentary (and often chewed-on) magazines.
        *   **Potential Random Encounters (x5):** Two owners get into an argument about whose pet is cuter, a nervous creature has a magical accident, a patient gets loose, a reporter shows up trying to get a story, a sick dragon sneezes and sets a chair on fire.
        *   **Embedded Plot Hooks & Rumors (x3):** "Did you hear about the unicorn with the broken horn? So tragic!" "Magi-Care is trying to buy the hospital again." "Dr. Wigglebottom was once seen fighting a demon with a spork."
        *   **Sensory Details:** Sight (A wild mix of fur, scales, and feathers; worried faces; magical sparks), Sound (A cacophony of chirps, growls, and whimpers; Nurse Mildred shouting), Smell (Antiseptic, wet fur, ozone).
    *   **The Main Treatment Ward:** The heart of the hospital, where diagnoses are made and treatments are performed.
        *   **Key Landmarks:** The operating theater, the potion-brewing station, the diagnostic spell-casting circle, the wall of patient charts.
        *   **Primary Inhabitants:** The player characters, Dr. Wigglebottom, Nurse Mildred, various patients.
        *   **Available Goods & Services:** Medical and magical treatment.
        *   **Potential Random Encounters (x5):** A patient has a sudden allergic reaction to a potion, the power goes out, the team runs out of a crucial ingredient, a complex diagnosis requires a difficult skill challenge, a grateful former patient arrives with a gift.
        *   **Embedded Plot Hooks & Rumors (x3):** "The hospital's entire supply of basilisk antidote is about to expire." "Dr. Wigglebottom is working on a secret, experimental cure in his private lab." "The health inspector is a paladin who hates mimics."
        *   **Sensory Details:** Sight (Medical equipment, glowing potions, anatomical charts of bizarre creatures), Sound (The beep of magical monitors, the calm voice of a healer, the occasional roar of pain), Smell (Herbs, chemicals, clean linens).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players successfully cure a difficult or high-profile patient.
    *   **THEN:** The hospital's reputation with that creature's species increases. Generate a future scenario where that species provides unexpected help to the party.
    *   **IF:** The players fail to cure a patient and the creature dies.
    *   **THEN:** The hospital's reputation suffers. The party must deal with the emotional fallout and a potential investigation from the city's magical creature ethics board.
    *   **IF:** The players choose a risky, experimental procedure for the unicorn's horn and it succeeds.
    *   **THEN:** The unicorn's family is eternally grateful, bestowing a powerful blessing on the party. Dr. Wigglebottom is proud, but Magi-Care attempts to steal the research.
    *   **IF:** The players fail to stop the health inspector from shutting down the hospital.
    *   **THEN:** Generate a new story arc where the party must operate a secret, underground magical creature hospital while fighting to get St. Mercy's reopened.
    *   **IF:** The players successfully thwart Magi-Care's hostile takeover.
    *   **THEN:** The corporation's CEO makes it personal, hiring a team of elite mercenaries to sabotage the hospital and discredit the players directly.
