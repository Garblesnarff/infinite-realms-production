### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Crimson Masquerade**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** A magical curse, a mind-altering melody, sweeps through a major city, forcing its populace to dance until they die. The players must investigate the source of this "Dancing Plague," uncovering a hidden cult that is using the mass exhaustion and death as a grand ritual to weaken the veil to the Abyss. They must stop the music before the entire city dances itself into oblivion.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of the city and its relationship with festivals and revelry.
    *   Write the story of the forgotten Demon Lord of endless, agonizing revelry that the cult worships.
    *   Describe the magical theory behind the "Melody of Madness" and how it infects the mind.
    *   Explain the nature of the Abyssal Veil and how the ritual is weakening it.
    *   Detail a past event in the city where a magical plague or mass hysteria occurred.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The City Watch** (Major)
        *   **Goals:** To maintain order and stop the chaos.
        *   **Hierarchy:** A standard city guard structure, but overwhelmed and ineffective against the magical plague.
        *   **Public Agenda:** To quarantine the afflicted and find a medical or mundane solution.
        *   **Secret Agenda:** The captain of the watch is secretly taking bribes from the cult to steer the investigation away from them.
        *   **Assets:** The authority of the law, a large but ill-equipped force of guards, the city's prisons.
        *   **Relationships:** Initially dismissive of the players, but can become allies if the players provide results.
    *   **The Cult of the Final Dance** (Major)
        *   **Goals:** To complete their grand ritual and summon their demonic patron.
        *   **Hierarchy:** A secretive cult led by a charismatic high priest, with cells hidden throughout the city.
        *   **Public Agenda:** To encourage revelry and celebrate the city's festival spirit.
        *   **Secret Agenda:** To use the cursed melody to dance the entire city to death, using the psychic energy to open a portal to the Abyss.
        *   **Assets:** The cursed melody, hidden focal points for the ritual, fanatical followers who hide in plain sight.
        *   **Relationships:** The primary antagonists, viewing the players as killjoys trying to stop the ultimate party.
    *   **The College of Bards** (Minor)
        *   **Goals:** To understand and counteract the Melody of Madness.
        *   **Hierarchy:** A scholarly institution of lore-masters and master musicians.
        *   **Public Agenda:** To preserve musical history and theory.
        *   **Secret Agenda:** To capture the Melody of Madness for study, seeing it as a unique and powerful magical artifact, even if it is dangerous.
        *   **Assets:** Deep knowledge of musical theory and magical acoustics, soundproofed archives, powerful counter-sonics.
        *   **Relationships:** A potential ally for the players, but their academic curiosity can make them reckless.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Maestro Valerius:** The charismatic and insane leader of the Cult of the Final Dance.
    *   **Captain Thorne:** The corrupt and overwhelmed captain of the City Watch.
    *   **Loremaster Elara:** The head of the College of Bards, who is fascinated by the magical properties of the melody.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Manic, dancing citizen (victim)"
    *   "Undercover Cultist"
    *   "Frustrated City Guard"
    *   "Aloof Bardic Scholar"
    *   "Lesser Demonic Manifestation (Creature)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Festival Square:** The epicenter of the dancing plague, a once-joyous square now a scene of chaotic, non-stop revelry.
        *   **Key Landmarks:** The central fountain, the bandstand (now silent), the various food stalls (now abandoned), the makeshift infirmary for exhausted dancers.
        *   **Primary Inhabitants:** Hundreds of afflicted dancers, a few overwhelmed healers, undercover cultists egging on the dancers.
        *   **Available Goods & Services:** None. This is a disaster zone.
        *   **Potential Random Encounters (x5):** A dancer collapses from exhaustion, a fight breaks out between frustrated guards and manic dancers, a cultist tries to magically enhance the dancers' stamina, a character fails a saving throw and is compelled to dance for one minute, a planar rift briefly opens, showing a glimpse of the Abyss.
        *   **Embedded Plot Hooks & Rumors (x3):** "The melody seems strongest near the old clock tower." "Some of the dancers are whispering the name of a demon lord." "The city's healers are running out of supplies."
        *   **Sensory Details:** Sight (A swirling mass of bodies, expressions of ecstatic pain, discarded finery), Sound (The maddening, unheard melody (a psychic hum), the scuffing of thousands of feet, pained groans), Smell (Sweat, dust, a faint, sickly sweet scent).
    *   **The Hidden Cult Sanctum:** A secret location where the cultists are broadcasting the melody, likely in a place with good acoustics like an abandoned theater or bell tower.
        *   **Key Landmarks:** The magical amplifier for the melody, the sacrificial altar, the portal to the Abyss, the prison for those who resist the melody.
        *   **Primary Inhabitants:** The cult's high priest, elite cultist guards, bound demons.
        *   **Available Goods & Services:** None. This is the enemy stronghold.
        *   **Potential Random Encounters (x5):** A patrol of cultist guards, a magical ward that deafens the party, the party finds a captured city guard who can help them, the high priest begins to address his followers, the portal to the Abyss pulses, releasing a wave of fear.
        *   **Embedded Plot Hooks & Rumors (x3):** "The melody is powered by a powerful, captured fey." "The high priest is not a true believer, but a demon in disguise." "There is a counter-melody hidden in the College of Bards that can disrupt the ritual."
        *   **Sensory Details:** Sight (Dark, enclosed space; demonic symbols; a vibrating, magical artifact), Sound (The Melody of Madness at its absolute peak, chanting), Smell (Incense, blood, ozone).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** A player fails a Wisdom saving throw against the Melody of Madness.
    *   **THEN:** The player is compelled to dance for one round, moving erratically and suffering a level of exhaustion. Their movement provokes opportunity attacks.
    *   **IF:** The players take too long to identify the source of the curse.
    *   **THEN:** The Planar Bleeding worsens. Generate more frequent and more dangerous demonic manifestations in the city. The DC for saving throws against the melody increases.
    *   **IF:** The players successfully create a "zone of silence" around a group of dancers.
    *   **THEN:** The dancers collapse, freed from the melody's influence but suffering from multiple levels of exhaustion. This proves the curse is sonic/magical, but also alerts the cult to the players' interference.
    *   **IF:** The players expose Captain Thorne's corruption to the City Watch.
    *   **THEN:** The Watch is thrown into chaos. Some guards may join the players, but others will brand them as criminals, making it harder to move through the city.
    *   **IF:** In the finale, the players fail to stop the ritual.
    *   **THEN:** The portal to the Abyss opens fully. The campaign shifts from a mystery to a desperate, city-wide survival horror against a demonic invasion.
