### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Sunken Kingdom of Zancig**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise. The tone is a psychological thriller that blurs the line between reality and a world of pure thought.
*   **Content:** Based on the real-life Zancigs telepathy act, the players are individuals who have accidentally "tuned in" to the Zancig Frequency, gaining access to the Noosphere—a shared mind-scape. This newfound psychic ability makes them targets for parasitic ideas and forgotten archetypes that hunger to cross over into the real world. The players must learn to navigate this "Sunken Kingdom" of thought to defend their reality and their own sanity.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the "true" story of Julius and Agnes Zancig and their discovery of the Noosphere.
    *   Write a philosophical and scientific explanation of the Noosphere. What is it, and how does it relate to the Material Plane?
    *   Describe the different types of "Ideomorphs" that inhabit the Noosphere (e.g., benign concepts, parasitic ideas, powerful archetypes).
    *   Explain the concept of an "Anchor" and how Ideomorphs use them to manifest in the real world.
    *   Detail a historical account of a major event that was secretly caused by a powerful Ideomorph manifesting in the real world.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Newly Awakened (The Players)** (Minor)
        *   **Goals:** To understand and control their new psychic abilities, and to survive the attention of the Ideomorphs.
        *   **Hierarchy:** A small, disparate group of individuals, likely without a formal leader.
        *   **Public Agenda:** To live their normal lives.
        *   **Secret Agenda:** To protect the real world from the threats of the Noosphere without losing their minds.
        *   **Assets:** Their nascent psychic abilities, a fragile connection to each other through the Zancig Frequency.
        *   **Relationships:** Hunted by parasitic Ideomorphs; viewed as potential tools or threats by other factions.
    *   **The Parasitic Ideas** (Major)
        *   **Goals:** To find suitable anchors in the real world, manifest physically, and feed on the emotions and thoughts of mortals.
        *   **Hierarchy:** A chaotic ecosystem of predator and prey, with no formal structure.
        *   **Public Agenda:** None.
        *   **Secret Agenda:** To consume and replicate.
        *   **Assets:** The ability to manipulate the Noosphere, the power to infect mortal minds, the fact that most people are unaware of their existence.
        *   **Relationships:** The primary antagonists, viewing the players as both a meal and a potential gateway.
    *   **The Archetypes** (Major)
        *   **Goals:** To maintain the balance and structure of the Noosphere.
        *   **Hierarchy:** A loose council of powerful, ancient concepts (e.g., The Warrior, The Sage, The Trickster).
        *   **Public Agenda:** To exist as the fundamental building blocks of thought.
        *   **Secret Agenda:** To test the players and determine if they are worthy of their power, or if they are a threat to the Noosphere that must be eliminated.
        *   **Assets:** Immense power within the Noosphere, the ability to shape the mind-scape at will, a deep understanding of reality.
        *   **Relationships:** An ambiguous, god-like faction that can be a source of great power or a devastating enemy.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Anxiety:** A recurring Ideomorph that stalks the players, manifesting as a physical monster of shifting, indistinct form.
    *   **The Librarian:** A powerful Archetype that guards the "Library of Every Thought," who may offer knowledge for a price.
    *   **A Forgotten God:** An Ideomorph of a deity that no longer has any worshippers, desperate to find a new anchor in the real world.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "A living riddle (Ideomorph)"
    *   "A manifestation of a player's self-doubt (Ideomorph)"
    *   "A predatory meme (Ideomorph)"
    *   "A helpful concept like 'Curiosity' (Ideomorph)"
    *   "A person whose mind has been infected by a parasitic idea"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Noosphere:** The shared mind-scape, a fluid and symbolic landscape.
        *   **Key Landmarks:** The Sea of Memories, the Forest of Forgotten Ideas, the Mountains of Logic, the Graveyard of Dead Gods.
        *   **Primary Inhabitants:** Ideomorphs of all kinds.
        *   **Available Goods & Services:** Knowledge, concepts, ideas (all of which can be dangerous).
        *   **Potential Random Encounters (x5):** The landscape shifts to reflect a player's current emotional state, the party is attacked by a manifestation of a collective fear (e.g., fear of spiders), they find a lost memory, a living story tries to draw them into its narrative, a powerful Archetype appears to test them.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Zancigs didn't just discover the Noosphere; they built a safe haven within it." "There is a concept so dangerous that the Archetypes have it imprisoned." "You can find the answer to any question in the Library of Every Thought, but you might not survive the experience."
        *   **Sensory Details:** Varies wildly. The landscape is a metaphor. The Sea of Memories might smell like a specific, personal scent from a player's past. The Mountains of Logic might be unnervingly silent.
    *   **An Anchored Location (e.g., a haunted house):** A place in the real world where a powerful Ideomorph has manifested.
        *   **Key Landmarks:** The object acting as the Anchor, rooms that defy physical space, manifestations of the Ideomorph's nature (e.g., in a house anchored by "Paranoia," all the doors have extra locks).
        *   **Primary Inhabitants:** The Ideomorph, any humans it is tormenting, physical manifestations of its thoughts.
        *   **Available Goods & Services:** None. This is a dungeon.
        *   **Potential Random Encounters (x5):** A door opens into the Noosphere, a player is confronted by a manifestation of their own fear, the Anchor pulses with psychic energy, the Ideomorph tries to make a bargain with a player, the house's layout changes when no one is looking.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Anchor can only be destroyed by a specific, symbolic act." "The person who lives here invited the Ideomorph in." "The Ideomorph is not evil, just lonely."
        *   **Sensory Details:** A blend of the mundane and the impossible. The house might look normal, but the air feels heavy, and there are whispers just at the edge of hearing.

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** A player suffers mental damage during "Mental Combat."
    *   **THEN:** They temporarily lose access to a skill or memory. Generate a short, descriptive scene of this concept unraveling from their mind.
    *   **IF:** The players successfully identify and cleanse an Anchor.
    *   **THEN:** The hostile Ideomorph is banished from the real world, and the location returns to normal. The players gain a deeper understanding of their powers, perhaps unlocking a new psychic ability.
    *   **IF:** The players are confronted by a manifestation of their own self-doubt and fail to defeat it in Mental Combat.
    *   **THEN:** They gain a new, permanent flaw related to that doubt, which imposes a mechanical penalty on certain actions until they can overcome it through roleplaying and character development.
    *   **IF:** The players choose to make a deal with a powerful but dangerous Ideomorph (e.g., a Forgotten God).
    *   **THEN:** They gain a powerful boon or piece of information, but they now act as that Ideomorph's Anchor, and it can begin to influence their actions and the world around them.
    *   **IF:** The players discover that a weaponized conspiracy theory is attempting to manifest in the real world.
    *   **THEN:** The campaign shifts. The players must not only fight the Ideomorph in the Noosphere but also race to debunk the theory in the real world, as every new believer makes the Ideomorph stronger.
