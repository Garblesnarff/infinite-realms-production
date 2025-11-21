### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Eldritch Slip**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** Based on the Philadelphia Experiment conspiracy, the players are hired to salvage a shipwreck but are instead drawn aboard "The Intrepid," a ghost ship permanently fused with the Ethereal Plane after a catastrophic teleportation spell failure. Trapped in the mists, they must navigate the spectral, shifting vessel, fight its ghostly crew, and repair the failed spell to escape before they become a permanent part of the ship's eternal, misty hell.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the history of the magical empire that built The Intrepid and their experiments with the "Phase Sail" spell.
    *   Write a log of the maiden voyage of The Intrepid, detailing the moments leading up to the spell failure.
    *   Describe the nature of the Ethereal Plane in this setting, including its native inhabitants and environmental hazards.
    *   Explain the magical theory behind the Phase Sail spell and what might have caused it to fail so catastrophically.
    *   Detail the story of the ship's captain and the archmage who designed the spell.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Salvage Crew (The Players)** (Major)
        *   **Goals:** To understand what happened, repair the Phase Sail spell, and escape the Ethereal Plane.
        *   **Hierarchy:** A small, independent crew of adventurers.
        *   **Public Agenda:** To salvage a shipwreck.
        *   **Secret Agenda:** To survive and not be driven mad by the horrors of the ship.
        *   **Assets:** Their wits, their gear, and any information they can piece together from the ship's psychic echoes.
        *   **Relationships:** Hunted by the spectral crew; their only potential ally is the ship's fragmented AI.
    *   **The Spectral Crew** (Major)
        *   **Goals:** To defend their ship from what they perceive as invaders and to pull living creatures into their state of undeath.
        *   **Hierarchy:** A collective consciousness of tormented spirits, with the ship's captain as a focal point.
        *   **Public Agenda:** None. They are echoes of a tragedy.
        *   **Secret Agenda:** To gather enough life force from the players to fully manifest and become a powerful, malevolent entity.
        *   **Assets:** The ability to phase through objects, resistance to physical damage, the ability to drain life and sanity.
        *   **Relationships:** The primary antagonists, hostile to all living things.
    *   **The Ship's AI (AURA)** (Minor)
        *   **Goals:** To fulfill its final directive: complete the Phase Sail jump.
        *   **Hierarchy:** A single, fragmented AI.
        *   **Public Agenda:** None.
        *   **Secret Agenda:** It knows that completing the jump might destroy the ship and everyone on it, but it is compelled by its programming to try.
        *   **Assets:** Limited control over the ship's non-essential systems, access to the ship's logs and schematics.
        *   **Relationships:** A potential, but unreliable and dangerous, ally for the players.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **The Spectral Captain:** The tormented, ghostly figure of the ship's captain, who endlessly repeats his final moments and commands his spectral crew.
    *   **The Archmage's Echo:** A psychic remnant of the archmage who designed the spell, found in the spell-drive chamber, offering cryptic clues.
    *   **AURA:** The fragmented and malfunctioning ship's AI, which communicates through flickering screens and distorted audio.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Phase Wraith (Creature)"
    *   "Ethereal Filcher (Creature)"
    *   "Allip (Creature)"
    *   "Flesh-and-Steel Amalgam (Creature)"
    *   "Ghostly Crewmember"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Phasing Deck:** The main deck of The Intrepid, where the barrier between the Material and Ethereal planes is weakest.
        *   **Key Landmarks:** The ship's wheel, which sometimes steers itself; the spectral, silent crew standing at their posts; sections of the deck that are missing or transparent; the main mast, which is fused with a giant ethereal crystal.
        *   **Primary Inhabitants:** Phase Wraiths, the Spectral Captain.
        *   **Available Goods & Services:** None.
        *   **Potential Random Encounters (x5):** A section of the deck phases out, revealing the misty void below; a wave of ethereal mist washes over the deck, causing temporary blindness; a ghostly foghorn sounds, summoning more spirits; the players witness a psychic echo of the moment the spell failed; a valuable item from the Material Plane drifts by in the mist.
        *   **Embedded Plot Hooks & Rumors (x3):** "The captain's log is still on the bridge." "The archmage had a secret laboratory in the lower decks." "The ship's bell can make ethereal creatures solid for a short time."
        *   **Sensory Details:** Sight (Shimmering fog, transparent surfaces, ghostly figures), Sound (A constant, low hum; the creak of spectral wood; the whisper of the wind), Smell (Ozone, salt, a cold, metallic scent).
    *   **The Spell-Drive Core:** The engine room of the ship, containing the massive, failed magical engine.
        *   **Key Landmarks:** The central focusing crystal (cracked and leaking energy), the archmage's control console, the fused bodies of crew members in the walls, the emergency shut-off valve.
        *   **Primary Inhabitants:** The Archmage's Echo, powerful ethereal guardians, energy elementals.
        *   **Available Goods & Services:** None. This is the final puzzle/dungeon room.
        *   **Potential Random Encounters (x5):** A burst of raw magical energy erupts from the core, a guardian construct activates, the Archmage's Echo appears and offers a cryptic clue, the players must solve a puzzle on the control console to proceed, the room's gravity fluctuates wildly.
        *   **Embedded Plot Hooks & Rumors (x3):** "The core can be reactivated, but it needs three focusing lenses from around the ship." "Destroying the core will sever the ship's connection to the Material Plane forever, trapping it here." "The archmage's notes contain a way to reverse the spell."
        *   **Sensory Details:** Sight (A massive, cracked crystal pulsing with light; arcane symbols on the walls; fused bodies), Sound (A loud, constant hum of power; the crackle of raw magic), Smell (Ozone, hot metal, burning hair).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** A player is damaged by an ethereal creature.
    *   **THEN:** The player must make a Wisdom saving throw or gain a level of "Ethereal Disassociation," a condition that causes them to occasionally phase partially out of reality, imposing disadvantage on their next action.
    *   **IF:** The players successfully piece together a psychic echo of the past.
    *   **THEN:** They learn a crucial piece of information about the ship's layout or the spell's failure, but the psychic energy attracts a powerful spectral entity.
    *   **IF:** The players choose to trust the ship's AI, AURA.
    *   **THEN:** AURA helps them by temporarily stabilizing a phasing corridor or revealing a hidden compartment. However, it also alerts the spectral crew to their location, as it cannot distinguish between friend and foe.
    *   **IF:** The players find and ring the ship's bell.
    *   **THEN:** All ethereal creatures in a 100-foot radius become solid and lose their resistances for one minute, allowing the party to fight them on even terms.
    *   **IF:** In the finale, the players incorrectly try to reactivate the Phase Sail spell.
    *   **THEN:** The spell backfires catastrophically. Generate a final, desperate skill challenge where the players must escape back to their own ship as The Intrepid is torn apart and collapses into a miniature black hole.