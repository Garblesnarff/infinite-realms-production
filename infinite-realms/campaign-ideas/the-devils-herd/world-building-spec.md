### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Devil's Herd**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise. The tone is a high-octane, man-vs-nature apocalyptic thriller.
*   **Content:** Based on Australia's real-life "Great Emu War," an ancient, malevolent earth-spirit has granted terrifying intelligence to the continent's fauna, creating a unified army known as the "Red Earth Army." The players are survivors who must cross the hostile outback, battling mobs of killer kangaroos and tactical emus, to reach a supposed safe haven, all while being hunted by the most dangerous, coordinated wildlife on the planet.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the nature and history of the malevolent earth-spirit. What is its motivation for wiping out humanity?
    *   Write a detailed, tactical after-action report of the 1932 Great Emu War from the perspective of the victorious emus.
    *   Describe the initial hours of the animal uprising, known as the "Red Day."
    *   Explain the command structure of the Red Earth Army, detailing the specific roles of kangaroos, cassowaries, kookaburras, and spiders.
    *   Detail the legends and rumors surrounding "Sanctuary," the supposed last safe haven for humanity.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Survivors (The Players)** (Minor)
        *   **Goals:** To travel across the outback and reach the safe zone of Sanctuary.
        *   **Hierarchy:** A small, independent group of survivors.
        *   **Public Agenda:** To survive.
        *   **Secret Agenda:** Each survivor may have a personal goal, such as finding a lost family member or a piece of valuable technology.
        *   **Assets:** Their skills, a single vehicle, and whatever they can scavenge.
        *   **Relationships:** Hunted by the Red Earth Army; wary of other survivor groups.
    *   **The Red Earth Army** (Major)
        *   **Goals:** To eradicate all human presence from the continent.
        *   **Hierarchy:** A collective consciousness guided by the earth-spirit, with emus acting as strategists and field commanders.
        *   **Public Agenda:** None. They are a force of nature.
        *   **Secret Agenda:** To perform a ritual at a specific location (e.g., Uluru) that will permanently fuse the earth-spirit with the continent's fauna, making their intelligence permanent and irreversible.
        *   **Assets:** A continent-spanning army of intelligent and coordinated animals, intimate knowledge of the terrain, the ability to influence the weather.
        *   **Relationships:** The primary antagonists, hostile to all humans.
    *   **The Road Scrappers** (Minor)
        *   **Goals:** To survive and profit by scavenging and controlling key resources like fuel and water.
        *   **Hierarchy:** Numerous small, competing gangs, each led by a ruthless leader.
        *   **Public Agenda:** Survival of the fittest.
        *   **Secret Agenda:** To capture and tame some of the less intelligent animals for their own use.
        *   **Assets:** Fortified outposts, heavily modified vehicles, a willingness to do anything to survive.
        *   **Relationships:** Hostile to the players (as competitors for resources) and the Red Earth Army (as prey).

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **The Earth-Spirit's Echo:** A psychic projection of the ancient earth-spirit, which may appear as a shimmering figure, a voice on the wind, or in the eyes of a lead emu.
    *   **"Mad" Max (a nod, but distinct):** A grizzled, lone survivor who has lost his family and now roams the outback, offering cryptic advice or sudden violence in equal measure.
    *   **The Emu General:** A specific, highly intelligent and scarred emu that acts as the field commander for the local Red Earth Army forces, becoming a recurring nemesis for the players.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Desperate Survivor in a ruined town"
    *   "Ruthless Road Scrapper Boss"
    *   "Tactical Emu (Creature)"
    *   "Brawling Kangaroo (Creature)"
    *   "Cassowary Assassin (Creature)"
    *   "Venomous Spider Ambusher (Creature)"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **A Ruined Outback Town:** A small, abandoned town, now a hunting ground for the Red Earth Army.
        *   **Key Landmarks:** The abandoned petrol station, the fortified pub, the dried-up water tower, the local mechanic's garage.
        *   **Primary Inhabitants:** Packs of kangaroos, flocks of galahs acting as lookouts, hidden venomous creatures.
        *   **Available Goods & Services:** Salvageable fuel, scrap metal, canned food, spare parts.
        *   **Potential Random Encounters (x5):** A mob of kangaroos attacks, a dust storm rolls in, the party finds a hidden cache of supplies, a rival group of survivors arrives, the Emu General is spotted observing the town from a nearby ridge.
        *   **Embedded Plot Hooks & Rumors (x3):** "The mechanic's garage has the parts needed to upgrade our vehicle." "There's a map to a working well in the pub." "The last broadcast from Sanctuary came from the radio tower here."
        *   **Sensory Details:** Sight (Dusty, empty streets; sun-bleached buildings; the twitch of an ear in the distance), Sound (Howling wind, the distant caw of a crow, an unnerving silence), Smell (Dust, rust, the faint scent of eucalyptus).
    *   **A Red Earth Army Nesting Ground:** A key strategic location for the animals, such as a massive emu nest or a kangaroo mob's warren.
        *   **Key Landmarks:** The central nest/warren, lookout points, a large watering hole, a graveyard of human vehicles.
        *   **Primary Inhabitants:** Hundreds of coordinated animals, including non-combatant young.
        *   **Available Goods & Services:** None. This is an enemy stronghold.
        *   **Potential Random Encounters (x5):** The party is spotted by a kookaburra scout, a patrol of cassowaries attacks, the Emu General arrives to give orders, the party has a chance to poison the watering hole, a captured human survivor is found.
        *   **Embedded Plot Hooks & Rumors (x3):** "The Emu General is planning a major assault on a nearby survivor outpost." "The animals are hoarding scavenged human technology here." "The earth-spirit's influence is strongest here, causing strange weather patterns."
        *   **Sensory Details:** Sight (A massive, organized animal colony; crude fortifications made of branches and scrap metal), Sound (A cacophony of animal calls, the thumping of kangaroo feet, the clicks and whistles of emu commands), Smell (Animal musk, dirt, rain).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players successfully salvage enough parts to upgrade their vehicle.
    *   **THEN:** They gain a new ability for vehicle combat (e.g., a ram, reinforced armor, a mounted weapon), but their vehicle now consumes more fuel.
    *   **IF:** The players are caught in a dust storm caused by the earth-spirit.
    *   **THEN:** They must make a series of survival checks to navigate. Failure results in their vehicle being damaged and losing precious resources.
    *   **IF:** The players successfully destroy a Red Earth Army nesting ground.
    *   **THEN:** The animal attacks in that region become disorganized and less frequent for a time, creating a safe window for travel. However, the Emu General now considers the players a primary threat and begins actively hunting them.
    *   **IF:** The players choose to ally with a group of Road Scrappers.
    *   **THEN:** They gain access to a fortified outpost and better resources, but must participate in a raid against another survivor group, making them enemies of other potential allies.
    *   **IF:** The players reach Sanctuary.
    *   **THEN:** Generate a final twist. Sanctuary is not a place, but a person: a powerful psychic who has been keeping the animals at bay. The earth-spirit is now focusing all its power to break this person's concentration, and the players must defend them in a final, desperate siege.