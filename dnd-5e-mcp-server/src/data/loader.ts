import { readFileSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Base path to the 5e-database data
const DATA_PATH = join(__dirname, '../../data/5e-database/src/2014');

// Data cache to avoid repeated file reads
const dataCache = new Map<string, any[]>();

// Load and cache data from JSON files
export function loadData(fileName: string): any[] {
  if (dataCache.has(fileName)) {
    return dataCache.get(fileName)!;
  }

  try {
    const filePath = join(DATA_PATH, fileName);
    const data = JSON.parse(readFileSync(filePath, 'utf-8'));
    dataCache.set(fileName, data);
    return data;
  } catch (error) {
    console.error(`Error loading ${fileName}:`, error);
    return [];
  }
}

// Utility function to search through data arrays
export function searchData(data: any[], searchTerm: string, fields: string[] = ['name', 'index']): any[] {
  const lowerSearchTerm = searchTerm.toLowerCase();

  return data.filter(item => {
    return fields.some(field => {
      const value = getNestedProperty(item, field);
      return value && value.toString().toLowerCase().includes(lowerSearchTerm);
    });
  });
}

// Get nested property from object using dot notation
function getNestedProperty(obj: any, path: string): any {
  return path.split('.').reduce((current, key) => current?.[key], obj);
}

// Fuzzy search implementation
export function fuzzySearch(data: any[], searchTerm: string, fields: string[] = ['name', 'index']): any[] {
  const results = searchData(data, searchTerm, fields);

  // If exact matches found, return them
  if (results.length > 0) {
    return results;
  }

  // Otherwise, try more flexible matching
  const terms = searchTerm.toLowerCase().split(' ');
  return data.filter(item => {
    return fields.some(field => {
      const value = getNestedProperty(item, field);
      if (!value) return false;

      const itemText = value.toString().toLowerCase();
      return terms.every(term => itemText.includes(term));
    });
  });
}

// Specific data loaders for each file type
export const loadSpells = () => loadData('5e-SRD-Spells.json');
export const loadMonsters = () => loadData('5e-SRD-Monsters.json');
export const loadClasses = () => loadData('5e-SRD-Classes.json');
export const loadRaces = () => loadData('5e-SRD-Races.json');
export const loadEquipment = () => loadData('5e-SRD-Equipment.json');
export const loadMagicItems = () => loadData('5e-SRD-Magic-Items.json');
export const loadFeatures = () => loadData('5e-SRD-Features.json');
export const loadConditions = () => loadData('5e-SRD-Conditions.json');
export const loadRules = () => loadData('5e-SRD-Rules.json');
export const loadSkills = () => loadData('5e-SRD-Skills.json');
export const loadBackgrounds = () => loadData('5e-SRD-Backgrounds.json');
export const loadSubclasses = () => loadData('5e-SRD-Subclasses.json');
export const loadTraits = () => loadData('5e-SRD-Traits.json');