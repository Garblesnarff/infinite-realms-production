### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Chronos Loop of Oakhaven**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The players awaken in the quaint village of Oakhaven, only to discover they are trapped in a repeating time loop. The villagers are unaware, living out the same day endlessly. The players, retaining their memories, must use their unique predicament to investigate a central mystery that occurs within the loop, hoping that by solving it, they can break the cycle.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of the village of Oakhaven. What is its significance?
    *   Write the story of the magical artifact or ritual that caused the time loop.
    *   Describe the central mystery of the loop (e.g., the murder, the theft) as it would appear to a first-time observer.
    *   Explain the nature of the Whispering Willow and its connection to the temporal anomaly.
    *   Detail the backstory of Old Man Hemlock and what he witnessed on the day the loop began.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Outsiders (The Players)** (Major)
        *   **Goals:** To understand the loop, solve the central mystery, and break the cycle.
        *   **Hierarchy:** A small group of individuals who are the only ones aware of the loop.
        *   **Public Agenda:** To appear as normal visitors or residents of Oakhaven.
        *   **Secret Agenda:** To manipulate the day's events to gather information.
        *   **Assets:** Their retained memories, the ability to experiment without permanent consequences, any skills they possessed before the loop.
        *   **Relationships:** The only faction aware of the true nature of reality; all other relationships reset daily.
    *   **The Villagers of Oakhaven** (Major)
        *   **Goals:** To live out their daily routines (e.g., prepare for the festival, run their shops).
        *   **Hierarchy:** A typical village structure led by Mayor Thistlewick.
        *   **Public Agenda:** To have a pleasant, normal day.
        *   **Secret Agenda:** Various villagers have personal, mundane secrets (e.g., a secret crush, a petty theft, a hidden debt) that may be relevant to the central mystery.
        *   **Assets:** Their predictable routines, which can be studied and exploited by the players.
        *   **Relationships:** Oblivious to the loop; their disposition towards the players resets every morning.
    *   **The Chronomancer (The Cause)** (Minor)
        *   **Goals:** Varies depending on the nature of the cause (e.g., to perfect a spell, to prevent a disaster, to trap an enemy).
        *   **Hierarchy:** A single individual or entity.
        *   **Public Agenda:** To blend in as a normal villager or remain hidden.
        *   **Secret Agenda:** To maintain the time loop for their own purposes.
        *   **Assets:** Control over the artifact or ritual generating the loop.
        *   **Relationships:** The secret antagonist or unwitting cause of the campaign's conflict.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation. Each NPC profile must include a detailed daily schedule.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Mayor Thistlewick:** The perpetually cheerful and oblivious mayor of Oakhaven.
    *   **The Chronomancer:** The hidden individual or entity responsible for the loop.
    *   **Old Man Hemlock:** The grumpy village eccentric who has fragmented memories of the loop's beginning.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Gossipy Innkeeper"
    *   "Stern Village Guard"
    *   "Lovelorn Farmer's Daughter"
    *   "Mischievous Child"
    *   "Suspicious Blacksmith"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections. Each blueprint must include a timeline of key events that happen at that location during the day.
*   **Location Roster:**
    *   **The Oakhaven Town Square:** The central hub of the village, where many of the day's key events unfold.
        *   **Key Landmarks:** The central clock tower (which is stuck), the market stalls, the village well, the statue of the town's founder.
        *   **Primary Inhabitants:** Villagers, merchants, children playing.
        *   **Available Goods & Services:** Market goods (which reset every day).
        *   **Timeline of Events:** 9 AM: Market opens. 12 PM: The central mystery event occurs. 3 PM: A town festival begins. 6 PM: The market closes.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Mayor gives the same speech every day at 3 PM." "The blacksmith always argues with the baker at 10 AM." "Old Man Hemlock is always seen staring at the clock tower just before noon."
        *   **Sensory Details:** Sight (Quaint buildings, colorful market stalls, happy villagers), Sound (The chatter of a crowd, children laughing, festival music), Smell (Fresh bread, flowers, livestock).
    *   **The Whispering Willow:** An ancient tree on the outskirts of town, rumored to have magical properties and connected to the loop.
        *   **Key Landmarks:** The tree itself, a hidden hollow at its base, a ring of strange mushrooms, a lover's carving on the trunk.
        *   **Primary Inhabitants:** Birds, squirrels, a potential dryad or nature spirit.
        *   **Available Goods & Services:** Rare herbs, a place for quiet contemplation.
        *   **Timeline of Events:** 11 AM: A young couple always meets here. 4 PM: The tree's shadow aligns with the entrance to a hidden location. Midnight: The tree whispers secrets.
        *   **Embedded Plot Hooks & Rumors (x3):** "They say the tree is older than the village itself." "The Chronomancer used a branch from the tree for their ritual." "If you answer the tree's riddle, it will show you a vision."
        *   **Sensory Details:** Sight (A massive, ancient willow; dappled sunlight; strange mushrooms), Sound (The rustle of leaves, birdsong, a faint whispering), Smell (Damp earth, old wood, grass).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome within a single loop.
*   **Triggers:**
    *   **IF:** A player tells an NPC a piece of information they shouldn't know.
    *   **THEN:** The NPC reacts with confusion or fear for the rest of the day, potentially altering their daily routine in a minor but significant way.
    *   **IF:** The players prevent the central mystery event (e.g., the murder) from happening.
    *   **THEN:** The loop does not break. Instead, generate a new, unexpected consequence later in the day, indicating that the event was a symptom, not the cause, of the loop.
    *   **IF:** The players manage to convince Old Man Hemlock of the time loop.
    *   **THEN:** His fragmented memories coalesce. He reveals a key piece of information about the day the loop started, but the mental strain causes him to have a heart attack at 5 PM, creating a new problem for the players to solve in future loops.
    *   **IF:** The players acquire a key item during a loop.
    *   **THEN:** The item disappears at the start of the next day. However, the players now know how to acquire that item and can plan to retrieve it again as part of a larger, multi-step plan.
    *   **IF:** The players successfully solve the central mystery and confront the Chronomancer.
    *   **THEN:** Generate a final, climactic encounter where the players must use all their accumulated knowledge of the day's events to corner the Chronomancer and perform the specific action required to break the loop before the day resets one last time.
