# D&D 5e MCP Server

A Model Context Protocol (MCP) server that provides access to D&D 5th Edition SRD data for Claude Code and other MCP-compatible clients.

## Features

This MCP server provides the following tools:

### Core Search Tools
- **search_spell** - Search for spells by name, level, school, or class
- **search_monster** - Find monsters by name, type, or challenge rating
- **search_class** - Look up class information and features
- **search_race** - Find race information and traits
- **search_equipment** - Search weapons, armor, and gear
- **search_magic_item** - Find magic items by name or rarity
- **search_condition** - Look up conditions and their effects
- **search_rules** - Search game rules and mechanics

### Utility Tools
- **roll_dice** - Roll dice with standard D&D notation (e.g., 2d6+3, 1d20)
- **get_random_encounter** - Generate random encounters by challenge rating

## Installation

1. Clone this repository
2. Install dependencies: `npm install`
3. Build the TypeScript: `npm run build`
4. Add to your Claude Desktop configuration:

```json
{
  "mcpServers": {
    "dnd-5e": {
      "command": "node",
      "args": ["/path/to/dnd-5e-mcp-server/dist/index.js"]
    }
  }
}
```

## Data Source

This server uses the official D&D 5e SRD data from [5e-bits/5e-database](https://github.com/5e-bits/5e-database), which contains comprehensive information about spells, monsters, classes, races, equipment, and game rules.

## Usage Examples

### Spell Search
```
Query: "search for fireball spell"
Returns: Complete spell information including damage, range, components, etc.
```

### Monster Lookup
```
Query: "find dragons with CR 10 or higher"
Returns: List of dragon monsters filtered by challenge rating
```

### Dice Rolling
```
Query: "roll 2d6+3"
Returns: Individual dice results and total with breakdown
```

### Random Encounters
```
Query: "give me a random CR 5 encounter"
Returns: Random monster appropriate for CR 5 encounters
```

## Development

- `npm run build` - Compile TypeScript to JavaScript
- `npm run dev` - Watch for changes and recompile
- `npm start` - Run the compiled server

## License

MIT - See LICENSE file for details.

## Contributing

This server was built to provide D&D 5e reference data to AI assistants for game mastering and character creation. Feel free to contribute improvements or additional tools!