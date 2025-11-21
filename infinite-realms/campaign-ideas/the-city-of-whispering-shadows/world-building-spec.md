### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The City of Whispering Shadows**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** In the gaslit metropolis of Nocturne, every citizen has a sentient shadow. The players are investigators drawn into a series of terrifying crimes where victims are left as emotionless shells, their shadows violently stolen. They must hunt a killer who can move through darkness, bargain with a black market that trades in stolen shadows, and confront a being from the Plane of Shadow before the city is consumed by its own darkness.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the origin of the sentient shadows of Nocturne. Was it a magical event, a curse, or a natural evolution?
    *   Write the history of the relationship between citizens and their shadows. How has society adapted?
    *   Describe the Plane of Shadow in this setting and its connection to Nocturne.
    *   Explain the story of Kael, the Man with No Shadow. How was he exiled, and what are the rules of his existence?
    *   Detail the rise of the Penumbra and the creation of the shadow market.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Umbral Guard (The Players)** (Minor)
        *   **Goals:** To solve the shadow-thefts and bring the killer to justice.
        *   **Hierarchy:** A new, small agency or independent group of investigators.
        *   **Public Agenda:** To stop the killings.
        *   **Secret Agenda:** To understand the nature of their own increasingly independent shadows.
        *   **Assets:** Their investigative skills, their unique connection to their own shadows, the trust of a few key officials.
        *   **Relationships:** In conflict with the shadow-thief; navigating the corruption of the City Watch; wary of the Penumbra.
    *   **The Shadow Market** (Major)
        *   **Goals:** To profit from the trade of stolen shadows.
        *   **Hierarchy:** A collective of high-society elites, led by the enigmatic Penumbra.
        *   **Public Agenda:** To be influential members of Nocturne's elite.
        *   **Secret Agenda:** To use the stolen shadows to replace their own guilt-ridden ones, achieving a form of emotional immortality.
        *   **Assets:** Immense wealth, political connections, a secret auction house, enforcers.
        *   **Relationships:** The primary drivers of the central conspiracy; they see the shadow-thief as a supplier and the players as a threat to their business.
    *   **Kael's Brood** (Minor)
        *   **Goals:** To steal enough shadows for Kael to complete his transformation into a powerful new entity.
        *   **Hierarchy:** A single being, Kael, and the shadow creatures he creates.
        *   **Public Agenda:** None.
        *   **Secret Agenda:** To gather enough stolen essence to anchor Kael permanently to the Material Plane.
        *   **Assets:** The ability to travel through shadows, control over Shade-Hounds, a sanctum made of solidified shadow.
        *   **Relationships:** The primary antagonist and killer; sees the Shadow Market as customers and the players as obstacles.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **The Penumbra:** The smooth, amoral, and mysterious broker of the shadow market, who is secretly a collective consciousness.
    *   **Detective Malachi Slate:** A grizzled, cynical, and just detective on the city watch, secretly investigating the case against orders.
    *   **Kael, the Man with No Shadow:** The cold, sorrowful, and terrifying antagonist from the Plane of Shadow.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Hollowed, emotionless victim"
    *   "Corrupt City Watch officer"
    *   "Wealthy, guilt-ridden socialite"
    *   "Shade-Hound (Creature)"
    *   "Sentient, feral shadow (Creature)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Umbral Bazaar:** A secret market that only exists in the city's darkest shadows, where forbidden goods are traded.
        *   **Key Landmarks:** The stall of the shadow-tailor, the whisper-broker's corner, the entrance to the Penumbra's auction house, a fountain of liquid shadow.
        *   **Primary Inhabitants:** Shadow-mancers, informants, dealers in illegal magic, wealthy clients in masks.
        *   **Available Goods & Services:** Stolen shadows, magical poisons, information, shadow-forged weapons.
        *   **Potential Random Encounters (x5):** A deal goes bad and a shadow-fight breaks out, an informant offers a clue for a price, the party is mistaken for a rival crew, a patrol of Shade-Hounds passes through, the Penumbra makes a public announcement.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Penumbra isn't one person, but many." "The killer, Kael, is the Penumbra's sole supplier." "You can buy a shadow that has memories of a specific skill, and gain that skill for a short time."
        *   **Sensory Details:** Sight (Deep shadows, flickering, minimal light from glowing fungi or crystals, masked figures), Sound (Constant whispering, the rustle of unseen things), Smell (Damp earth, ozone, a cold, metallic scent).
    *   **The Obsidian Cathedral:** Kael's sanctum, a church built from solidified shadow-stuff on a demi-plane of perpetual twilight.
        *   **Key Landmarks:** The Altar of Stolen Selves, the Font of Emptiness, the pews where hollowed victims sit, the portal to the Plane of Shadow.
        *   **Primary Inhabitants:** Kael, his most powerful Shade-Hounds, the psychic echoes of his victims.
        *   **Available Goods & Services:** None. This is the final dungeon.
        *   **Potential Random Encounters (x5):** The walls shift and change, a player's shadow is temporarily stolen, a psychic echo of a victim pleads for help, Kael appears as a projection to taunt the party, a portal to the Plane of Shadow briefly opens, showing a terrifying landscape.
        *   **Embedded Plot Hooks & Rumors (x3):** "Kael can be harmed by true sunlight." "He is trying to build himself a new shadow from the ones he has stolen." "His first victim was the one who exiled him from his home plane."
        *   **Sensory Details:** Sight (Shifting black walls, architecture that defies geometry, a profound lack of light), Sound (A deafening silence, the sound of your own breathing, a sorrowful hum), Smell (Nothing. A complete absence of scent).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** A player uses a Shadow Manipulation ability.
    *   **THEN:** Their shadow becomes slightly more independent. Generate a short, descriptive scene where the shadow performs a small, autonomous action (e.g., points at a hidden clue, recoils from an NPC).
    *   **IF:** The party is in an area of Bright Light.
    *   **THEN:** Their shadow abilities are weakened or disabled. Shadow creatures in the area take damage or are unable to manifest.
    *   **IF:** The players successfully expose the Penumbra's identity to the public.
    *   **THEN:** The shadow market is thrown into chaos. The high-society members turn on each other, creating a new power vacuum, but Kael loses his primary client and becomes more desperate and aggressive in his thefts.
    *   **IF:** The players manage to restore the shadow of a feral victim.
    *   **THEN:** The victim regains their senses and provides a key piece of information about their attacker, Kael, but the psychic feedback from the restoration gives one player a form of temporary madness.
    *   **IF:** In the finale, the players choose to help Kael create a new shadow for himself instead of destroying him.
    *   **THEN:** Generate a complex skill challenge to build a new shadow from raw shadow-stuff and a fragment of the players' own shadows. Success pacifies Kael, who becomes a powerful, morally ambiguous ally. Failure causes him to explode, releasing all the stolen shadows as hostile specters across the city.
