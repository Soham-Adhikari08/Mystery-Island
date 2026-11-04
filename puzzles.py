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


def ask_puzzle(question, options, correct_answer, hint):

    print("\n--- PUZZLE ---")
    print(question)

    for option in options:
        print(option)

    attempts = 2

    while attempts > 0:

        answer = input("\nYour answer (or type 'hint'): ").strip().lower()

        if answer == "hint":
            print("\nHint:", hint)
            continue

        # Accept either the option number or answer text
        if answer == str(correct_answer):
            print("\nCorrect! You solved the puzzle!")
            return True

        # Also accept the actual answer text
        correct_option = options[correct_answer - 1]
        correct_text = correct_option.split(". ", 1)[-1].lower()

        if answer == correct_text:
            print("\nCorrect! You solved the puzzle!")
            return True

        attempts -= 1

        if attempts > 0:
            print("Incorrect! Try again.")
        else:
            print("You failed the puzzle.")

    return False
