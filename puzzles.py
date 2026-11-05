# puzzles.py - Stores riddles, hints, and answer-checking logic for Mystery Island

PUZZLES = {
    "Dark Forest": {
        "riddle": "I have roots as nobody sees, higher than trees, up and up I go, and yet I never grow. What am I?",
        "options": ["1. A Mountain", "2. A River", "3. A Cloud"],
        "hint": "Think about something tall and rocky that touches the clouds.",
        "answer": "1",
        "word_answer": "mountain"
    },
    "Crystal Cave": {
        "riddle": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
        "options": ["1. A Shadow", "2. An Echo", "3. A Whisper"],
        "hint": "You can hear me bounce back when you shout in an empty canyon.",
        "answer": "2",
        "word_answer": "echo"
    },
    "Abandoned Ship": {
        "riddle": "I have keys but no locks. I have space but no room. You can enter, but you can't go outside. What am I?",
        "options": ["1. A Keyboard", "2. A Door", "3. A Treasure Chest"],
        "hint": "You use me every day when you type out code on a computer.",
        "answer": "1",
        "word_answer": "keyboard"
    },
    "Ancient Temple": {
        "riddle": "What has to be broken before you can use it?",
        "options": ["1. A Lock", "2. A Mirror", "3. An Egg"],
        "hint": "You usually crack this open in the morning for breakfast.",
        "answer": "3",
        "word_answer": "egg"
    },
    "Treasure Chamber": {
        "riddle": "FINAL TRIAL: I am full of holes, yet I still hold a lot of water. What am I?",
        "options": ["1. A Net", "2. A Sponge", "3. A Bucket"],
        "hint": "It's a soft, absorbent cleaning tool you use in the kitchen or bathroom.",
        "answer": "2",
        "word_answer": "sponge"
    }
}


def get_puzzle(location_name):
    """Retrieves the puzzle dictionary for a specific location."""
    return PUZZLES.get(location_name, None)


def check_answer(user_input, correct_answer, word_answer=None):
    """
    Checks whether the player's answer matches the correct option number or word.
    Returns True if correct, False otherwise.
    """
    cleaned = str(user_input).strip().lower()
    target = str(correct_answer).strip().lower()

    if cleaned == target:
        return True
    if word_answer and cleaned == str(word_answer).strip().lower():
        return True
    return False


def ask_puzzle(question_or_location, options=None, correct_answer=None, hint=None):
    """
    Works in two ways:
    1. Called from locations.py with 4 arguments: ask_puzzle(question, options, correct_answer, hint)
    2. Called with 1 argument (location name): ask_puzzle("Dark Forest")
    Returns True if solved correctly, False otherwise.
    """
    word_answer = None

    # Case 1: Only a location name was passed (1 argument)
    if options is None and correct_answer is None:
        puzzle = get_puzzle(question_or_location)
        if not puzzle:
            print(f"\n[!] No puzzle found for {question_or_location}.")
            return True
        question = puzzle["riddle"]
        options = puzzle["options"]
        correct_answer = puzzle["answer"]
        hint = puzzle.get("hint", "No hint available.")
        word_answer = puzzle.get("word_answer", None)
    # Case 2: All 4 arguments were passed directly from locations.py
    else:
        question = question_or_location
        if not hint:
            hint = "Look closely at the options and think carefully!"

    print(f'\n"{question}"\n')

    # Print options whether passed as a list/tuple or a single string
    if isinstance(options, (list, tuple)):
        for i, opt in enumerate(options, start=1):
            opt_str = str(opt)
            # Add numbering (1., 2., 3.) only if not already numbered
            if opt_str.strip().startswith(f"{i}.") or opt_str.strip().startswith(f"{i})"):
                print(opt_str)
            else:
                print(f"{i}. {opt_str}")
    elif options:
        print(options)

    attempts = 2  # Gives the player a chance to use a hint or retry

    while attempts > 0:
        user_input = input("\nYour Answer (enter choice or type 'hint' for a clue): ").strip().lower()

        if user_input == "hint":
            print(f"\n💡 Hint: {hint}")
            continue

        if check_answer(user_input, correct_answer, word_answer):
            print("\n✨ CORRECT ANSWER! You solved the puzzle!")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"\n❌ Incorrect! You have {attempts} attempt(s) left. Try again.")
            else:
                print("\n❌ Incorrect! You failed the puzzle.")

    return False