### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Anomalous Continent of Xylos**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise. The world must feel surreal, dreamlike, and subtly unsettling.
*   **Content:** After centuries of being shrouded in a magical storm, the continent of Xylos is now accessible. The players are part of the first major expedition to a land where reality is fluid: gravity shifts, colors are heard, and time flows differently. They must chart its impossible landscapes, catalog its bizarre life forms, and uncover the source of the anomalies before their own minds and bodies are irrevocably altered.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. The answers should be strange, esoteric, and raise more questions than they answer.
*   **Prompts:**
    *   Detail the theories behind the magical storm that once shrouded Xylos. Was it a natural phenomenon or a deliberate quarantine?
    *   Write the fragmented history of the previous, failed civilization that tried to understand Xylos, as found in the Echoing Ruins.
    *   Describe the nature of the "Xylosian Echo." Is it a single entity, the collective consciousness of the continent, or something else entirely?
    *   Explain the scientific and philosophical principles behind a world where reality is fluid.
    *   Detail the known effects of long-term exposure to Xylos's anomalies on sentient minds.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The First Expedition** (Major)
        *   **Goals:** To chart, catalog, and understand the continent of Xylos.
        *   **Hierarchy:** Led by a council comprising the head of research (Professor Thorne) and the head of security (Captain Valerius).
        *   **Public Agenda:** Scientific discovery and peaceful exploration.
        *   **Secret Agenda:** Different sub-factions exist: the scientists want to harness the anomalies, the security team wants to weaponize them, and a corporate sponsor wants to exploit them.
        *   **Assets:** A fortified base camp, advanced research equipment, a small security force.
        *   **Relationships:** The primary viewpoint faction, in direct opposition to the continent's will.
    *   **The Xylosian Echo** (Major)
        *   **Goals:** Incomprehensible to mortals. May involve observation, testing, or absorption of the intruders.
        *   **Hierarchy:** A single, distributed consciousness that is the continent itself.
        *   **Public Agenda:** None.
        *   **Secret Agenda:** None. Its actions are overt but its motivations are alien.
        *   **Assets:** The entire continent, control over reality and physics within its borders.
        *   **Relationships:** The primary antagonist, treating the expedition as an interesting but ultimately irrelevant phenomenon.
    *   **The Lost** (Minor)
        *   **Goals:** To survive and find a way to reverse their transformations.
        *   **Hierarchy:** A loose, desperate band of survivors from previous, failed expeditions.
        *   **Public Agenda:** To be left alone.
        *   **Secret Agenda:** To steal the expedition's technology in the hopes of escaping Xylos.
        *   **Assets:** Deep, firsthand knowledge of the continent's dangers; strange, anomaly-induced abilities.
        *   **Relationships:** Paranoid and hostile towards the new expedition, whom they see as future rivals for resources.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Professor Aris Thorne:** The brilliant, obsessive lead scientist, who is slowly being driven mad by the very anomalies he studies.
    *   **Captain Valerius, the Pragmatist:** The grizzled, no-nonsense security chief who is terrified of a repeat of his last disastrous mission to Xylos.
    *   **The Xylosian Echo:** The alien, incomprehensible intelligence of the continent itself, which may communicate through environmental shifts or psychic projections.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Eager Young Researcher"
    *   "Cynical, Over-armed Security Guard"
    *   "Mutated Survivor from a Past Expedition"
    *   "Creature that Exists in a Different Dimension (Creature)"
    *   "Sentient, Ambulatory Plant-life (Creature)"
    *   "Creature Made of Pure Sound (Creature)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections. Emphasize the surreal and reality-bending nature of each location.
*   **Location Roster:**
    *   **The Chromatic Jungles:** Forests where plants glow with impossible colors and emit strange, melodic sounds.
        *   **Key Landmarks:** The Grove of Singing Flora, the River of Liquid Light, a tree that grows its fruit in the shape of visitors' memories, a field of gravity-inverting moss.
        *   **Primary Inhabitants:** Creatures made of woven light, camouflaged predators that mimic the sounds of the flora, sentient swarms of insects.
        *   **Available Goods & Services:** Bizarre fruits with unpredictable effects, unique alchemical reagents.
        *   **Potential Random Encounters (x5):** A player's voice is transformed into a cascade of colors, a creature communicates through music, the jungle shifts its layout, a sudden silence falls as a major predator approaches, a player develops synesthesia.
        *   **Embedded Plot Hooks & Rumors (x3):** "The heart of the jungle contains a plant that can solidify reality locally." "The Lost have learned to interpret the songs of the flora." "The colors are a language, and they are screaming a warning."
        *   **Sensory Details:** Sight (Impossible colors, glowing plants, shifting light), Sound (A constant, melodic hum; complex, alien birdsong; the sound of color), Smell (Alien pollens, sweet nectar, something like ozone).
    *   **The Echoing Ruins:** Ancient ruins that seem to exist in multiple timelines simultaneously.
        *   **Key Landmarks:** The Plaza of a Thousand Pasts (where different historical versions of the plaza flicker in and out of existence), the Library of Fading Knowledge, the Unchanging Obelisk.
        *   **Primary Inhabitants:** Chronal Echos (ghosts of the former inhabitants), Time-Displaced Creatures, guardians that exist outside of time.
        *   **Available Goods & Services:** Fragmented, often contradictory, historical records.
        *   **Potential Random Encounters (x5):** The party is briefly shifted into a past or future version of the ruins, a player sees an echo of themselves, a creature from another time period attacks, a vital piece of equipment is aged to dust, a message from the past appears on a wall.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Unchanging Obelisk is the anchor that keeps the ruins from collapsing entirely." "The original inhabitants did not die; they transcended time." "The source of the anomalies is buried beneath the ruins."
        *   **Sensory Details:** Sight (Flickering, transparent buildings; figures fading in and out; distorted perspectives), Sound (A cacophony of different eras; whispers from the past; sudden, jarring silences), Smell (Dust, ozone, the scent of rain on stone even when it is dry).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The expedition's Reality Flux tracker reaches a new threshold.
    *   **THEN:** Generate a new, major Reality Anomaly affecting the entire region (e.g., gravity reverses for one hour, the color spectrum inverts, spoken words manifest as physical objects).
    *   **IF:** A player accumulates a high number of Anomaly Points.
    *   **THEN:** The player must make a Wisdom saving throw. On a failure, they gain a new, permanent, and bizarre physical or mental trait (e.g., their skin becomes translucent, they can only speak in questions).
    *   **IF:** The players attempt to use their own magic to counter one of Xylos's anomalies.
    *   **THEN:** Generate an unpredictable magical feedback loop. The player's spell may be twisted into a new, strange form, or it may be amplified to a terrifying degree.
    *   **IF:** The players manage to communicate with the Xylosian Echo.
    *   **THEN:** The Echo responds not with words, but by altering reality to reflect its answer, creating a new, surreal environment that the players must interpret as a clue.
    *   **IF:** In the final confrontation, the players choose to destroy the Heart of Anomaly.
    *   **THEN:** Xylos does not return to normal. Instead, its reality shatters completely. Generate a desperate escape sequence as the continent dissolves into pure chaos behind the players.
