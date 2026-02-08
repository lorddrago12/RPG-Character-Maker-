# RPG Character Maker

A simple command-line RPG character creation tool that allows you to create a character with custom stats displayed in a visual format.

## Features

- Interactive character name input
- Three core stats: Strength (STR), Intelligence (INT), and Charisma (CHA)
- Visual stat representation using filled and empty dots
- Input validation to ensure balanced characters
- Clean, formatted character sheet output

## Requirements

- Python 3.6 or higher

## Installation

No installation required! Just download `main.py` and run it.

## Usage

Run the program from your terminal:

```bash
python main.py
```

You'll be prompted to enter:
1. Your character's name
2. Strength value (1-4)
3. Intelligence value (1-4)
4. Charisma value (1-4)

### Example

```
Enter name: Aragorn
*****YOUR CHARACTER STATS*****
Enter strength: 3
Enter intelligence: 2
Enter charisma: 2

Aragorn
STR ●●●○○○○○○○
INT ●●○○○○○○○○
CHA ●●○○○○○○○○
```

## Character Rules

Your character must follow these rules:

- **Name**: 
  - Must be a non-empty string
  - Maximum 10 characters
  - No spaces allowed
  
- **Stats**:
  - Each stat must be between 1 and 4
  - All stats must be integers
  - Total stat points must equal exactly 7

## Visual Display

Stats are displayed using:
- **●** (filled dot) - Allocated stat points
- **○** (empty dot) - Unallocated stat points (up to 10 total)

## Error Handling

The program will display helpful error messages if:
- Non-numeric values are entered for stats
- Name doesn't meet requirements
- Stats don't meet the validation rules
- Total stat points don't equal 7

## License

Free to use and modify for personal or educational purposes.
