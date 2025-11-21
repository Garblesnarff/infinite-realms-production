### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Chronos Commandos**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The players are a team of elite temporal agents, recruited from across time to protect the timeline. Their mission is to hunt the rogue chronomancer, Malachi, who is traveling through history, altering key events and causing devastating paradoxes. The campaign is a high-octane chase across time, from the age of dinosaurs to the far future, to stop him before he unravels reality itself.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of the Temporal Concordance and its mission to protect the timeline.
    *   Write the story of a major temporal war that led to the strict laws of time travel.
    *   Describe the nature of a "paradox" in this universe and the potential consequences of a timeline unraveling.
    *   Explain the origins of Malachi. Who was he before he went rogue, and what event triggered his crusade?
    *   Detail the technology behind the Concordance's time-jump equipment and temporal abilities.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Chronos Commandos (The Players)** (Major)
        *   **Goals:** To hunt down Malachi, repair the damage to the timeline, and prevent paradoxes.
        *   **Hierarchy:** An elite team operating under the direct command of the Administrator.
        *   **Public Agenda:** None. They operate in secret throughout time.
        *   **Secret Agenda:** To uncover the truth about Malachi's origins, which may be linked to the Concordance itself.
        *   **Assets:** Advanced temporal technology, access to historical data, a base outside of time.
        *   **Relationships:** In direct conflict with Malachi; rivals with Agent Paradox's faction.
    *   **Malachi's Anachronists** (Major)
        *   **Goals:** To rewrite history according to Malachi's vision.
        *   **Hierarchy:** Led by the charismatic Malachi, with a small following of loyal temporal renegades.
        *   **Public Agenda:** To "improve" history by correcting its greatest tragedies.
        *   **Secret Agenda:** Malachi is trying to prevent a personal tragedy from his own past, regardless of the cost to the timeline.
        *   **Assets:** A powerful, experimental time-travel device; deep knowledge of historical pivot points; an army of anachronistically-enhanced followers (e.g., mobsters with laser guns).
        *   **Relationships:** The primary antagonists, viewing the Commandos as slaves to a flawed history.
    *   **The Revisionists** (Minor)
        *   **Goals:** To create their own "perfect" timeline by making subtle, strategic alterations.
        *   **Hierarchy:** A splinter faction within the Temporal Concordance, secretly led by Agent Paradox.
        *   **Public Agenda:** To be the most effective agents in the Concordance.
        *   **Secret Agenda:** To subtly sabotage the Commandos' missions to allow for small, beneficial paradoxes to occur.
        *   **Assets:** Access to Concordance resources, inside information, a willingness to bend the rules.
        *   **Relationships:** Covert rivals to the players, pretending to be allies.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Malachi:** The brilliant, charismatic, and tragic rogue chronomancer who is a future version of a party member.
    *   **The Administrator:** The cold, detached, and mysterious AI that leads the Temporal Concordance.
    *   **Agent Paradox:** A reckless and arrogant rival temporal agent who is secretly working for a splinter faction.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Confused Historical Figure"
    *   "Anachronistically-enhanced Thug"
    *   "Dinosaur with Mind-Control Tech (Creature)"
    *   "By-the-book Concordance Analyst"
    *   "Futuristic Robot Enforcer (Creature)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections. Each location must be in a distinct time period.
*   **Location Roster:**
    *   **1920s Chicago (Altered):** A Prohibition-era city where mobsters have been given advanced weaponry by Malachi.
        *   **Key Landmarks:** The speakeasy headquarters of the laser-gun-toting mob, the city bank under siege, the docks where a temporal beacon is hidden.
        *   **Primary Inhabitants:** Mobsters with laser guns, terrified citizens, overwhelmed police officers.
        *   **Available Goods & Services:** Illegal booze, historical information (if you can get anyone to talk).
        *   **Potential Random Encounters (x5):** A drive-by shooting with laser rifles, a police raid on a speakeasy, a meeting with a historical figure who shouldn't be there, a temporal distortion causes a car to be replaced by a horse, a rival agent is seen observing the party.
        *   **Embedded Plot Hooks & Rumors (x3):** "Al Capone is not in charge anymore; some new guy with strange tech is." "The mob's new guns came from a man who 'fell from the sky.'" "There's a strange humming sound coming from the docks."
        *   **Sensory Details:** Sight (Flashing laser fire, classic 1920s architecture, pinstripe suits), Sound (The roar of Tommy guns and laser rifles, jazz music, police sirens), Smell (Gunpowder, ozone, spilled whiskey).
    *   **The End of Time:** A place of pure chaos and entropy, where all timelines converge and eventually die.
        *   **Key Landmarks:** Malachi's Fortress of Time, the River of Chronal Energy, the Graveyard of Lost Moments, the Anomaly Engine.
        *   **Primary Inhabitants:** Temporal predators, echoes of people who never existed, Malachi himself.
        *   **Available Goods & Services:** None. This is the final dungeon.
        *   **Potential Random Encounters (x5):** A wave of entropy ages a player's equipment to dust, a vision of a possible future appears, the party is attacked by their own temporal duplicates, gravity reverses, a piece of a completely alien timeline drifts by.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Anomaly Engine is powered by paradoxes." "Malachi's fortress is built from moments he has stolen from history." "The only way to destroy the Engine is to create a paradox big enough to erase it."
        *   **Sensory Details:** Sight (A chaotic swirl of colors and light, fragments of different places and times, impossible geometry), Sound (A deafening silence punctuated by the roar of collapsing timelines), Smell (Nothing, and everything, all at once).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players take an action that increases the Paradox Level (e.g., leaving future tech in the past).
    *   **THEN:** Generate a minor, strange side effect. A historical figure now has a piece of anachronistic knowledge, or a player's own memories of their past become fuzzy.
    *   **IF:** The players successfully repair a major historical event that Malachi altered.
    *   **THEN:** The timeline stabilizes, and the Paradox Level decreases. The Administrator provides the party with a new piece of temporal technology as a reward.
    *   **IF:** The players fail to stop Malachi from stealing the Holy Grail.
    *   **THEN:** Malachi uses its power to create a more powerful and stable portal to the future, making him harder to track. The party must now deal with a new faction: angry knights of the Round Table who have followed them through time.
    *   **IF:** The players discover that Malachi is a future version of one of their own.
    *   **THEN:** That player begins to experience flashes of Malachi's memories, gaining clues but also risking psychic damage. This creates a moral crisis within the party.
    *   **IF:** In the finale, the players choose to destroy the Anomaly Engine, erasing their own existence.
    *   **THEN:** Generate an epilogue showing the new, stable timeline. The world is safe, but no one remembers the Chronos Commandos or their sacrifice. A final scene shows a new team of Commandos being recruited, implying the cycle continues.
