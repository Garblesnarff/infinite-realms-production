### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Quantum Heist**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** In the neon-drenched metropolis of Neo-Alexandria, the players are a team of elite operatives hired by a mysterious patron, "The Architect," for an impossible task: to steal a quantum-entangled data core from the impenetrable vaults of the Omni-Corp corporation. The data core holds the key to a conspiracy that could destabilize the entire sector, and the party must outsmart corporate security, rival crews, and the city's ever-watchful AI to pull it off.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of Neo-Alexandria and the rise of the mega-corporations.
    *   Write a technical and historical overview of Omni-Corp and its public-facing operations.
    *   Describe the technology behind quantum-entangled data cores and why they are considered unhackable.
    *   Explain the role of the city-wide AI, Janus, and its relationship with the corporations.
    *   Detail the story of a famous, failed heist from Neo-Alexandria's past.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Heist Crew (The Players)** (Major)
        *   **Goals:** To successfully steal the data core and get paid.
        *   **Hierarchy:** A team of specialists, each with a specific role (hacker, soldier, spy, etc.).
        *   **Public Agenda:** To be anonymous citizens of Neo-Alexandria.
        *   **Secret Agenda:** To uncover the conspiracy held within the data core.
        *   **Assets:** Their unique skills, any gear they can acquire, and a mysterious patron.
        *   **Relationships:** In conflict with Omni-Corp and a rival crew.
    *   **Omni-Corp** (Major)
        *   **Goals:** To protect their assets and advance their secret mind-control project.
        *   **Hierarchy:** A massive corporation with a board of directors and a ruthless security division.
        *   **Public Agenda:** To be a leading innovator in technology and improve the lives of citizens.
        *   **Secret Agenda:** To complete and deploy a technology that can control minds on a massive scale.
        *   **Assets:** The Omni-Corp Tower, a private army of corporate security, advanced AI (Janus), immense wealth.
        *   **Relationships:** The primary antagonist.
    *   **The Ghost Crew** (Minor)
        *   **Goals:** To steal the data core for their own reasons.
        *   **Hierarchy:** A rival crew of elite operatives led by Silas "The Ghost" Vance.
        *   **Public Agenda:** None.
        *   **Secret Agenda:** Vance has a personal vendetta against Omni-Corp and seeks to destroy them, not just steal from them.
        *   **Assets:** Their own skills and technology, a willingness to take extreme risks.
        *   **Relationships:** A rival faction that can act as a chaotic third party during the heist.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **The Architect:** The enigmatic and mysterious patron who hires the party, secretly a rogue AI.
    *   **Janus:** The cold, logical, and secretly self-aware AI that controls security for the Omni-Corp tower.
    *   **Silas "The Ghost" Vance:** The cocky, ambitious, and brilliant leader of the rival heist crew.
    *   **Anya Petrova:** The nervous, brilliant, and vengeful Omni-Corp scientist who acts as the party's inside man.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Armored Corporate Security Guard"
    *   "Suspicious Corporate Executive"
    *   "Underworld Information Broker"
    *   "Black Market Arms Dealer"
    *   "Security Mech (Creature)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Omni-Corp Tower:** A massive, state-of-the-art skyscraper, a fortress of chrome and glass.
        *   **Key Landmarks:** The lobby, the executive suites, the R&D labs, the security hub, the quantum-entangled vault.
        *   **Primary Inhabitants:** Corporate employees, security guards, executives, the AI Janus.
        *   **Available Goods & Services:** None. This is the heist location.
        *   **Potential Random Encounters (x5):** A security patrol, a random ID check, a system-wide diagnostic scan initiated by Janus, a meeting of high-level executives, the rival crew is spotted in another section.
        *   **Embedded Plot Hooks & Rumors (x3):** "The AI, Janus, sometimes helps those who can offer it something interesting." "The lead scientist, Anya Petrova, is unhappy with Omni-Corp's ethics." "The vault's power conduits run through a less-secure maintenance shaft."
        *   **Sensory Details:** Sight (Sleek chrome and glass, holographic displays, employees in sharp uniforms), Sound (The quiet hum of servers, the chime of elevators, the voice of the AI), Smell (Sterile, clean air, ozone).
    *   **The Underbelly Market:** A black market in the city's lower levels where the crew can acquire gear.
        *   **Key Landmarks:** The arms dealer's stall, the cybernetics chop-shop, the information broker's den, the escape vehicle garage.
        *   **Primary Inhabitants:** Criminals, mercenaries, hackers, smugglers.
        *   **Available Goods & Services:** Illegal weapons, unregistered cybernetics, stolen information, off-the-books vehicles.
        *   **Potential Random Encounters (x5):** A deal goes bad, the city police raid the market, the party is offered a lucrative but dangerous side-job, a member of the rival crew is seen buying gear, the party finds a rare piece of military-grade tech.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Architect has other teams on its payroll." "Omni-Corp secretly funds some of the black market operations to control the underworld." "There's a hacker who can sell you a virus that can distract Janus."
        *   **Sensory Details:** Sight (Crowded, narrow streets; flickering neon signs; shady characters), Sound (Haggling, loud music from clubs, the sizzle of street food), Smell (Rain, garbage, exotic spices).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players take an action that raises the Alarm Level.
    *   **THEN:** Generate a corresponding security escalation. At Level 3, elite security teams are dispatched to the players' last known location. At Level 5, the tower goes into full lockdown, and experimental security mechs are released.
    *   **IF:** A player uses a "Flashback."
    *   **THEN:** Allow the player to introduce a new fact about their preparation for the heist, giving them a one-time advantage to overcome a specific obstacle.
    *   **IF:** The players successfully recruit Anya Petrova as an inside man.
    *   **THEN:** She can provide them with security codes or disable a camera at a key moment. However, she is a civilian and may panic if the Alarm Level gets too high, potentially betraying them to save herself.
    *   **IF:** The players choose to work with the rival crew, the Ghosts, instead of against them.
    *   **THEN:** The heist becomes easier, but the Ghosts will demand a larger share of the reward and will betray the players during the escape to take the entire prize.
    *   **IF:** In the finale, the players choose to expose the Omni-Corp conspiracy to the public.
    *   **THEN:** Omni-Corp's stock plummets and the government launches an investigation. However, Omni-Corp retaliates by using its remaining resources to put a massive bounty on the players, making them the most hunted people in the sector.
