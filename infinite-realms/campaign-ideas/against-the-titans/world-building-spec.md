### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**Against the Titans**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** In a world where civilization exists in the shadows of Titans—colossal monsters that are living forces of nature—the players are members of the elite Slayer's Guild. They are the only ones brave and foolish enough to hunt these city-destroying behemoths. Each arc of the campaign is a grand hunt, forcing the party to research their colossal prey, track it across vast territories, prepare the battlefield, and finally, engage in a multi-stage, epic battle against a creature the size of a mountain.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of the first Titan attacks and the near-collapse of civilization.
    *   Write the founding story of the Slayer's Guild and its first legendary hunt.
    *   Describe the biology and nature of the Titans. Are they natural creatures, magical beasts, or something else entirely?
    *   Explain the unique properties of Titan parts and why they are so valuable for crafting.
    *   Detail the history of a famous Titan that was defeated in the past and the legendary gear crafted from its remains.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Slayer's Guild** (Major)
        *   **Goals:** To protect civilization by hunting the most dangerous Titans.
        *   **Hierarchy:** Led by Guildmaster Valerius, with a council of veteran Slayers and department heads (Research, Smithing, etc.).
        *   **Public Agenda:** We are humanity's shield, the heroes who face the impossible.
        *   **Secret Agenda:** To maintain their monopoly on Titan-hunting and the immense wealth and political power that comes from it.
        *   **Assets:** The Guildhall, the Forges, a network of informants, the loyalty of the people.
        *   **Relationships:** Allied with most kingdoms out of necessity; rivals with any who would challenge their monopoly.
    *   **The Titanologists** (Minor)
        *   **Goals:** To study and understand the Titans, not just kill them.
        *   **Hierarchy:** A loose collective of academics led by Professor Arkwright.
        *   **Public Agenda:** To aid the Slayer's Guild with research and knowledge.
        *   **Secret Agenda:** To prevent the extinction of the Titans, believing they are a vital, albeit dangerous, part of the world's ecosystem.
        *   **Assets:** The Guild's library, a network of field researchers, forbidden knowledge.
        *   **Relationships:** Dependent on the Slayer's Guild for access and samples; secretly opposed to their ultimate mission.
    *   **Rival Slayer Crews** (Minor)
        *   **Goals:** To gain fame, glory, and wealth by taking on high-profile Titan contracts.
        *   **Hierarchy:** Independent crews, each with their own leader.
        *   **Public Agenda:** To be the best Slayers in the world.
        *   **Secret Agenda:** To sabotage other crews (including the players) to secure the most lucrative contracts.
        *   **Assets:** Their own gear, contacts, and unique hunting techniques.
        *   **Relationships:** Competitive and hostile towards other Slayer crews.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Guildmaster Valerius:** The grizzled, one-legged former Slayer who runs the Guild. He is a no-nonsense mentor haunted by the Titan that crippled him.
    *   **Professor Arkwright:** The eccentric, brilliant Titanologist who is more interested in studying Titans than killing them.
    *   **"Forge-Hand" Brynja:** The legendary dwarven smith who can craft gear from Titan parts, the last of her clan.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Ambitious Rival Slayer"
    *   "Terrified Village Elder"
    *   "Awe-Struck Young Scholar"
    *   "Cynical Guild Quartermaster"
    *   "Retired Slayer with a Tall Tale"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Slayer's Guildhall:** A massive fortress built from the bones of a long-dead Titan, serving as the campaign hub.
        *   **Key Landmarks:** The Great Hall (lined with trophies), The Forges, The Titanology Library, The Sparring Arena.
        *   **Primary Inhabitants:** Slayers, smiths, scholars, guild staff.
        *   **Available Goods & Services:** Accepting contracts, crafting gear, research facilities, training.
        *   **Potential Random Encounters (x5):** A bar brawl between rival crews, a demonstration of a new weapon, a scholar seeking help with a discovery, a summons from the Guildmaster, a rookie Slayer asking for advice.
        *   **Embedded Plot Hooks & Rumors (x3):** "Valerius has been seen staring at the skull of the Titan that took his leg." "Brynja is looking for a rare mineral to forge a masterpiece." "Arkwright is paying well for live samples of Titan parasites."
        *   **Sensory Details:** Sight (Massive bone architecture, roaring fires of the forge, maps of Titan sightings), Sound (Clang of hammers, roar of Slayers telling tales, sharpening of blades), Smell (Forge smoke, old books, monster viscera).
    *   **The Petramach's Path:** A wide swathe of destruction carved through plains and forests by the walking-mountain Titan.
        *   **Key Landmarks:** A pulverized forest, a half-crushed village, the Titan's massive footprints, a crystal-filled cavern (feeding ground).
        *   **Primary Inhabitants:** Displaced wildlife (angry Bulettes), scavengers, elemental parasites.
        *   **Available Goods & Services:** None. Pure wilderness.
        *   **Potential Random Encounters (x5):** A pack of displaced predators, a sudden rockslide caused by the Titan's tremors, a rival crew tracking the same beast, a lone survivor from a crushed caravan, a patch of valuable minerals exposed by the Titan.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Titan seems to be drawn to large deposits of crystal." "Legends say its underbelly is soft." "The parasites that live on it are vulnerable to thunder damage."
        *   **Sensory Details:** Sight (Crushed trees, giant tracks, shimmering crystals), Sound (Rumbling earth, cracking rock, wind howling across the plains), Smell (Dust, crushed pine, ozone).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players successfully harvest a rare component from a Titan (e.g., Petramach's Heartstone).
    *   **THEN:** Brynja can forge a unique piece of Legendary gear for them. Generate the stats and description for this item, designed to be effective against the next major Titan.
    *   **IF:** The players fail to topple the Petramach before it reaches the fortified city.
    *   **THEN:** Generate a new scenario: a desperate city defense. The party must now fight the Titan amidst collapsing walls and fleeing civilians, a much more chaotic and dangerous encounter.
    *   **IF:** The players ally with Professor Arkwright and choose to capture a Titan's offspring instead of killing it.
    *   **THEN:** The Slayer's Guild is furious and may revoke the party's membership. Generate a new plotline where the party is branded as renegades and must protect the young Titan from both the Guild and other threats.
    *   **IF:** The players discover Guildmaster Valerius's secret obsession with the Titan that crippled him.
    *   **THEN:** Generate a moral dilemma. The players can either help him on his quest for revenge, potentially endangering the Guild, or report him to the council, creating a political power struggle within the Guild.
