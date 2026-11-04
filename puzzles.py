# puzzles.py - Stores riddles, hints, and answer-checking logic for Mystery Island

# Dictionary holding location-specific puzzles, riddles, hints, and correct answers
PUZZLES = {
    "Dark Forest": {
        "riddle": "I have roots as nobody sees, higher than trees, up and up I go, and yet I never grow. What am I?",
        "hint": "Think about something tall and rocky that touches the clouds.",
        "answer": "mountain"
    },
    "Crystal Cave": {
        "riddle": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
        "hint": "You can hear me bounce back when you shout in an empty canyon.",
        "answer": "echo"
    },
    "Ancient Ruins": {
        "riddle": "What has to be broken before you can use it?",
        "hint": "You usually crack this open in the morning for breakfast.",
        "answer": "egg"
    },
    "Sunken Shipwreck": {
        "riddle": "I have keys but no locks. I have space but no room. You can enter, but you can't go outside. What am I?",
        "hint": "You use me every day when you type out code on a computer.",
        "answer": "keyboard"
    },
    "Treasure Chamber": {
        "riddle": "FINAL TRIAL: I am full of holes, yet I still hold a lot of water. What am I?",
        "hint": "It's a soft, absorbent cleaning tool you use in the kitchen or bathroom.",
        "answer": "sponge"
    }
}

def get_puzzle(location_name):
    """
    Retrieves the puzzle dictionary for a specific location.
    Returns None if the location doesn't have a puzzle.
    """
    return PUZZLES.get(location_name, None)

def ask_puzzle(location_name):
    """
    Presents the riddle for the given location to the player.
    Allows the player to request a hint or attempt to solve it.
    Returns True if solved correctly, False otherwise.
    """
    puzzle = get_puzzle(location_name)
    
    if not puzzle:
        print(f"\n[!] No puzzle found for {location_name}.")
        return True

    print(f"\n--- PUZZLE: {location_name.upper()} ---")
    print(puzzle["riddle"])
    
    attempts = 2  # Gives the player a chance to use a hint or retry
    
    while attempts > 0:
        user_input = input("\nYour Answer (type 'hint' for a clue): ").strip().lower()
        
        if user_input == "hint":
            print(f"\n💡 Hint: {puzzle['hint']}")
            continue
            
        # Check if the user's cleaned input matches the correct answer
        if user_input == puzzle["answer"]:
            print("\n✨ Correct! You solved the puzzle!")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"\n❌ Incorrect! You have {attempts} attempt(s) left. Try again.")
            else:
                print(f"\n❌ Incorrect! You failed the puzzle.")
                
    return False