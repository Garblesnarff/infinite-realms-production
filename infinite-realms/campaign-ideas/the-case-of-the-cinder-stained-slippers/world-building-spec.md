### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Case of the Cinder-Stained Slippers**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** In the perpetually twilit, rain-slicked city of Everafter, the players are hard-boiled private eyes. Hired by the vapid Prince Charmington IV, they must investigate a series of bizarre crimes where the only calling card is a single, cinder-stained glass slipper. They must navigate a world of crooked dwarves, magic-dealing godmothers, and socialite princesses to solve the case before the Royal Ball becomes a crime scene.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the founding of Everafter and how the various fairy-tale characters came to live there.
    *   Write the "true" story of Cinderella's rise to power, from scullery maid to ruthless Glass Baroness.
    *   Describe the criminal history of the Big Bad Wolf and the circumstances of his "reform."
    *   Explain the magical mechanics of the Fairy Godmother's protection racket.
    *   Detail the political structure of Everafter under the rule of the Charmington dynasty.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Grimm & Gritty Detective Agency (The Players)** (Minor)
        *   **Goals:** To solve the case, get paid, and survive the city's corruption.
        *   **Hierarchy:** A small, independent agency.
        *   **Public Agenda:** We find the truth, for a price.
        *   **Secret Agenda:** To expose the rot at the heart of the city's "happily ever after" facade.
        *   **Assets:** A run-down office, a network of underworld informants, a cynical worldview.
        *   **Relationships:** Hired by the Royal Family; viewed with suspicion by the City Guard; rivals with other P.I.s.
    *   **The Godmother Syndicate** (Major)
        *   **Goals:** To control all illicit magic and favors in the city.
        *   **Hierarchy:** Led by the Fairy Godmother, with a crew of ogre enforcers.
        *   **Public Agenda:** To provide magical assistance to those in need.
        *   **Secret Agenda:** To run a magical protection racket, ensuring that no one achieves their dreams without her getting a cut.
        *   **Assets:** A monopoly on wish-granting magic, powerful enforcers, blackmail material on half the city.
        *   **Relationships:** A primary antagonist, who sees the players as a threat to her business.
    *   **The Glass Conglomerate** (Major)
        *   **Goals:** To maintain its monopoly on the glass industry, from slippers to castles.
        *   **Hierarchy:** A corporation ruthlessly managed by its CEO, the Glass Baroness Cinderella.
        *   **Public Agenda:** To provide high-quality glass products to the citizens of Everafter.
        *   **Secret Agenda:** To crush all competition and acquire the magical formula for unbreakable glass, currently held by the Dwarf Miners' Guild.
        *   **Assets:** Immense wealth, corporate lawyers, high-tech security, a private army of glass golems.
        *   **Relationships:** A rival to the Godmother Syndicate; sees the players as potential pawns or threats.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Prince Charmington IV:** The handsome, vain, and oblivious client.
    *   **Cinderella, the Glass Baroness:** The cold, calculating, and ruthless former scullery maid, now a corporate titan.
    *   **"Big Bad" Wolf:** The gruff, cynical, and world-weary bouncer and informant.
    *   **The Fairy Godmother:** The smiling, seemingly benevolent, and utterly ruthless head of a magical crime syndicate.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Crooked King's Guard Knight"
    *   "Gossiping Socialite Princess"
    *   "Gnome Union Worker"
    *   "Ogre Enforcer (Creature)"
    *   "Fast-talking Gingerbread Man Snitch"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Crooked Man:** A shady tavern where deals are made and secrets are sold, run by the Crooked Man himself.
        *   **Key Landmarks:** The bar (manned by the Big Bad Wolf), the corner booth where informants whisper, the back room for high-stakes card games, the dartboard with a picture of the Prince.
        *   **Primary Inhabitants:** Criminals, informants, off-duty guards, cynical fairy-tale characters.
        *   **Available Goods & Services:** Strong drinks, unreliable information, a chance to lose your money.
        *   **Potential Random Encounters (x5):** A bar brawl breaks out, an informant offers a cryptic clue for a price, a crooked guard tries to intimidate the party, the party spots a key suspect meeting with a rival, the Big Bad Wolf shares a piece of unsolicited, cynical wisdom.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Gingerbread Man knows who's been buying up all the cinder in the city." "The Godmother's ogres collect her debts here every week." "Cinderella's stepsisters are deep in debt to the owner."
        *   **Sensory Details:** Sight (Dim lighting, smoke-filled air, shady figures in trench coats), Sound (Low jazz music, clinking glasses, hushed, tense conversations), Smell (Stale beer, cheap perfume, desperation).
    *   **The Glass Tower:** The corporate headquarters of the Glass Baroness, Cinderella. A marvel of modern, magical architecture.
        *   **Key Landmarks:** The lobby with a giant glass slipper statue, the executive offices, the high-security design lab, the rooftop helipad.
        *   **Primary Inhabitants:** Corporate executives, stressed-out designers, glass golem security guards.
        *   **Available Goods & Services:** Glass products of all kinds (not for sale to walk-ins).
        *   **Potential Random Encounters (x5):** A security patrol of glass golems, the party is mistaken for a rival design team, an alarm is triggered, the party finds a disgruntled employee willing to talk, Cinderella herself makes a surprise appearance.
        *   **Embedded Plot Hooks & Rumors (x3):** "Cinderella has a secret vault where she keeps her most valuable designs." "One of the stepsisters has been seen meeting with the Godmother." "The slippers used in the crimes are flawed prototypes from this tower."
        *   **Sensory Details:** Sight (Gleaming glass surfaces, minimalist design, panoramic city views), Sound (The quiet hum of technology, the chime of elevators, the echo of footsteps), Smell (Glass cleaner, sterile air).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players successfully connect two clues on the Clue Board.
    *   **THEN:** A "Moment of Insight" is granted. Generate a new, specific line of questioning the players can use on a key NPC, which will reveal a new clue.
    *   **IF:** The players fail to intimidate a witness during a "Press the Witness" encounter.
    *   **THEN:** The witness's Composure score increases. They become hostile to the party and may provide false information to the City Guard about them.
    *   **IF:** The players present irrefutable evidence of the Godmother's protection racket to the City Guard.
    *   **THEN:** The Guard is forced to act, but the Godmother retaliates by calling in the Prince's debts, putting the party's client in a compromised position.
    *   **IF:** The players discover that Cinderella is being blackmailed by her stepsister.
    *   **THEN:** They can choose to use this information to force Cinderella to cooperate, or they can help her, earning a powerful but ruthless ally.
    *   **IF:** The players fail to identify the killer before the Royal Ball.
    *   **THEN:** The killer attempts to assassinate the Prince during the ball. Generate a chaotic combat encounter in a crowded ballroom, where the players must protect the Prince while trying to capture the killer.
