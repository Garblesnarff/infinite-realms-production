### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**Chronos Investigations, Inc.**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The players are agents of Chronos Investigations, Inc., a secretive organization tasked with preserving the timeline's integrity. When temporal anomalies or sabotage occur, they jump through different eras to solve mysteries and prevent catastrophic paradoxes. Their first major case involves a series of coordinated anomalies, revealing a shadowy organization, the "Achronists," who believe the timeline is flawed and seek to rewrite it to their own design.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the founding of Chronos Investigations, Inc. and the discovery of stable time travel.
    *   Write the history of a major temporal disaster that led to the strict rules Chronos Inc. now follows.
    *   Describe the "Prime Timeline" and why it is considered the correct one.
    *   Explain the theoretical dangers of a Grand Paradox and what it would mean for reality.
    *   Detail the origins and philosophy of the Achronist movement.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **Chronos Investigations, Inc.** (Major)
        *   **Goals:** To preserve the Prime Timeline and prevent paradoxes.
        *   **Hierarchy:** Led by the enigmatic Director Paradox, with department heads for Research, Field Operations, and Historical Archives.
        *   **Public Agenda:** They have no public presence.
        *   **Secret Agenda:** To protect the Director's own paradoxical existence, which is tied to the stability of the Prime Timeline.
        *   **Assets:** Time-travel technology, a headquarters outside of time, extensive historical archives, trained temporal agents.
        *   **Relationships:** Covertly opposed to the Achronists; wary of other, unknown temporal powers.
    *   **The Achronists** (Major)
        *   **Goals:** To reshape the timeline according to their own design, which they believe is morally superior.
        *   **Hierarchy:** Led by the charismatic Chronal Architect.
        *   **Public Agenda:** They have no public presence.
        *   **Secret Agenda:** To restore their own erased timeline, even if it means destroying the current one.
        *   **Assets:** Stolen or reverse-engineered time-travel tech, deep knowledge of historical pivot points, fanatical followers.
        *   **Relationships:** Actively hostile towards Chronos Inc.; view history as a tool to be manipulated.
    *   **Temporal Bounty Hunters Guild** (Minor)
        *   **Goals:** To profit by capturing or eliminating individuals who have gone rogue in the timeline.
        *   **Hierarchy:** A loose network of independent contractors.
        *   **Public Agenda:** None.
        *   **Secret Agenda:** Will work for the highest bidder, be it Chronos Inc. or the Achronists.
        *   **Assets:** Individual time-jump devices, tracking equipment, non-lethal temporal weaponry.
        *   **Relationships:** Neutral, but their actions often complicate matters for both major factions.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Director Paradox:** The enigmatic, calm, and cryptic head of Chronos Inc., who is himself a temporal anomaly.
    *   **Agent "Tick-Tock" Thorne:** A cynical, world-weary veteran agent who acts as a rival or mentor to the players.
    *   **The Chronal Architect:** The brilliant, charismatic, and morally convinced leader of the Achronists.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Naive Historical Figure"
    *   "Jaded Chronos Inc. Archivist"
    *   "Fanatical Achronist Saboteur"
    *   "Ruthless Temporal Bounty Hunter"
    *   "Confused Local Law Enforcement (in any era)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **Chronos Inc. Headquarters:** A facility existing outside of normal time, the campaign hub.
        *   **Key Landmarks:** The Director's Office, the Temporal Scanners room, the Historical Archives, the Time-Jump Chamber.
        *   **Primary Inhabitants:** Chronos agents, researchers, archivists, and support staff.
        *   **Available Goods & Services:** Mission briefings, temporal equipment, access to historical data, medical facilities.
        *   **Potential Random Encounters (x5):** A temporal alert goes off, Agent Thorne offers unsolicited advice, a training simulation goes awry, a debate between two historians about a key event, a newly discovered anachronism is brought in for analysis.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Director's office seems to phase out of reality sometimes." "Thorne lost his last partner in the Renaissance." "The Archives have a record of a timeline where the Achronists won."
        *   **Sensory Details:** Sight (Clean, sterile corridors, holographic displays, flickering temporal screens), Sound (A low, constant hum, the quiet murmur of researchers, sudden alarms), Smell (Ozone, old paper, antiseptic).
    *   **The Temporal Nexus:** A fluctuating point in the timeline where multiple eras converge.
        *   **Key Landmarks:** A Roman column next to a flickering neon sign, a medieval gate that opens into a futuristic city, a river that flows with liquid time.
        *   **Primary Inhabitants:** Lost travelers, temporal predators, rogue agents from various factions.
        *   **Available Goods & Services:** None. Highly dangerous and unstable.
        *   **Potential Random Encounters (x5):** A dinosaur wanders out of a portal, a brief, violent skirmish between Achronists and Chronos agents from another team, a valuable piece of tech from a lost timeline appears, reality briefly shifts to an alternate history, a temporal storm erases a section of the Nexus.
        *   **Embedded Plot Hooks & Rumors (x3):** "There's a trader in the Nexus who sells items from dead timelines." "The Achronists use the Nexus as a secret highway." "The center of the Nexus is said to show you your own death."
        *   **Sensory Details:** Sight (Shifting landscapes, flickering portals, clashing architecture), Sound (A cacophony of different eras: horses, hover-cars, sword fights), Smell (Constantly changing: rain, ozone, gunpowder, flowers).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** A player reveals future knowledge to a historical figure.
    *   **THEN:** The player gains Paradox Points. Generate a minor temporal glitch affecting the player (e.g., their reflection is briefly older, a key item is temporarily replaced with an anachronistic one).
    *   **IF:** The party accumulates a high number of Paradox Points as a group.
    *   **THEN:** Generate a "Temporal Backlash" mission, where the party must jump to a new location to fix a problem they inadvertently created (e.g., a historical figure now has a strange obsession with "rock and roll").
    *   **IF:** The players successfully prevent the Achronists from stealing a key historical artifact.
    *   **THEN:** The Achronists retaliate by targeting a moment in one of the players' own pasts, forcing a deeply personal mission.
    *   **IF:** The players manage to capture and interrogate a high-ranking Achronist.
    *   **THEN:** They learn the location of the Achronist base, but the information is a trap designed to lure them to a specific point in time.
    *   **IF:** During the final confrontation, the players choose to let a "correctable" but morally reprehensible historical event happen to preserve the timeline.
    *   **THEN:** Generate the emotional and psychological fallout for the characters. Director Paradox commends their difficult choice, but Agent Thorne expresses his disgust, creating a rift in the party's relationship with their mentors.
