import {
  loadSpells,
  loadMonsters,
  loadClasses,
  loadRaces,
  loadEquipment,
  loadMagicItems,
  loadFeatures,
  loadConditions,
  loadRules,
  loadSkills,
  loadBackgrounds,
  loadSubclasses,
  loadTraits,
  searchData,
  fuzzySearch
} from './data/loader.js';

// Dice rolling utility
export function rollDice(expression: string): { result: number; rolls: number[]; expression: string } {
  // Parse dice expressions like "2d6+3", "1d20", "4d4-1"
  const match = expression.match(/(\d+)?d(\d+)([+\-]\d+)?/i);

  if (!match) {
    throw new Error(`Invalid dice expression: ${expression}`);
  }

  const numDice = parseInt(match[1] || '1', 10);
  const diceSize = parseInt(match[2], 10);
  const modifier = match[3] ? parseInt(match[3], 10) : 0;

  if (numDice < 1 || numDice > 100 || diceSize < 2 || diceSize > 1000) {
    throw new Error('Dice parameters out of reasonable range');
  }

  const rolls: number[] = [];
  let total = 0;

  for (let i = 0; i < numDice; i++) {
    const roll = Math.floor(Math.random() * diceSize) + 1;
    rolls.push(roll);
    total += roll;
  }

  total += modifier;

  return {
    result: total,
    rolls,
    expression: `${numDice}d${diceSize}${modifier >= 0 ? '+' : ''}${modifier || ''}`
  };
}

// Format search results for display
function formatResults(results: any[], maxResults: number = 10): any[] {
  return results.slice(0, maxResults).map(item => {
    // Remove URL references to clean up the output
    const cleaned = JSON.parse(JSON.stringify(item, (key, value) => {
      if (key === 'url' && typeof value === 'string' && value.startsWith('/api/')) {
        return undefined;
      }
      return value;
    }));
    return cleaned;
  });
}

// Tool implementations
export const tools = [
  {
    name: 'search_spell',
    description: 'Search for D&D 5e spells by name or keyword',
    inputSchema: {
      type: 'object',
      properties: {
        query: {
          type: 'string',
          description: 'Spell name or search term'
        },
        level: {
          type: 'number',
          description: 'Optional: Filter by spell level (0-9)',
          minimum: 0,
          maximum: 9
        },
        school: {
          type: 'string',
          description: 'Optional: Filter by magic school (e.g., evocation, divination)'
        },
        class: {
          type: 'string',
          description: 'Optional: Filter by class that can cast the spell'
        }
      },
      required: ['query']
    }
  },
  {
    name: 'search_monster',
    description: 'Search for D&D 5e monsters by name, type, or CR',
    inputSchema: {
      type: 'object',
      properties: {
        query: {
          type: 'string',
          description: 'Monster name or search term'
        },
        type: {
          type: 'string',
          description: 'Optional: Filter by monster type (e.g., undead, dragon, humanoid)'
        },
        cr_min: {
          type: 'number',
          description: 'Optional: Minimum challenge rating'
        },
        cr_max: {
          type: 'number',
          description: 'Optional: Maximum challenge rating'
        }
      },
      required: ['query']
    }
  },
  {
    name: 'search_class',
    description: 'Search for D&D 5e class information and features',
    inputSchema: {
      type: 'object',
      properties: {
        query: {
          type: 'string',
          description: 'Class name or search term'
        }
      },
      required: ['query']
    }
  },
  {
    name: 'search_race',
    description: 'Search for D&D 5e race information and traits',
    inputSchema: {
      type: 'object',
      properties: {
        query: {
          type: 'string',
          description: 'Race name or search term'
        }
      },
      required: ['query']
    }
  },
  {
    name: 'search_equipment',
    description: 'Search for D&D 5e equipment, weapons, and armor',
    inputSchema: {
      type: 'object',
      properties: {
        query: {
          type: 'string',
          description: 'Equipment name or search term'
        },
        category: {
          type: 'string',
          description: 'Optional: Filter by equipment category'
        }
      },
      required: ['query']
    }
  },
  {
    name: 'search_magic_item',
    description: 'Search for D&D 5e magic items',
    inputSchema: {
      type: 'object',
      properties: {
        query: {
          type: 'string',
          description: 'Magic item name or search term'
        },
        rarity: {
          type: 'string',
          description: 'Optional: Filter by rarity (common, uncommon, rare, very rare, legendary)'
        }
      },
      required: ['query']
    }
  },
  {
    name: 'search_condition',
    description: 'Search for D&D 5e conditions and their effects',
    inputSchema: {
      type: 'object',
      properties: {
        query: {
          type: 'string',
          description: 'Condition name or search term'
        }
      },
      required: ['query']
    }
  },
  {
    name: 'search_rules',
    description: 'Search for D&D 5e game rules and mechanics',
    inputSchema: {
      type: 'object',
      properties: {
        query: {
          type: 'string',
          description: 'Rule topic or search term'
        }
      },
      required: ['query']
    }
  },
  {
    name: 'roll_dice',
    description: 'Roll dice with standard D&D notation (e.g., 2d6+3, 1d20, 4d4-1)',
    inputSchema: {
      type: 'object',
      properties: {
        expression: {
          type: 'string',
          description: 'Dice expression in standard notation (e.g., 2d6+3)'
        }
      },
      required: ['expression']
    }
  },
  {
    name: 'get_random_encounter',
    description: 'Get a random monster for encounters based on challenge rating',
    inputSchema: {
      type: 'object',
      properties: {
        cr: {
          type: 'number',
          description: 'Challenge rating for the encounter'
        },
        type: {
          type: 'string',
          description: 'Optional: Monster type filter'
        }
      },
      required: ['cr']
    }
  }
];

