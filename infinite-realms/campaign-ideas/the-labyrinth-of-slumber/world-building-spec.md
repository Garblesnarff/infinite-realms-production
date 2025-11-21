### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Labyrinth of Slumber**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise. The world must be surreal, psychological, and operate on dream-logic.
*   **Content:** A magical sleeping sickness, the "Somnus Plague," has trapped the kingdom's citizens in a collective dream. The players, as "Dream-Walkers," must project their minds into this Labyrinth of Slumber. They must navigate a bizarre, ever-shifting landscape of shared desires and nightmares to find the plague's source—a powerful, grieving child psychic—and awaken the sleepers before they are lost forever.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the nature of the Dream-Walkers. Is their ability magical, psionic, or something else?
    *   Write the history of Prince Alaric, his relationship with his mother, and the tragedy that caused his grief.
    *   Describe the "rules" of the Labyrinth of Slumber. How does belief shape reality within it?
    *   Explain the nature of the Sandman and the Bogeyman as natural functions of the collective unconscious.
    *   Detail a past, smaller-scale incident of a Somnus Plague and how it was resolved.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Dream-Walkers (The Players)** (Major)
        *   **Goals:** To find the source of the Somnus Plague and awaken the sleepers.
        *   **Hierarchy:** A small, specialized team.
        *   **Public Agenda:** To rescue the kingdom from the plague.
        *   **Secret Agenda:** To survive the psychological dangers of the dreamscape and not lose their own minds.
        *   **Assets:** The ability to enter the dream, their waking-world skills, and any Psychic Resonances they bring with them.
        *   **Relationships:** Guided by the Sandman; hunted by the Bogeyman.
    *   **The Prince's Subconscious** (Major)
        *   **Goals:** To protect Prince Alaric from further emotional pain.
        *   **Hierarchy:** A single, powerful, and fractured consciousness.
        *   **Public Agenda:** None.
        *   **Secret Agenda:** To keep the Prince (and therefore the entire kingdom) asleep forever, believing the waking world is too painful.
        *   **Assets:** The ability to shape the dreamscape, create powerful nightmare constructs, and weaponize emotions.
        *   **Relationships:** The primary antagonist, but not truly malevolent, only protective and grieving.
    *   **The Dream Natives** (Minor)
        *   **Goals:** To maintain the natural state of the dreamscape.
        *   **Hierarchy:** A loose collection of sentient dreams and concepts, with the Sandman as a key figure.
        *   **Public Agenda:** To observe and interact with dreamers.
        *   **Secret Agenda:** To purge the Prince's overwhelming influence (the "plague") from the dreamscape, even if it means destroying the minds of the sleepers to do so.
        *   **Assets:** A deep understanding of dream-logic, the ability to move freely through the dream, control over natural dream phenomena.
        *   **Relationships:** An ambiguous faction that may help or hinder the players, depending on what best serves the dreamscape's balance.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **The Sandman:** The whimsical, cryptic, and powerful native dream-entity that guides the party.
    *   **The Bogeyman:** A relentless, unkillable manifestation of collective fear that hunts the party.
    *   **Prince Alaric:** The lonely, grieving, and immensely powerful child psychic who is the unwitting cause of the plague.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Manifestation of Anxiety (Creature)"
    *   "Helpful Memory-Fragment (Guide)"
    *   "Rigid, Authoritarian Dream-Guard (Creature)"
    *   "Living Metaphor (Creature)"
    *   "Monstrous Living Toy (Creature)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Sea of Lost Memories:** A vast ocean where dreamers' forgotten memories wash up on the shore as smooth, glass-like pebbles.
        *   **Key Landmarks:** The Shore of First Kisses, the Isle of Forgotten Names, the Whirlpool of Trauma, a shipwreck made from a forgotten promise.
        *   **Primary Inhabitants:** Memory-draining sirens, echoes of past selves, sentient regrets.
        *   **Available Goods & Services:** Lost memories that can be experienced, providing clues or psychic damage.
        *   **Potential Random Encounters (x5):** A player finds one of their own forgotten memories, a storm of painful memories rolls in, a message in a bottle from another Dream-Walker washes ashore, a friendly memory-fragment offers to trade secrets, the Bogeyman is seen walking on the water in the distance.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Prince's happiest memory of his mother is on the Isle of Forgotten Names." "You can build a raft from happy memories to sail the sea safely." "The Sandman cannot enter the Whirlpool of Trauma."
        *   **Sensory Details:** Sight (A calm, glassy sea; shimmering pebbles; distant, hazy islands), Sound (The gentle lapping of waves, faint whispers of forgotten conversations), Smell (Salt, rain, and a scent unique to a specific memory).
    *   **The Library of Possibilities:** A library where every book is a story of a life a dreamer could have lived.
        *   **Key Landmarks:** The Section of Unfulfilled Ambitions, the Wing of Alternate Histories, a book that is still being written, the Librarian (a being made of stories).
        *   **Primary Inhabitants:** Living stories, grammar-correcting golems, the ghosts of abandoned choices.
        *   **Available Goods & Services:** The ability to briefly experience an alternate life, providing new skills or perspectives.
        *   **Potential Random Encounters (x5):** A book opens and tries to pull a player in, the party is attacked by a manifestation of a character's self-doubt, a story escapes its book and runs rampant, the Librarian asks for help finding a misplaced plot point, the party finds a book detailing a future where the nightmare wins.
        *   **Embedded Plot Hooks & Rumors (x3):** "The book of the Prince's life is here, but the final chapters are a nightmare." "The key to defeating the Bogeyman is written in a book that has no ending." "The Nightmare Architect has been seen redacting books here."
        *   **Sensory Details:** Sight (Endless shelves, books of all shapes and sizes, words floating in the air), Sound (The rustle of millions of pages, the quiet murmur of narration), Smell (Old paper, ink, dust).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** A player fails a Reality Check saving throw.
    *   **THEN:** Generate a minor, personal nightmare for that player. They are briefly separated from the party in a pocket dimension representing one of their own fears, and must overcome it to return.
    *   **IF:** The players use the "Impose Belief" mechanic to create a solution to a puzzle.
    *   **THEN:** The dreamscape adapts. The next puzzle they face will be designed by the Prince's subconscious to be resistant to that kind of logic, forcing the players to find new, creative solutions.
    *   **IF:** The players manage to temporarily defeat or evade the Bogeyman.
    *   **THEN:** The collective fear in that dream-region lessens, making the environment less hostile. However, the Bogeyman returns in the next region, now possessing a new ability based on how the players defeated it last time.
    *   **IF:** The players find and experience the Prince's happiest memory of his mother.
    *   **THEN:** They can use this Psychic Resonance as a weapon against nightmare creatures, or as a key to reach the Prince in the heart of his nightmare.
    *   **IF:** In the finale, the players choose to attack the psychic projection of Prince Alaric.
    *   **THEN:** The dreamscape itself turns violently against them. The Prince's grief manifests as a powerful, kaiju-sized monster, and the only way to win is to defeat this creature, which will cause permanent psychological damage to the Prince in the waking world.