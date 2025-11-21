### **Template: World-Building Specification Brief**

This document is the primary instruction set for the world-building AI pipeline. Each section provides explicit directives for specialized agents to generate the necessary assets for a complete and dynamic campaign world.

---

**The Final Examination: Academy of Night**

**1. Core Concept & Narrative Hook**
*   **Directive:** This is the foundational context. All generated content must align with this core premise.
*   **Content:** The players are scholarship students at the elite and remote Blackwood University, a renowned magical institution shrouded in ancient traditions and academic excellence. They soon discover the university's horrifying secret: it is a farm, and the ancient, vampiric faculty are the farmers who cultivate the most promising students for their magical talent. "Graduation" is a euphemism for a ritual where students' life force is harvested to sustain the faculty's immortality. Having learned the truth, the players must navigate the paranoid social landscape of the school, find a means of escape, and break free before their own "Final Examination" is scheduled.

**2. Lore & History Primer**
*   **Directive:** The Lore Generation Agent must create detailed entries for each of the following prompts. These entries will form the historical and cultural bedrock of the world.
*   **Prompts:**
    *   Detail the founding of Blackwood University and its transformation from a center of learning to a predatory institution.
    *   Write the history of the vampiric faculty and their development of the soul-harvesting ritual.
    *   Describe the evolution of the university's curriculum and how it serves the faculty's predatory needs.
    *   Explain the various methods the faculty uses to identify and cultivate promising students.
    *   Detail the student resistance movements that have occasionally emerged and their tragic outcomes.
    *   Write about the "University Charter" - the ancient document that binds the faculty's behavior and creates their only weakness.

**3. Faction Deep-Dive**
*   **Directive:** The Faction Generation Agent must create a detailed profile for each faction listed below. Each profile must contain the specified fields.
*   **Factions Roster:**
    *   **The Faculty Circle** (Major)
        *   **Goals:** To maintain the university's operations and identify students suitable for the harvest ritual.
        *   **Hierarchy:** Council of ancient vampires led by Headmaster Viktor Voss.
        *   **Public Agenda:** We provide the finest magical education and preserve academic excellence.
        *   **Secret Agenda:** To harvest the life force of exceptional students to maintain our immortality.
        *   **Assets:** Ancient magical knowledge, university facilities, student surveillance systems.
        *   **Relationships:** Predatory toward students; cooperative among faculty members.
    *   **The Student Body** (Major)
        *   **Goals:** To survive the university's demands and graduate successfully.
        *   **Hierarchy:** Informal social structure led by prefects and senior students.
        *   **Public Agenda:** We are the future of magical academia and scholarship.
        *   **Secret Agenda:** To uncover the university's secrets and potentially escape its grasp.
        *   **Assets:** Youthful energy, collective knowledge, potential magical talent.
        *   **Relationships:** Competitive among themselves; suspicious of faculty authority.
    *   **The University Staff** (Minor)
        *   **Goals:** To maintain the university's operations while surviving the faculty's predation.
        *   **Hierarchy:** Departmental structure led by senior staff members who have survived longest.
        *   **Public Agenda:** We support the university's mission of magical education.
        *   **Secret Agenda:** To protect promising students from the faculty's harvest.
        *   **Assets:** Intimate knowledge of university operations, access to restricted areas.
        *   **Relationships:** Supportive of students; fearful of faculty; protective of university secrets.

**4. NPC Generation Roster**
*   **Directive:** The Character Generation Agent must create full profiles for all NPCs listed. Tier 1 NPCs are unique individuals. Tier 2 & 3 are archetypes to be instantiated multiple times with unique details as needed by the simulation.
*   **Tier 1 (Unique, Major NPCs):**
    *   **Headmaster Viktor Voss:** The ancient vampire who founded the university and leads the faculty.
    *   **Professor Mortain:** The lich-librarian obsessed with knowledge preservation.
    *   **Elara Voss, Head Prefect:** The brilliant student leader destined to become the Headmaster's successor.
*   **Tier 2 & 3 (Archetypes for Generation):**
    *   "Faculty Professor"
    *   "Senior Student"
    *   "University Staff"
    *   "Suspicious Student"
    *   "Faculty Informant"
    *   "Resistant Student"

