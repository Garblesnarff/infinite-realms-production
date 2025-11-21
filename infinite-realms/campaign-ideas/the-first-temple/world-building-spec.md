### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The First Temple**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** Based on the discovery of Göbekli Tepe, the players are hired to investigate a "haunted" mining operation that has accidentally unearthed the world's oldest temple. They soon discover it is not a temple, but an ancient, arcane prison for a world-destroying primordial entity. As the miners dig deeper, the prison's wards are failing, and the players must descend into the temple to reactivate them before the entity fully awakens.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of the Dawn War and the specific primordial entity imprisoned within the temple.
    *   Write the story of the temple's construction. Which ancient races collaborated to build it?
    *   Describe the arcane mechanics of the prison. How do the wards, guardians, and layout work together to contain the primordial?
    *   Explain why the temple was deliberately buried and its memory erased from the world.
    *   Detail the culture and motivations of the Dwarven Mining Guild that has discovered the temple.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Investigators (The Players)** (Major)
        *   **Goals:** To understand the nature of the threat, reactivate the prison's wards, and prevent the primordial from escaping.
        *   **Hierarchy:** An independent group of adventurers.
        *   **Public Agenda:** To investigate a haunted dig site for the mining guild.
        *   **Secret Agenda:** To save the world from a threat it doesn't know exists.
        *   **Assets:** Their skills, any lore they can uncover within the temple, and a growing sense of dread.
        *   **Relationships:** Initially employed by the Dwarven Mining Guild, but this relationship will become adversarial.
    *   **The Dwarven Mining Guild** (Major)
        *   **Goals:** To excavate the temple for riches and lost knowledge.
        *   **Hierarchy:** A corporate structure led by a greedy Guildmaster.
        *   **Public Agenda:** To conduct a legitimate archaeological and mining operation.
        *   **Secret Agenda:** To find the temple's rumored "heart"—a massive, priceless gem (which is actually the primordial's core).
        *   **Assets:** A large workforce, advanced mining equipment, a private security force.
        *   **Relationships:** The players' initial employer, but they become secondary antagonists as their greed conflicts with the need to stop the excavation.
    *   **The Awakened** (Minor)
        *   **Goals:** To aid the escape of their primordial master.
        *   **Hierarchy:** A small cult of maddened miners and elemental spirits, led by a foreman who first made psychic contact with the entity.
        *   **Public Agenda:** To sabotage the mining operation, appearing as simple Luddites.
        *   **Secret Agenda:** To disable the temple's remaining wards from within and perform a ritual to hasten the primordial's escape.
        *   **Assets:** Fanatical followers, the ability to communicate with and command the temple's corrupted elementals.
        *   **Relationships:** A hidden antagonist faction that will actively work against the players inside the temple.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Guildmaster Borin Stonebeard:** The greedy, short-sighted, and stubborn leader of the Dwarven Mining Guild.
    *   **Foreman Kael:** The first miner to touch the prison's core, now the maddened and charismatic leader of the Awakened cult.
    *   **The Primordial's Echo:** A psychic manifestation of the imprisoned entity, which appears in dreams and visions, tempting and threatening those within the temple.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Greedy Dwarf Miner"
    *   "Maddened Cultist"
    *   "Ancient Guardian Construct (Creature)"
    *   "Corrupted Earth Elemental (Creature)"
    *   "Twisted Wildlife (Creature)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Dig Site:** The sprawling mining operation surrounding the entrance to the First Temple.
        *   **Key Landmarks:** The Guildmaster's tent, the main excavation pit, the miners' barracks, the slag heaps where twisted creatures are seen.
        *   **Primary Inhabitants:** Dwarven miners, guild guards, worried local representatives.
        *   **Available Goods & Services:** Basic mining supplies, rumors, a place to rest (that is increasingly unsafe).
        *   **Potential Random Encounters (x5):** A mining machine goes haywire, a fight breaks out between miners driven mad by nightmares, a key section of the dig site collapses, a patrol of guild guards tries to restrict the party's access, a twisted creature emerges from the slag heaps and attacks.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Guildmaster is ignoring reports of madness from the lower levels." "Some of the miners have started a secret cult." "The strange carvings on the temple walls seem to shift when no one is looking."
        *   **Sensory Details:** Sight (A massive, open pit; scaffolding; dust), Sound (The constant clang of pickaxes, the roar of machinery, the grumbling of dwarves), Smell (Earth, rock dust, coal smoke).
    *   **The Chamber of Wards:** A key level within the temple, designed to channel and maintain the prison's magical energy.
        *   **Key Landmarks:** The central power conduit, a series of focusing crystals, the guardian construct barracks, a map of the temple's energy flows.
        *   **Primary Inhabitants:** Ancient guardian constructs, energy elementals, Awakened cultists attempting to sabotage the wards.
        *   **Available Goods & Services:** None. This is a dungeon level.
        *   **Potential Random Encounters (x5):** A ward fails, releasing a wave of chaotic energy; a guardian construct activates and challenges the party; the party finds the journal of one of the temple's original builders; a group of cultists is trying to shatter a focusing crystal; the Primordial's Echo manifests and offers the party power.
        *   **Embedded Plot Hooks & Rumors (x3):** "Reactivating the wards requires a specific sequence of rituals." "The guardian constructs are powered by the prison itself; weakening them weakens the prison." "There is a master control room that can realign the temple's energy flows."
        *   **Sensory Details:** Sight (Intricate glowing runes, massive crystals, complex machinery), Sound (A loud, constant hum of power; the crackle of magical energy), Smell (Ozone, a clean, sterile scent).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players take a long rest.
    *   **THEN:** The "Ticking Clock" advances. The Dwarven Mining Guild excavates a new section of the temple, weakening the wards further. Generate a new environmental effect on the outside world (e.g., a minor earthquake, a new type of twisted creature appears).
    *   **IF:** The players successfully present proof of the danger to the dwarven miners.
    *   **THEN:** A portion of the miners go on strike, slowing the excavation. Guildmaster Stonebeard hires mercenaries to replace them and becomes openly hostile to the players.
    *   **IF:** The players destroy a guardian construct instead of bypassing it.
    *   **THEN:** The energy from the construct is released, causing a temporary but significant weakening of the local ward. The Primordial's influence in that area increases, creating a new hazard or a more powerful monster.
    *   **IF:** The players manage to capture and interrogate Foreman Kael.
    *   **THEN:** He reveals the location of the central chamber but also triggers a psychic backlash from the primordial that permanently scars the mind of his interrogator.
    *   **IF:** In the finale, the players fail to reactivate the wards in time.
    *   **THEN:** The primordial does not fully escape. Instead, its consciousness breaks free and possesses the most powerful being it can find: Guildmaster Stonebeard. Generate a new final boss fight against a primordial-infused dwarf with the ability to shape earth and metal at will.