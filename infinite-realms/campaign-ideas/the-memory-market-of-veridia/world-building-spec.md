### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Memory Market of Veridia**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise. The tone is dystopian, philosophical, and noir-inspired.
*   **Content:** In the neon-lit metropolis of Veridia, memories are a tangible commodity that can be extracted, bought, and sold. The players are "Memory Runners," specialists who navigate this dangerous market. When a new, highly addictive memory-drug called "Echo" hits the streets, causing users to lose their own memories, the players must uncover its source and confront the powerful forces seeking to control the very essence of self.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the discovery of memory-extraction technology and the establishment of the Memory Market.
    *   Write a history of the social stratification caused by memory commerce (the wealthy Curated vs. the memory-poor Drifters).
    *   Describe the process of memory extraction, implantation, and the creation of a "Memory Fragment."
    *   Explain the philosophy of The Curator and the purpose of the Archive of Pure Thought.
    *   Detail the rise of the Memory Guild and its transformation into a powerful corporate-criminal entity.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Memory Runners (The Players)** (Minor)
        *   **Goals:** To survive the dangerous market, complete their jobs, and uncover the truth behind "Echo."
        *   **Hierarchy:** A small, independent crew.
        *   **Public Agenda:** To be discreet couriers and investigators in the memory trade.
        *   **Secret Agenda:** To protect the concept of genuine memory from total commodification.
        *   **Assets:** Their specialized skills, a network of underworld contacts, the ability to navigate the Memory Market.
        *   **Relationships:** In conflict with the Memory Guild and the Architect of Echo.
    *   **The Memory Guild** (Major)
        *   **Goals:** To control and monopolize the entire Memory Market.
        *   **Hierarchy:** A powerful syndicate led by a shadowy council, with enforcers like Silas "The Eraser" Vane.
        *   **Public Agenda:** To regulate the memory trade for the safety and prosperity of all.
        *   **Secret Agenda:** To control the supply of "Echo" and use it to eliminate rival factions and gain leverage over the city's elite.
        *   **Assets:** Control of legitimate memory clinics, a private army of enforcers, immense wealth.
        *   **Relationships:** A primary antagonist, viewing the players as a threat to their control.
    *   **The Curated Elite** (Major)
        *   **Goals:** To maintain their lives of curated bliss and acquire the rarest and most powerful memories.
        *   **Hierarchy:** The wealthy upper class of Veridia.
        *   **Public Agenda:** To be patrons of the arts and paragons of culture.
        *   **Secret Agenda:** To ensure the Memory Market continues to serve their interests, even if it means exploiting the poor.
        *   **Assets:** Vast wealth, political influence, access to the best legal and illegal memories.
        *   **Relationships:** The primary customers of the Memory Market and a source of jobs and intrigue for the players.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **The Curator, Elias Thorne:** The ancient, melancholic, and philosophical guardian of the Archive of Pure Thought.
    *   **Silas "The Eraser" Vane:** The ruthless, efficient, and memory-less enforcer for the Memory Guild.
    *   **The Architect of Echo:** The brilliant, manipulative, and secretly tragic creator of the "Echo" drug.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Desperate citizen selling a cherished memory"
    *   "Wealthy client looking for an exotic experience"
    *   "Memory-addled "Echo" victim"
    *   "Black market memory-splicer"
    *   "Armored Guild Enforcer"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Memory Market:** A bustling, multi-tiered bazaar where memories are openly traded in glowing vials.
        *   **Key Landmarks:** The stalls of memory-brokers, the "Echo Den" for sampling the drug, the Guild's regulatory checkpoint, a holographic board displaying the fluctuating prices of emotions.
        *   **Primary Inhabitants:** Memory-brokers, buyers, sellers, tourists, Guild enforcers.
        *   **Available Goods & Services:** Memories of all kinds (skills, experiences, emotions), memory-extraction services, illicit "Echo" drug.
        *   **Potential Random Encounters (x5):** A seller has a breakdown after selling a core memory, a deal goes bad and a psychic fight erupts, the party is offered a memory that contains a dangerous secret, a Guild patrol begins shaking down vendors, a victim of Echo goes on a rampage.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Curator is looking for runners to retrieve 'pure' memories before they hit the market." "The best memory-splicers can combine memories to create new skills." "The Architect of Echo tests their new batches in the Echo Dens before releasing them."
        *   **Sensory Details:** Sight (A kaleidoscope of glowing vials, holographic ads for perfect vacations, desperate and wealthy faces), Sound (The murmur of a thousand simultaneous sales pitches, the hum of extraction devices), Smell (Ozone, antiseptic, a strange mix of countless perfumes).
    *   **The Mind-Forge:** The hidden, high-tech laboratory where Echo is produced.
        *   **Key Landmarks:** The central memory-processor, the vats of raw psychic effluent, the holding cells for "donors," the Architect's personal research terminal.
        *   **Primary Inhabitants:** The Architect of Echo, lab technicians, high-tech security drones, mindless test subjects.
        *   **Available Goods & Services:** None. This is the enemy stronghold.
        *   **Potential Random Encounters (x5):** A security drone patrol, a containment breach releases raw, unprocessed memories, the party finds the Architect's personal logs, a test subject escapes, the Architect initiates a system purge to erase all evidence.
        *   **Embedded Plot Hooks & Rumors (x3):** "Echo is made from the traumatic memories of unwilling donors." "The Architect is trying to erase a single, specific memory from the city's collective unconscious." "There is a flaw in Echo that can be exploited to reverse its effects."
        *   **Sensory Details:** Sight (Sterile white walls, glowing blue conduits, vats of shimmering liquid, complex machinery), Sound (The hum of powerful computers, the whir of medical equipment, muffled cries), Smell (Antiseptic, ozone, a faint, sweet chemical scent).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** A player uses a Memory Fragment to gain a skill.
    *   **THEN:** They have that skill for a limited time, but must make a Wisdom saving throw or gain a temporary "Psychic Scar" in the form of a flaw from the memory's original owner.
    *   **IF:** A player chooses to sell one of their own core memories.
    *   **THEN:** They gain a significant boon (e.g., a large sum of money, a powerful favor), but they permanently lose that memory. Generate a short scene where they encounter a person or place from that memory and feel nothing.
    *   **IF:** The players successfully expose the Memory Guild's connection to the Echo drug.
    *   **THEN:** The Guild's public reputation plummets, and a gang war breaks out in the Memory Market as rivals try to take over their territory. The Guild, in turn, puts a massive bounty on the players' heads.
    *   **IF:** The players choose to work with The Curator.
    *   **THEN:** He provides them with rare, pure memories that can act as powerful tools or antidotes to Psychic Scars, but he also asks them to retrieve memories that are culturally significant, even if it means stealing them from their current owners.
    *   **IF:** In the finale, the players discover the Architect's tragic motivation.
    *   **THEN:** Generate a moral choice. Do they help the Architect achieve their goal of erasing a single, catastrophic memory from the world's history, even if it means destabilizing the present, or do they stop them, forcing the Architect to live with their trauma forever?