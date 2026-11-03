# player.py
# Handles player name, health and status

def get_player_name():
    """Asks for and returns the player's name."""
    name = input("Enter your explorer name: ")
    return name

def show_status(health, score, inventory):
    """Displays health, score and progress."""
    print("\nPLAYER STATUS")
    print(f"Health : {health} lives")
    print(f"Score  : {score}")
    
    # Check if inventory is empty to display it exactly like the sample terminal output
    if len(inventory) == 0:
        print("Items  : Empty")
    else:
        # Prints items separated by a comma
        print(f"Items  : {', '.join(inventory)}")
    print("=====================")

def lose_life(current_health):
    """Reduces health after a failed challenge and ensures it never goes below zero."""
    new_health = current_health - 1
    
    # Check to ensure health never drops below zero
    if new_health < 0:
        new_health = 0
        
    return new_health