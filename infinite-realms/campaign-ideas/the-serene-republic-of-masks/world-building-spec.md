### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Serene Republic of Masks**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** In the canal-laced city-state of Venza, the month-long "Festival of Masks" guarantees absolute anonymity. The players are agents of a secret society, the "Silent Hand," tasked with uncovering a conspiracy to assassinate the Doge during the festival. They must trade swords for secrets and armor for masks, navigating a treacherous world of masquerade balls and political backstabbing to save the republic.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of Venza and the founding of its republican government.
    *   Write the story of the Festival of Masks. Why was it created, and what are its ancient rules?
    *   Describe the origins and purpose of the Silent Hand secret society.
    *   Explain the political structure of Venza, including the roles of the Doge, the noble houses, and the merchant guilds.
    *   Detail a past conspiracy or coup attempt in Venza's history.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Silent Hand (The Players)** (Minor)
        *   **Goals:** To protect the Republic by uncovering and neutralizing the conspiracy.
        *   **Hierarchy:** A clandestine network of spies, led by the enigmatic spymaster, Lady Annalisa.
        *   **Public Agenda:** None. They operate through various personas.
        *   **Secret Agenda:** To maintain the delicate balance of power in Venza, ensuring no single faction becomes too powerful.
        *   **Assets:** A network of informants, safe houses, and the ability to create and manage multiple identities.
        *   **Relationships:** Secretly loyal to the idea of the Republic, if not its current leaders. Adversaries to the conspirators.
    *   **The Restorationists (The Conspirators)** (Major)
        *   **Goals:** To assassinate the Doge, dissolve the merchant guilds' power, and restore the nobility to absolute rule.
        *   **Hierarchy:** A secret council of nobles and military officers, led by the respected Captain Valerius of the City Guard.
        *   **Public Agenda:** To be loyal servants of the Republic.
        *   **Secret Agenda:** To stage a military coup during the Grand Masquerade.
        *   **Assets:** Influence over the City Guard, a hired mercenary company, the loyalty of the old noble houses.
        *   **Relationships:** The primary antagonists, who see the current government as corrupt and weak.
    *   **The Merchant Guilds** (Major)
        *   **Goals:** To maintain their economic power and influence over the Doge.
        *   **Hierarchy:** A coalition of powerful merchant princes.
        *   **Public Agenda:** To promote trade and the prosperity of Venza.
        *   **Secret Agenda:** To further erode the power of the nobility and turn the Republic into a corporate oligarchy.
        *   **Assets:** Vast wealth, control of trade and shipping, the ability to hire mercenaries and spies.
        *   **Relationships:** The primary political rivals of the noble houses; unaware they are being targeted by the conspiracy.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **The Lying Widow (Lady Annalisa):** The party's ruthless and enigmatic spymaster.
    *   **Captain Valerius:** The seemingly honorable Captain of the City Guard and secret leader of the conspiracy.
    *   **The Gilded Fool:** The whimsical, chaotic, and mysterious exiled brother of the Doge, who acts as a wild card.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Ambitious Merchant Prince"
    *   "Decadent, Scheming Noble"
    *   "Gossip-mongering Courtier"
    *   "Masked Assassin"
    *   "Gondolier Informant"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **A Grand Masquerade Ball:** A lavish party hosted by one of Venza's powerful factions.
        *   **Key Landmarks:** The ballroom floor, the balcony overlooking the canals, the private garden for secret conversations, the buffet table.
        *   **Primary Inhabitants:** Masked nobles, wealthy merchants, artists, spies, assassins.
        *   **Available Goods & Services:** Fine wine, exotic foods, gossip, secrets, opportunities for seduction or blackmail.
        *   **Potential Random Encounters (x5):** A rival challenges a player's persona, a player overhears a crucial secret, a romantic entanglement begins, a player is slipped a coded message, a dead body is discovered in the garden.
        *   **Embedded Plot Hooks & Rumors (x3):** "The host of this ball is secretly funding the conspiracy." "The Gilded Fool is expected to make an appearance." "A master forger is here, and can be hired to duplicate the Doge's seal."
        *   **Sensory Details:** Sight (A swirl of colorful, elaborate masks and costumes; glittering chandeliers), Sound (An orchestra playing, the murmur of hundreds of conversations, laughter), Smell (Expensive perfume, wine, flowers).
    *   **The Labyrinth of Canals:** The watery streets of Venza, perfect for clandestine travel.
        *   **Key Landmarks:** The Bridge of Sighs, a hidden smuggler's cove, a foggy intersection of canals, the entrance to the city's sewer system.
        *   **Primary Inhabitants:** Gondoliers, smugglers, city guard patrols, lovers on a romantic ride.
        *   **Available Goods & Services:** Discreet transportation, smuggled goods.
        *   **Potential Random Encounters (x5):** The party's gondola is ambushed, they witness a body being dumped in a canal, a city guard patrol demands to see their papers, a thick fog rolls in, reducing visibility to zero, they are followed by a mysterious, lone figure in another gondola.
        *   **Embedded Plot Hooks & Rumors (x3):** "There are secret passages that connect the canals to the dungeons of the Doge's Palace." "The gondoliers have their own spy network." "The conspirators are using the sewers to move weapons."
        *   **Sensory Details:** Sight (Dark water, crumbling architecture, flickering lanterns), Sound (The lapping of water, the cry of a distant gull, the song of a gondolier), Smell (Brackish water, damp stone, refuse).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** A player's Persona reaches a Notoriety of 5 with a faction.
    *   **THEN:** That Persona is compromised. Generate a new complication where that faction actively works against the player when they are using that mask (e.g., guards will detain them on sight, merchants will refuse to deal with them).
    *   **IF:** The players spend Favors to gain an advantage.
    *   **THEN:** The NPC who granted the favor will later call upon the players to repay it, generating a new, unexpected side quest at an inconvenient time.
    *   **IF:** The players successfully steal the weapons shipment manifest from the merchant prince.
    *   **THEN:** They can use it to turn the Merchant Guilds against the conspirators. However, the merchant prince, now exposed, puts a massive bounty on the players' true identities, not just their personas.
    *   **IF:** The players fail to expose the conspiracy before the Grand Masquerade.
    *   **THEN:** The assassination attempt on the Doge occurs. The campaign shifts from a social stealth mystery to a chaotic urban combat scenario as the conspirators make their move.
    *   **IF:** In the finale, the players expose Captain Valerius as the leader of the conspiracy.
    *   **THEN:** The City Guard is thrown into disarray. Some remain loyal to Valerius, leading to a civil war within the guard itself. The players must escape the palace amidst the chaos.
