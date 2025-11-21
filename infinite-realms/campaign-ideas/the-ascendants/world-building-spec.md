### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Ascendants**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** In the modern city of Metroburg, a mysterious event called the "Ascension" has granted a small percentage of the population incredible powers. The players are a group of these newly-powered individuals who must decide whether to become heroes or villains while dealing with the consequences of their actions, the emergence of other, more dangerous Ascendants, and the revelation of the Ascension's terrifying, man-made origin.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the "Ascension" event. What did it look like? How did it feel to those who were empowered?
    *   Write the history of Project Chimera, the shadowy government agency behind the Ascension.
    *   Describe the public's initial reaction to the emergence of Ascendants, using news reports and social media posts.
    *   Explain the different theories about the source of the powers (magic, mutation, divine gift) before the truth is revealed.
    *   Detail the story of Apex's transformation from a victim of Project Chimera's experiments into a supervillain.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Party (The Ascendants)** (Major)
        *   **Goals:** To understand their powers, protect the innocent, and survive in a world that fears them.
        *   **Hierarchy:** A newly-formed, democratic team of heroes.
        *   **Public Agenda:** To be a force for good and prove that Ascendants are not a threat.
        *   **Secret Agenda:** To uncover the truth behind the Ascension and protect their secret identities.
        *   **Assets:** Their unique powers, a secret base of operations (once established), the element of surprise.
        *   **Relationships:** In direct opposition to Apex; wary of the government; trying to win over the public.
    *   **The True Ascendants** (Major)
        *   **Goals:** To establish a new world order where Ascendants rule over humans.
        *   **Hierarchy:** An authoritarian structure led by the charismatic and powerful Apex.
        *   **Public Agenda:** To liberate Ascendants from human oppression.
        *   **Secret Agenda:** Apex is desperately seeking a cure for his own unstable powers, even if it means sacrificing the entire city.
        *   **Assets:** A small army of loyal, super-powered followers; a fortified headquarters; Apex's immense power.
        *   **Relationships:** The primary antagonists, viewing the players as race-traitors.
    *   **Project Chimera** (Major)
        *   **Goals:** To control or eliminate all Ascendants and cover up their role in the Ascension event.
        *   **Hierarchy:** A clandestine government agency led by the ruthless General Miller.
        *   **Public Agenda:** To monitor and contain the Ascendant threat.
        *   **Secret Agenda:** To capture and weaponize powerful Ascendants while eliminating any evidence of their illegal experiments.
        *   **Assets:** Advanced technology, highly-trained soldiers, black sites, a powerful, unstable Ascendant kept in cryo-sleep.
        *   **Relationships:** A secondary antagonist, hostile to all Ascendants, including the players and Apex.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Apex:** The charismatic, arrogant, and tragic leader of the True Ascendants, whose powers are slowly killing him.
    *   **General Miller:** The cold, calculating, and ruthless leader of Project Chimera, who is secretly protecting his Ascendant son.
    *   **Jessica Jones (a nod, but distinct):** A tenacious and idealistic reporter investigating the Ascension, driven by the disappearance of her Ascendant brother.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Newly-powered, scared teenager"
    *   "Power-hungry thug who joined Apex"
    *   "Black-suited Project Chimera agent"
    *   "Fear-mongering news anchor"
    *   "Grateful citizen saved by the heroes"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **The Rooftops of Metroburg:** The domain of the city's heroes and villains, a place of secret meetings and dramatic battles.
        *   **Key Landmarks:** The gargoyle-adorned spire of the old cathedral, the neon-lit sign of the Metroburg Globe newspaper, the water towers of the industrial district, the glass roof of the central mall.
        *   **Primary Inhabitants:** Heroes, villains, pigeons.
        *   **Available Goods & Services:** A vantage point to survey the city, a quick escape route.
        *   **Potential Random Encounters (x5):** The party spots a crime in progress below, a rival Ascendant is seen patrolling their territory, a police helicopter shines its spotlight on the party, a sudden rainstorm makes the rooftops slick and dangerous, a group of teenagers are trying to film the heroes for social media.
        *   **Embedded Plot Hooks & Rumors (x3):** "Apex has been seen meeting with someone on the roof of the old power station." "There's a network of hidden caches on the rooftops, left by a previous generation of vigilantes." "Project Chimera has sniper nests on several key buildings."
        *   **Sensory Details:** Sight (Sprawling city lights, dramatic skylines, steam from vents), Sound (The distant wail of sirens, the hum of the city, the wind), Smell (Rain on concrete, exhaust fumes).
    *   **The Underground Fight Club:** A hidden arena where Ascendants test their powers for money and fame.
        *   **Key Landmarks:** The main fighting pit, the betting cages, the black-market potion vendor, the private lounge for high-rollers.
        *   **Primary Inhabitants:** Power-hungry Ascendants, criminals, gamblers, informants.
        *   **Available Goods & Services:** A place to earn money, gather information, or make dangerous contacts.
        *   **Potential Random Encounters (x5):** A fight gets out of hand and spills into the crowd, the party is challenged to a fight, the police raid the club, a recruiter for Apex is trying to sign up new talent, the party spots a Project Chimera agent observing the fights.
        *   **Embedded Plot Hooks & Rumors (x3):** "The champion of the fight club has a piece of Project Chimera tech." "The owner of the club is an information broker." "Apex himself got his start fighting here."
        *   **Sensory Details:** Sight (Flickering lights, cheering crowds, raw displays of power, exchanging of money), Sound (The roar of the crowd, the impact of blows, the crackle of energy), Smell (Sweat, blood, cheap alcohol).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players successfully stop a public crime and save civilians.
    *   **THEN:** Their Public Image score increases. Generate a positive news report about their actions and a short scene where a citizen thanks them.
    *   **IF:** The players cause a large amount of collateral damage during a fight.
    *   **THEN:** Their Public Image score decreases. Generate a negative news report questioning if they are as dangerous as the villains, and the police become less cooperative.
    *   **IF:** A player chooses to reveal their secret identity to a loved one.
    *   **THEN:** Generate a roleplaying scenario focused on the consequences of this revelation. That loved one now becomes a potential target for the player's enemies.
    *   **IF:** The players successfully expose Apex's plan to the public.
    *   **THEN:** Some of Apex's followers desert him, weakening his forces. However, Apex becomes more desperate and accelerates his timeline, forcing a confrontation sooner than expected.
    *   **IF:** In the final act, the players choose to release the evidence of Project Chimera's experiments to the world.
    *   **THEN:** Generate an epilogue where the world is thrown into panic. Governments begin registering and hunting Ascendants, and the players become fugitives, but also symbols of hope for a new generation of powered individuals.
