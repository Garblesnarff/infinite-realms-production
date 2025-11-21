### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Ashen Blight**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** In a world worn down by war and famine, a mysterious plague known as the Ashen Blight ravages the remote barony of Vyrnholm. The affliction doesn't just kill; it twists and corrupts all life, turning people into monsters and forests into graveyards. The players are drawn into this decay, tasked with finding a cure or a way to survive before the blight consumes everything, only to discover it is a deliberate curse spread by a death cult.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of the Barony of Vyrnholm before the blight. What were its people and economy like?
    *   Write the full story of the forgotten god Nalthur and why its temple was sunken and abandoned.
    *   Describe the dogma and origins of the Ashen Disciples death cult.
    *   Explain the magical nature of the Ashen Blight. How does it corrupt life, and what is its ultimate purpose?
    *   Detail the story of Baron Valerius Thorne's family and their connection to the sunken temple.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Oakhaven Survivors** (Minor)
        *   **Goals:** To survive the blight and protect their village.
        *   **Hierarchy:** Loosely led by the town healer, Elara Meadowlight.
        *   **Public Agenda:** To find a cure and fortify their village against the horrors of the Weeping Wood.
        *   **Secret Agenda:** Elara is secretly studying forbidden texts, willing to risk dark magic for a cure.
        *   **Assets:** A small group of determined villagers, a crumbling barricade, Elara's healing knowledge.
        *   **Relationships:** Desperate for outside help; suspicious of strangers.
    *   **The Ashen Disciples** (Major)
        *   **Goals:** To spread the Ashen Blight and summon the blight's patron entity.
        *   **Hierarchy:** A death cult led by the charismatic Baron Valerius Thorne.
        *   **Public Agenda:** To offer a path to peace and acceptance in a dying world.
        *   **Secret Agenda:** To complete a dark ritual in the Sunken Temple of Nalthur to transform the world.
        *   **Assets:** Fanatical cultists, Blighted beasts, the Baron's wealth and influence, a hidden temple.
        *   **Relationships:** The primary antagonists, actively spreading the plague and eliminating all who oppose them.
    *   **The Greyport Underworld** (Minor)
        *   **Goals:** To profit from the chaos caused by the blight.
        *   **Hierarchy:** A network of gangs and criminals, with key figures like the Skitter-kin chief, Marrow.
        *   **Public Agenda:** None. They operate in the shadows.
        *   **Secret Agenda:** To control the black market for supplies and information, selling to both survivors and the cult.
        *   **Assets:** A network of informants, control of the city's Underside, a willingness to do anything for a price.
        *   **Relationships:** Neutral and opportunistic, willing to work with or against the players for the right price.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Elara Meadowlight:** A pragmatic and exhausted hedge healer in Oakhaven, desperately seeking a cure.
    *   **Ser Kaelan the Disgraced:** A cynical, alcoholic fallen knight in Greyport who seeks redemption.
    *   **Baron Valerius Thorne:** The charismatic and ruthless noble who secretly leads the Ashen Disciples, his handsome face an illusion hiding his own corruption.
    *   **The Voice of Nalthur:** The ancient, whispering cosmic entity of decay that is the source of the blight.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Desperate Oakhaven Villager"
    *   "Fanatical Ashen Disciple Cultist"
    *   "Shrewd Skitter-kin (Rat-man) Thug"
    *   "Blighted Beast (Creature)"
    *   "Blighted Treant (Creature)"
    *   "Corrupt Greyport City Guard"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Weeping Wood:** A supernaturally tainted forest where the trees weep black sap and the wildlife is twisted and hostile.
        *   **Key Landmarks:** The Blighted Treant, a grove of whispering, skeletal trees, a river running thick with black sludge, the ruins of a druid's circle.
        *   **Primary Inhabitants:** Blighted beasts (wolves, bears), animated dead trees, will-o'-wisps drawn to decay.
        *   **Available Goods & Services:** Rare, blight-resistant herbs; poisonous fungi.
        *   **Potential Random Encounters (x5):** A pack of Blighted wolves, a sudden fog that carries the blight's corruption, the party finds the corpse of a cultist carrying a strange map, a ghostly apparition from before the blight appears, a section of the forest animates and attacks.
        *   **Embedded Plot Hooks & Rumors (x3):** "The heart of the forest is protected by a powerful, ancient guardian." "The cultists have a secret path through the woods to Greyport." "The sap of the trees can be used to create a potent poison."
        *   **Sensory Details:** Sight (Sickly green-black trees, thick fog, twisted animal corpses), Sound (Unnatural silence, the snap of twigs, wet, rasping coughs), Smell (Decay, rot, damp earth).
    *   **The Sunken Temple of Nalthur:** An ancient complex to a forgotten god of decay, now partially submerged in a murky swamp.
        *   **Key Landmarks:** The Inner Sanctum, the Chamber of Echoes, the flooded library, the sacrificial altar.
        *   **Primary Inhabitants:** Undead guardians, waterlogged zombies, cultists performing rituals, the Avatar of Nalthur.
        *   **Available Goods & Services:** None. This is the final dungeon.
        *   **Potential Random Encounters (x5):** A magical trap is triggered, a group of undead guardians rises from the water, the party overhears a conversation between cultists, a psychic wave of despair washes over the party, a valuable but cursed relic is found.
        *   **Embedded Plot Hooks & Rumors (x3):** "The final ritual requires a sacrifice of pure innocence." "Baron Thorne seeks to become the blight's ultimate vessel." "There is a secret way to reverse the ritual, but it requires a great sacrifice."
        *   **Sensory Details:** Sight (Crumbling, moss-covered stone; murky water; flickering ritual candles), Sound (Dripping water, distant chanting, the groans of the undead), Smell (Stagnant water, decay, incense).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** A player gains a Blight Corruption point.
    *   **THEN:** Generate a minor physical or mental side effect (e.g., a weeping sore, disadvantage on a social check, a disturbing nightmare that reveals a cryptic clue).
    *   **IF:** The players fail to defend Oakhaven's barricades in Act I.
    *   **THEN:** The hamlet is overrun. Key NPCs like Elara are either killed or forced to flee, becoming desperate refugees the party may encounter later. The blight spreads faster across the barony.
    *   **IF:** The players choose to make a deal with Marrow and the Skitter-kin in Greyport.
    *   **THEN:** They gain a reliable source of underworld information and a secret route through the city, but they are now indebted to a criminal faction and may be asked to perform a morally questionable task later.
    *   **IF:** The players successfully infiltrate the Baron's masquerade and steal evidence without being detected.
    *   **THEN:** They gain a significant advantage and know the temple's location early. The Baron becomes paranoid and increases security, making the final confrontation more difficult but the path there clearer.
    *   **IF:** In the final confrontation, the players choose to make the sacrifice required to stop the blight ritual.
    *   **THEN:** The blight is halted, but the cost is immense and personal. Generate an epilogue scene detailing the emotional and psychological fallout for the party and the world.
