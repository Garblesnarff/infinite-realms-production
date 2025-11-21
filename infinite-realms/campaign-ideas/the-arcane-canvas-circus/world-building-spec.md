### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Arcane Canvas Circus**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The players are performers in a traveling circus known for its seemingly impossible acts. They soon discover their talents are not tricks, but manifestations of latent, untrained magic. When a shadowy organization, the "Order of the Suppressed Arcane," begins hunting individuals with uncontrolled magic, the circus must go on the run, forcing the players to master their powers, protect their troupe, and uncover the truth behind their pursuers.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of the Order of the Suppressed Arcane. What event led to their belief that uncontrolled magic is a danger?
    *   Write the story of Madame Zola's past as a powerful mage and her conflict with the Order.
    *   Describe the nature of "latent magic" in this world. Why is it now awakening in random individuals?
    *   Explain the structure and purpose of the underground network of magic-users.
    *   Detail a famous historical event that was secretly caused by a wild magic surge.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Arcane Canvas Circus** (Major)
        *   **Goals:** To survive, to protect its members, and to put on a good show.
        *   **Hierarchy:** Led by the ringmaster, Madame Zola, with a core group of senior performers (including the players).
        *   **Public Agenda:** We are a simple circus, here to entertain.
        *   **Secret Agenda:** To act as a mobile sanctuary and recruitment center for individuals with latent magic.
        *   **Assets:** A loyal troupe of performers, specialized caravan wagons, the element of surprise.
        *   **Relationships:** Hunted by the Order; cautiously allied with the magical underground.
    *   **The Order of the Suppressed Arcane** (Major)
        *   **Goals:** To find, capture, and "cure" or neutralize all those with uncontrolled magical abilities.
        *   **Hierarchy:** A rigid, monastic structure led by a council of elders, with field agents like Silas the Silent Seeker.
        *   **Public Agenda:** To protect the world from magical catastrophes.
        *   **Secret Agenda:** To hoard magical power for themselves, believing only they are worthy to wield it.
        *   **Assets:** A network of spies, anti-magic technology, trained magical nullifiers, secret enclaves.
        *   **Relationships:** The primary antagonists, viewing the circus as a dangerous collection of anomalies.
    *   **The Underground Network** (Minor)
        *   **Goals:** To help latent magic-users escape the Order and learn to control their powers.
        *   **Hierarchy:** A decentralized network of safe houses and contacts.
        *   **Public Agenda:** None.
        *   **Secret Agenda:** To eventually launch a rebellion against the Order.
        *   **Assets:** Secret communication methods, hidden safe houses, knowledge of the Order's movements.
        *   **Relationships:** A potential ally for the circus, but deeply paranoid and hard to find.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Madame Zola:** The charismatic, enigmatic, and fiercely protective ringmaster, a former mage who lost her powers.
    *   **Silas, the Silent Seeker:** A cold, methodical, and righteous agent of the Order, driven by a past trauma.
    *   **The Great Mysterio:** A jealous rival magician who uses stage tricks and seeks to expose the circus.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Naive Young Performer with a New Power"
    *   "Grizzled Circus Roustabout"
    *   "Fanatical Order Agent"
    *   "Paranoid Underground Contact"
    *   "Suspicious Town Sheriff"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Big Top:** The heart of the circus, a place of wonder and danger, constantly being set up and torn down.
        *   **Key Landmarks:** The Center Ring, the high wire, the fortune teller's tent, the backstage dressing rooms.
        *   **Primary Inhabitants:** The performers, the audience, the circus crew.
        *   **Available Goods & Services:** Entertainment, food stalls, souvenirs.
        *   **Potential Random Encounters (x5):** A magical mishap during a performance causes chaos, a player spots an Order agent in the crowd, a local noble challenges a performer to a duel of skills, a child sneaks backstage and gets into trouble, a magical creature gets loose.
        *   **Embedded Plot Hooks & Rumors (x3):** "Madame Zola spends a lot of time in her private wagon, and no one is allowed in." "The strongman isn't just strong; they say he can't be harmed by metal." "The last town we were in, someone went missing after our show."
        *   **Sensory Details:** Sight (Colorful banners, sawdust, bright lights, cheering crowds), Sound (Upbeat circus music, applause, gasps of wonder), Smell (Popcorn, sawdust, animal musk).
    *   **An Order of the Suppressed Arcane Enclave:** A secret, sterile facility where the Order studies and suppresses magic.
        *   **Key Landmarks:** The Nullification Chamber, the subject holding cells, the research library, the training yard for agents.
        *   **Primary Inhabitants:** Order agents, captured magic-users, magical researchers.
        *   **Available Goods & Services:** None. This is an enemy stronghold.
        *   **Potential Random Encounters (x5):** A patrol of agents, a magical alarm is triggered, the party finds a captured magic-user they can rescue, a high-ranking agent like Silas arrives, the party discovers a logbook detailing the Order's future plans.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Order is developing a weapon that can detect latent magic from miles away." "Their leader was once a famous archmage." "They have a prison for creatures made of pure magic."
        *   **Sensory Details:** Sight (Cold stone or metal walls, anti-magic runes, sterile equipment), Sound (Oppressive silence, the hum of machinery, distant, muffled cries), Smell (Antiseptic, ozone, cold stone).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** A player uses their "Performance & Power" mechanic and rolls a critical success.
    *   **THEN:** Generate a spectacular, unexpected magical display that has a positive side effect (e.g., the acrobat's flight not only awes the crowd but also reveals the location of a hidden Order agent).
    *   **IF:** A player uses their "Performance & Power" mechanic and rolls a critical failure.
    *   **THEN:** Generate a wild magic surge. The effect should be related to their act but have a chaotic, comedic, or dangerous outcome (e.g., the juggler's balls turn into angry pixies; the fire-breather accidentally polymorphs the town mayor into a sheep).
    *   **IF:** The players successfully rescue the abducted performer in Act 1.
    *   **THEN:** The rescued performer becomes a key ally with crucial information about the Order's methods. The Order, in turn, assigns a higher-level agent (Silas) to the case.
    *   **IF:** The players choose to trust the Underground Network with a dangerous secret.
    *   **THEN:** The Network provides them with a powerful, one-time-use magical item. However, this also puts the Network at risk, leading to a future mission where the players must protect a safe house from an Order raid.
    *   **IF:** In the finale, the players choose to expose the Order's secrets to the world.
    *   **THEN:** The Order is thrown into disarray, but it also causes a worldwide panic about magic. Generate an epilogue where the circus becomes a symbol of a new "magical rights" movement, facing a whole new set of political challenges.
