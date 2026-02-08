full_dot = '●'
empty_dot = '○'

name = input("Enter name: ")
print("*****YOUR CHARACTER STATS*****")

# Convert inputs to integers
try:
    strength = int(input("Enter strength: "))
    intelligence = int(input("Enter intelligence: "))
    charisma = int(input("Enter charisma: "))
except ValueError:
    print("Error: Stats must be numbers!")
    exit()

def create_character(name, strength, intelligence, charisma):
    # validate name
    if not isinstance(name, str):
        return "The character name should be a string"

    if name == "":
        return "The character should have a name"

    if len(name) > 10:
        return "The character name is too long"

    if " " in name:
        return "The character name should not contain spaces"

    # Validate stats type
    if not all(isinstance(stat, int) for stat in [strength, intelligence, charisma]):
        return "All stats should be integers"

    # Validate stat minimum
    if any(stat < 1 for stat in [strength, intelligence, charisma]):
        return "All stats should be no less than 1"

    # Validate stat maximum
    if any(stat > 4 for stat in [strength, intelligence, charisma]):
        return "All stats should be no more than 4"

    # Validate total points
    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points"

    # Build stat lines
    def build_stat_line(label, value):
        full_dots = "●" * value
        empty_dots = "○" * (10 - value)
        return f"{label} {full_dots}{empty_dots}"
    
    result = (
        f"{name}\n"
        f"{build_stat_line('STR', strength)}\n"
        f"{build_stat_line('INT', intelligence)}\n"
        f"{build_stat_line('CHA', charisma)}"
    )
    
    return result

# Call the function and display the result
character = create_character(name, strength, intelligence, charisma)
print("\n" + character)