// Tool execution handlers
export async function handleToolCall(name: string, args: any): Promise<any> {
  try {
    switch (name) {
      case 'search_spell':
        return handleSearchSpell(args);
      case 'search_monster':
        return handleSearchMonster(args);
      case 'search_class':
        return handleSearchClass(args);
      case 'search_race':
        return handleSearchRace(args);
      case 'search_equipment':
        return handleSearchEquipment(args);
      case 'search_magic_item':
        return handleSearchMagicItem(args);
      case 'search_condition':
        return handleSearchCondition(args);
      case 'search_rules':
        return handleSearchRules(args);
      case 'roll_dice':
        return handleRollDice(args);
      case 'get_random_encounter':
        return handleRandomEncounter(args);
      default:
        throw new Error(`Unknown tool: ${name}`);
    }
  } catch (error) {
    return {
      error: true,
      message: error instanceof Error ? error.message : 'Unknown error occurred'
    };
  }
}

// Individual tool handlers
function handleSearchSpell(args: any) {
  const spells = loadSpells();
  let results = fuzzySearch(spells, args.query, ['name', 'index', 'desc']);

  // Apply filters
  if (args.level !== undefined) {
    results = results.filter(spell => spell.level === args.level);
  }
  if (args.school) {
    results = results.filter(spell =>
      spell.school?.index?.toLowerCase().includes(args.school.toLowerCase())
    );
  }
  if (args.class) {
    results = results.filter(spell =>
      spell.classes?.some((cls: any) =>
        cls.name?.toLowerCase().includes(args.class.toLowerCase())
      )
    );
  }

  return {
    query: args.query,
    count: results.length,
    results: formatResults(results, 5)
  };
}

function handleSearchMonster(args: any) {
  const monsters = loadMonsters();
  let results = fuzzySearch(monsters, args.query, ['name', 'index', 'type']);

  // Apply filters
  if (args.type) {
    results = results.filter(monster =>
      monster.type?.toLowerCase().includes(args.type.toLowerCase())
    );
  }
  if (args.cr_min !== undefined) {
    results = results.filter(monster => {
      const cr = typeof monster.challenge_rating === 'number'
        ? monster.challenge_rating
        : parseFloat(monster.challenge_rating?.toString() || '0');
      return cr >= args.cr_min;
    });
  }
  if (args.cr_max !== undefined) {
    results = results.filter(monster => {
      const cr = typeof monster.challenge_rating === 'number'
        ? monster.challenge_rating
        : parseFloat(monster.challenge_rating?.toString() || '0');
      return cr <= args.cr_max;
    });
  }

  return {
    query: args.query,
    count: results.length,
    results: formatResults(results, 5)
  };
}

function handleSearchClass(args: any) {
  const classes = loadClasses();
  const results = fuzzySearch(classes, args.query, ['name', 'index']);

  return {
    query: args.query,
    count: results.length,
    results: formatResults(results, 3)
  };
}

function handleSearchRace(args: any) {
  const races = loadRaces();
  const results = fuzzySearch(races, args.query, ['name', 'index']);

  return {
    query: args.query,
    count: results.length,
    results: formatResults(results, 5)
  };
}

function handleSearchEquipment(args: any) {
  const equipment = loadEquipment();
  let results = fuzzySearch(equipment, args.query, ['name', 'index']);

  if (args.category) {
    results = results.filter(item =>
      item.equipment_category?.name?.toLowerCase().includes(args.category.toLowerCase())
    );
  }

  return {
    query: args.query,
    count: results.length,
    results: formatResults(results, 10)
  };
}

function handleSearchMagicItem(args: any) {
  const magicItems = loadMagicItems();
  let results = fuzzySearch(magicItems, args.query, ['name', 'index', 'desc']);

  if (args.rarity) {
    results = results.filter(item =>
      item.rarity?.name?.toLowerCase().includes(args.rarity.toLowerCase())
    );
  }

  return {
    query: args.query,
    count: results.length,
    results: formatResults(results, 5)
  };
}

function handleSearchCondition(args: any) {
  const conditions = loadConditions();
  const results = fuzzySearch(conditions, args.query, ['name', 'index', 'desc']);

  return {
    query: args.query,
    count: results.length,
    results: formatResults(results, 10)
  };
}

function handleSearchRules(args: any) {
  const rules = loadRules();
  const results = fuzzySearch(rules, args.query, ['name', 'index', 'desc']);

  return {
    query: args.query,
    count: results.length,
    results: formatResults(results, 5)
  };
}

function handleRollDice(args: any) {
  const result = rollDice(args.expression);
  return {
    expression: args.expression,
    result: result.result,
    rolls: result.rolls,
    breakdown: `${result.rolls.join(' + ')}${result.expression.includes('+') || result.expression.includes('-') ? result.expression.match(/[+\-]\d+/)?.[0] || '' : ''} = ${result.result}`
  };
}

function handleRandomEncounter(args: any) {
  const monsters = loadMonsters();

  // Filter by CR and optional type
  let validMonsters = monsters.filter(monster => {
    const cr = typeof monster.challenge_rating === 'number'
      ? monster.challenge_rating
      : parseFloat(monster.challenge_rating?.toString() || '0');

    const crMatches = Math.abs(cr - args.cr) <= 0.5; // Allow some variance
    const typeMatches = !args.type || monster.type?.toLowerCase().includes(args.type.toLowerCase());

    return crMatches && typeMatches;
  });

  if (validMonsters.length === 0) {
    return {
      error: true,
      message: `No monsters found for CR ${args.cr}${args.type ? ` and type ${args.type}` : ''}`
    };
  }

  const randomMonster = validMonsters[Math.floor(Math.random() * validMonsters.length)];

  return {
    cr: args.cr,
    type: args.type,
    encounter: formatResults([randomMonster], 1)[0]
  };
}