**5. Location Blueprints**
*   **Directive:** The Environment Generation Agent must create a detailed blueprint for each location below, populating all specified sub-sections.
*   **Location Roster:**
    *   **Blackwood University Campus:** The entire campaign setting.
        *   **Key Landmarks:** The Main Academy Building, the Grand Library, the Student Dormitories, the Faculty Tower.
        *   **Primary Inhabitants:** Students, faculty, staff, and various magical creatures and constructs.
        *   **Available Goods & Services:** Academic resources, magical supplies, student services.
        *   **Potential Random Encounters (x5):** A faculty member observes suspicious activity, a student shares a rumor, discovery of a secret passage, a magical experiment goes wrong, a staff member offers discreet assistance.
        *   **Embedded Plot Hooks & Rumors (x3):** "The university has stood for centuries without change." "Some graduates never truly leave the campus." "The faculty tower holds the university's greatest secrets."
        *   **Sensory Details:** Sight (Gothic architecture, magical auras), Sound (Echoing hallways, distant lectures), Smell (Old books, magical incense).
    *   **The Grand Library:** A labyrinth of books and secret passages.
        *   **Key Landmarks:** The Main Reading Room, the Restricted Archives, the Faculty Study, the Hidden Stacks.
        *   **Primary Inhabitants:** Professor Mortain, dedicated students, magical book guardians.
        *   **Available Goods & Services:** Rare books, research assistance, forbidden knowledge.
        *   **Potential Random Encounters (x5):** A book guardian activates, a student discovers a secret text, discovery of a hidden passage, Professor Mortain makes an appearance, a magical tome reveals its secrets.
        *   **Embedded Plot Hooks & Rumors (x3):** "The library contains books that can drive readers mad." "Some students never return from the restricted section." "The library remembers every student who ever studied there."
        *   **Sensory Details:** Sight (Endless bookshelves, floating magical texts), Sound (Page turning, whispering voices), Smell (Aged paper, leather bindings).
    *   **The Arboretum:** A sprawling greenhouse of dangerous magical plants.
        *   **Key Landmarks:** The Central Conservatory, the Poison Gardens, the Experimental Groves, the Herbology Labs.
        *   **Primary Inhabitants:** Botany students, plant creatures, herbology professors.
        *   **Available Goods & Services:** Magical plants, potion ingredients, botanical knowledge.
        *   **Potential Random Encounters (x5):** A plant creature becomes aggressive, a student experiments with dangerous flora, discovery of a mutated specimen, a professor demonstrates a plant's properties, a garden maze shifts unexpectedly.
        *   **Embedded Plot Hooks & Rumors (x3):** "Some plants in the arboretum are students who failed their exams." "The central conservatory contains the oldest magical plant." "The poison gardens hold the cure to faculty immortality."
        *   **Sensory Details:** Sight (Exotic magical plants, colorful blooms), Sound (Rustling leaves, dripping water), Smell (Earth, flowers, herbs).

**6. Causality Chains & Dynamic World States**
*   **Directive:** The World Simulation Agent must implement the following trigger-based state changes. For each "IF" condition, the agent must pre-generate the narrative and environmental consequences for the "THEN" outcome.
*   **Triggers:**
    *   **IF:** The players successfully access the Forbidden Wing of the library.
    *   **THEN:** They gain crucial knowledge but attract faculty attention. Generate scenarios where the library's defenses activate to contain the breach.
    *   **IF:** The players form alliances with other students.
    *   **THEN:** They gain additional resources and information. Generate scenarios where student conflicts create complications.
    *   **IF:** The players discover the university's charter.
    *   **THEN:** They gain leverage over the faculty. Generate scenarios where the charter's restrictions create unexpected opportunities.
    *   **IF:** The players attempt to escape during the Commencement Ball.
    *   **THEN:** The entire campus becomes a hunting ground. Generate scenarios where the faculty drops all pretense and actively hunts the players.
    *   **IF:** The players confront the Headmaster directly.
    *   **THEN:** They may achieve victory but at great personal cost. Generate scenarios where the Headmaster's defeat triggers succession conflicts among the faculty.
