### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Fading Weave: Threads of Magic**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** Centuries after the Great Silence severed the world's connection to the arcane Weave, magic has become a dwindling resource, fading with each passing generation and leaving civilizations in ruins. The players are survivors in this dying world, initially struggling for personal survival but gradually drawn into a larger quest to understand and potentially reverse the Silence. As they journey across the scarred continent, they discover that the catastrophe wasn't natural but an intentional act by a powerful entity seeking to reshape reality. The players must balance immediate survival needs with the desperate hope of rekindling the Fading Weave, all while deciding whether magic's return would save their world or doom it to an even greater catastrophe.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the golden age of magic before the Great Silence and the society that flourished during that era.
    *   Write the history of the Great Silence itself - the signs, the catastrophe, and the immediate aftermath.
    *   Describe the evolution of magical decay and how it has changed both the landscape and surviving magical creatures.
    *   Explain the formation of survivor settlements and the various models of post-Silence governance.
    *   Detail the mutated creatures that emerged after the Silence and their behavioral patterns.
    *   Write about the "Weave Cults" - groups that worship or seek to harness the fading magical energy.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Weave Preservation Society** (Major)
        *   **Goals:** To study and preserve the last remnants of magic while searching for ways to rekindle the Weave.
        *   **Hierarchy:** Council of magical scholars and surviving mages from the pre-Silence era.
        *   **Public Agenda:** We will restore magic to the world and rebuild what was lost.
        *   **Secret Agenda:** To harness the Silence entity's power for controlled magical restoration.
        *   **Assets:** Magical artifacts, research facilities, network of magical sites.
        *   **Relationships:** Cooperative with magical researchers; cautious toward Silence worshippers.
    *   **The Silence Adaptation League** (Major)
        *   **Goals:** To help society adapt to a world without magic while preserving pre-Silence knowledge.
        *   **Hierarchy:** Council of engineers, scholars, and community leaders focused on mundane solutions.
        *   **Public Agenda:** Magic was a crutch - humanity will be stronger without it.
        *   **Secret Agenda:** To study the Silence entity for potential technological breakthroughs.
        *   **Assets:** Pre-Silence technology, engineering expertise, adaptation research.
        *   **Relationships:** Allied with mundane survivors; opposed to magical restoration efforts.
    *   **The Null Cult** (Minor)
        *   **Goals:** To embrace the Silence as a divine cleansing and eradicate all remaining magical energy.
        *   **Hierarchy:** Theocratic structure led by "Enlightened" individuals who have embraced the Silence.
        *   **Public Agenda:** The Silence was a blessing that will remake us all in its image.
        *   **Secret Agenda:** To accelerate the Silence's spread and become its heralds.
        *   **Assets:** Anti-magic technology, corrupted followers, hidden Silence sites.
        *   **Relationships:** Hostile toward all magical practitioners; seek to "enlighten" non-believers.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Elder Lirael Voss:** The pragmatic settlement leader who balances hope with harsh reality.
    *   **Kaelen the Shadow Weaver:** The corrupted mage who has adapted to the Silence.
    *   **The Null Cult Leader:** The entity herald who worships the Silence as a blessing.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Magical Researcher"
    *   "Adaptation Engineer"
    *   "Null Cultist"
    *   "Corrupted Creature"
    *   "Settlement Guard"
    *   "Weave Scholar"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Crystal Scar:** A massive chasm glowing with residual magical energy.
        *   **Key Landmarks:** The Central Pit, the Crystal Spires, the Energy Fields, the Research Camps.
        *   **Primary Inhabitants:** Magical researchers, corrupted creatures, energy-adapted survivors.
        *   **Available Goods & Services:** Rare magical crystals, energy samples, research data.
        *   **Potential Random Encounters (x5):** A crystal spire pulses with energy, a corrupted creature emerges, discovery of a magical artifact, an energy storm forces shelter, a researcher offers collaboration.
        *   **Embedded Plot Hooks & Rumors (x3):** "The scar is growing larger every year." "Some who enter the central pit never return." "The crystals can be used to predict magical events."
        *   **Sensory Details:** Sight (Shimmering crystal formations, glowing energy), Sound (Low humming energy, cracking crystals), Smell (Ozone, heated stone).
    *   **The Whispering Library:** A vast underground archive preserving pre-Silence knowledge.
        *   **Key Landmarks:** The Main Archive, the Restricted Section, the Research Stations, the Preservation Labs.
        *   **Primary Inhabitants:** Scholarly researchers, preservation experts, knowledge seekers.
        *   **Available Goods & Services:** Ancient texts, historical documents, research assistance.
        *   **Potential Random Encounters (x5):** An archive guardian activates, a document reveals a crucial discovery, discovery of forbidden knowledge, a researcher seeks collaboration, a preservation system fails.
        *   **Embedded Plot Hooks & Rumors (x3):** "The library contains knowledge from before the Silence." "Some books whisper secrets to those who listen." "The restricted section holds the key to restoring magic."
        *   **Sensory Details:** Sight (Ancient tomes, glowing preservation fields), Sound (Page turning, humming systems), Smell (Old paper, dust).
    *   **The Corrupted Wilds:** Areas where magic is abundant but twisted.
        *   **Key Landmarks:** The Crystal Forest, the Mutated River, the Energy Nexus, the Wild Settlements.
        *   **Primary Inhabitants:** Corrupted creatures, adapted survivors, energy researchers.
        *   **Available Goods & Services:** Mutated plants, energy sources, survival knowledge.
        *   **Potential Random Encounters (x5):** A corrupted creature migration, an energy storm approaches, discovery of a natural energy source, a survivor offers guidance, a mutated area reveals ancient ruins.
        *   **Embedded Plot Hooks & Rumors (x3):** "The wilds remember the old magic in strange ways." "Some corrupted areas are actually safer than they appear." "The energy nexus could be used to restore the Weave."
        *   **Sensory Details:** Sight (Twisted magical growths, glowing mutations), Sound (Strange animal calls, humming energy), Smell (Damp earth, unknown flowers).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players successfully restore a magical site.
    *   **THEN:** Magic returns to that area, creating new opportunities and dangers. Generate increased cult activity as they attempt to counter the restoration.
    *   **IF:** The players form an alliance with the Weave Preservation Society.
    *   **THEN:** They gain access to magical knowledge and safe havens. Generate scenarios where magical restoration conflicts with adaptation efforts.
    *   **IF:** The players acquire a significant magical artifact.
    *   **THEN:** Their magical abilities increase but they attract dangerous attention. Generate opportunities to study the artifact's properties.
    *   **IF:** The players help a settlement adapt to magic-less survival.
    *   **THEN:** Their reputation with adaptation groups grows. Generate scenarios where successful adaptation inspires other settlements.
    *   **IF:** The players embrace the Silence philosophy.
    *   **THEN:** They gain unique abilities but risk losing magical affinity. Generate scenarios where the Silence entity attempts to recruit them.
