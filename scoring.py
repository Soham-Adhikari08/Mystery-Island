# scoring.py
# Updates points and displays final results

def calculate_score(current_score, points_to_add):
    """Updates the player's points and returns the new total."""
    new_score = current_score + points_to_add
    print(f"+{points_to_add} POINTS")
    return new_score

def end_game(health, inventory, required_items):
    """Checks the win/lose condition and displays the final result."""
    # Lose condition
    if health <= 0:
        print("\nGAME OVER! You have lost all your lives.")
        return False
        
    # Win condition check
    has_all_items = True
    for item in required_items:
        if item not in inventory:
            has_all_items = False
            
    if has_all_items:
        print("\nCONGRATULATIONS! You used your items to unlock the chamber and found the legendary treasure!")
        return True
    else:
        print("\nYou do not have the required items to enter the final chamber yet.")
        return False