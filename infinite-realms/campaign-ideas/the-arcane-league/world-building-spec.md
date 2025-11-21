### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Arcane League**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** In the modern metropolis of Silverport, the most popular sport is Aether-Ball, a high-octane, magical game. The players are a new, underdog team of Aether-Ball players trying to win the Arcane League championship. They must train, compete, and navigate the treacherous world of professional sports, including rivalries, corporate sponsors, and the magical underworld.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history and rules of Aether-Ball. How did it evolve into a professional sport?
    *   Write the story of a legendary Aether-Ball player from the past.
    *   Describe the city of Silverport and how magic is integrated into its modern infrastructure.
    *   Explain the corporate structure of the Arcane League and its relationship with team owners and sponsors.
    *   Detail the history of the rivalry between the Silverport Griffins and the Blackwood Ravens.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Silverport Griffins (The Players)** (Major)
        *   **Goals:** To win the Arcane League championship.
        *   **Hierarchy:** A team of players led by their coach, "Grizzly" Adams.
        *   **Public Agenda:** To play hard and win for the city of Silverport.
        *   **Secret Agenda:** To survive the season, pay their bills, and expose the corruption in the league.
        *   **Assets:** Their unique skills, a rundown training facility, a washed-up but brilliant coach.
        *   **Relationships:** Fierce rivals with the Blackwood Ravens; financially dependent on their shady sponsor, Mr. Sterling.
    *   **The Blackwood Ravens** (Major)
        *   **Goals:** To win the championship and maintain their undefeated record.
        *   **Hierarchy:** A professional team with a star player, Vex.
        *   **Public Agenda:** To be the best, most dominant team in the league.
        *   **Secret Agenda:** Their star player, Vex, is secretly using a dangerous magical artifact to enhance his abilities.
        *   **Assets:** Top-tier training facilities, a massive fan base, a ruthless playing style.
        *   **Relationships:** The primary rivals of the Griffins.
    *   **Sterling Syndicate** (Major)
        *   **Goals:** To use the league for money-laundering and illegal betting.
        *   **Hierarchy:** A criminal organization led by the team's sponsor, Mr. Sterling.
        *   **Public Agenda:** To be a legitimate and respected corporate sponsor.
        *   **Secret Agenda:** To fix games and ensure their sponsored teams perform exactly as needed for their betting schemes.
        *   **Assets:** Vast wealth, a network of criminals and black-market alchemists, political influence.
        *   **Relationships:** The secret antagonists of the campaign, manipulating the league from behind the scenes.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Coach "Grizzly" Adams:** The team's gruff, cynical, and alcoholic coach, a former star player with a tragic past.
    *   **Vex:** The arrogant, charismatic, and supremely talented star player of the rival Blackwood Ravens.
    *   **Mr. Sterling:** The team's smooth, charming, and utterly ruthless sponsor, who is secretly a crime boss.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Ambitious Sports Reporter"
    *   "Die-hard Griffins Fan"
    *   "Corrupt League Referee"
    *   "Black-Market Potion Dealer"
    *   "Veteran Aether-Ball Player"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Aether-Dome:** The massive, state-of-the-art stadium where the Silverport Griffins play their home games.
        *   **Key Landmarks:** The playing field (with glowing goal-posts), the locker rooms, the VIP boxes, the massive holographic scoreboard.
        *   **Primary Inhabitants:** Players, fans, referees, media, vendors.
        *   **Available Goods & Services:** Merchandise stands, food and drink, betting windows (legal and illegal).
        *   **Potential Random Encounters (x5):** A post-game interview with a reporter, a confrontation with the rival team in the tunnel, a fan asks for an autograph, a scout from another team is seen taking notes, a magical mishap occurs with the arena's equipment.
        *   **Embedded Plot Hooks & Rumors (x3):** "They say the owner of the Ravens has a controlling stake in the referee's guild." "The championship trophy is a powerful magical artifact in its own right." "A player once died on this field; their ghost is said to haunt the locker room."
        *   **Sensory Details:** Sight (Bright lights, cheering crowds, team colors, magical energy), Sound (The roar of the crowd, the crackle of magic, the announcer's voice), Smell (Popcorn, sweat, ozone).
    *   **The Gilded Griffin Casino:** A high-class casino and nightclub owned by Mr. Sterling, which serves as a front for his criminal activities.
        *   **Key Landmarks:** The main casino floor, the VIP lounge (where shady deals are made), the secret back rooms, the Aether-Ball-themed bar.
        *   **Primary Inhabitants:** High-rollers, criminals, socialites, Mr. Sterling's enforcers.
        *   **Available Goods & Services:** Gambling, expensive drinks, information (for a price).
        *   **Potential Random Encounters (x5):** The party spots Vex meeting with a known criminal, a bar fight breaks out, Mr. Sterling invites the party to a "private" meeting, the party is accused of cheating at a card game, a police raid occurs.
        *   **Embedded Plot Hooks & Rumors (x3):** "Mr. Sterling is laundering money through the team." "The alchemist who sells performance-enhancing potions meets his clients here." "The casino is built on a place of powerful magical convergence."
        *   **Sensory Details:** Sight (Flashing lights, expensive decor, well-dressed patrons, watchful security), Sound (The clatter of chips, lounge music, hushed conversations), Smell (Cigar smoke, expensive perfume, greed).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players win a match through exceptional teamwork.
    *   **THEN:** The team's Chemistry score increases. Generate a short scene of the players celebrating and bonding, unlocking a new team-based special move they can use in the next game.
    *   **IF:** The players are caught using an illegal performance-enhancing potion.
    *   **THEN:** The team is suspended for several games, their reputation plummets, and they must complete a difficult side-quest to be reinstated into the league.
    *   **IF:** The players successfully expose the criminal organization fixing games.
    *   **THEN:** The league is thrown into chaos. Several teams are disqualified. The Griffins are hailed as heroes, but they have made powerful enemies in the criminal underworld.
    *   **IF:** The players refuse to throw the championship game for Mr. Sterling.
    *   **THEN:** Mr. Sterling places a massive bet against them and sends his enforcers to injure the players before the game, leading to a pre-game combat encounter.
    *   **IF:** The players win the championship.
    *   **THEN:** Generate an epilogue where the team must deal with the pressures of fame, including lucrative (and ridiculous) endorsement deals, intense media scrutiny, and a new set of high-powered rivals for the next season.
