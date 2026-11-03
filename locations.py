import puzzles
import inventory
import scoring

def explore_dark_forest(health, score, inv):
    print("\n=== 1. DARK FOREST ===")
    print("The trees are thick and block out the sun. A mysterious voice whispers a riddle...")
    
    question = "I have keys but open no locks. I have space but no room. You can enter but cannot go outside. What am I?"
    options = ["1. A Keyboard", "2. A Door", "3. A Treasure Chest"]
    hint = "You are likely using one right now to write your Python code."
    
    is_correct = puzzles.ask_puzzle(question, options, 1, hint)
    
    if is_correct:
        print("CORRECT ANSWER!")
        score = scoring.calculate_score(score, 20)
        inventory.add_item(inv, "Map Fragment")
    else:
        print("WRONG ANSWER! The forest spirits attack you.")
        health = scoring.lose_life(health)
        
    return health, score

def explore_crystal_cave(health, score, inv):
    print("\n=== 2. CRYSTAL CAVE ===")
    print("Beautiful glowing crystals light up the cave, but the floor is slippery.")
    
    question = "What is always in front of you but can't be seen?"
    options = ["1. The Sun", "2. The Future", "3. Your Nose"]
    hint = "It is related to time."
    
    is_correct = puzzles.ask_puzzle(question, options, 2, hint)
    
    if is_correct:
        print("CORRECT ANSWER! You safely cross the cave.")
        score = scoring.calculate_score(score, 20)
        inventory.add_item(inv, "Ancient Key")
    else:
        print("WRONG ANSWER! You slip and fall on the sharp crystals.")
        health = scoring.lose_life(health)
        
    return health, score

def explore_abandoned_ship(health, score, inv):
    print("\n=== 3. ABANDONED SHIP ===")
    print("You find an old pirate ship stuck on the rocks. You find a captain's diary.")
    
    question = "What has to be broken before you can use it?"
    options = ["1. A Glass", "2. An Egg", "3. A Promise"]
    hint = "It is often eaten for breakfast."
    
    is_correct = puzzles.ask_puzzle(question, options, 2, hint)
    
    if is_correct:
        print("CORRECT ANSWER! You decoded the message.")
        score = scoring.calculate_score(score, 20)
        inventory.add_item(inv, "Treasure Clue")
    else:
        print("WRONG ANSWER! A ghost pirate scares you away.")
        health = scoring.lose_life(health)
        
    return health, score

def explore_ancient_temple(health, score, inv):
    print("\n=== 4. ANCIENT TEMPLE ===")
    print("You enter a huge stone temple filled with logic traps.")
    
    question = "If you drop me I'm sure to crack, but give me a smile and I'll always smile back. What am I?"
    options = ["1. A Mirror", "2. A Phone", "3. A Friend"]
    hint = "It reflects your image."
    
    is_correct = puzzles.ask_puzzle(question, options, 1, hint)
    
    if is_correct:
        print("CORRECT ANSWER! A hidden door opens.")
        score = scoring.calculate_score(score, 20)
        inventory.add_item(inv, "Temple Coordinates")
    else:
        print("WRONG ANSWER! A trap triggers and hits you.")
        health = scoring.lose_life(health)
        
    return health, score

def explore_treasure_chamber(health, score, inv):
    print("\n=== 5. TREASURE CHAMBER ===")
    
    has_map = inventory.has_item(inv, "Map Fragment")
    has_key = inventory.has_item(inv, "Ancient Key")
    has_clue = inventory.has_item(inv, "Treasure Clue")
    has_coords = inventory.has_item(inv, "Temple Coordinates")
    
    if has_map and has_key and has_clue and has_coords:
        print("You place all 4 items on the pedestal. The grand door unlocks!")
        
        question = "FINAL PASSWORD: I am tall when I'm young, and I'm short when I'm old. What am I?"
        options = ["1. A Tree", "2. A Candle", "3. A Human"]
        hint = "It is made of wax and produces light."
        
        is_correct = puzzles.ask_puzzle(question, options, 2, hint)
        
        if is_correct:
            print("THE TREASURE IS YOURS!")
            score = scoring.calculate_score(score, 100)
            return True, health, score
        else:
            print("WRONG PASSWORD! The chamber shakes violently!")
            health = scoring.lose_life(health)
            return False, health, score
    else:
        print("The door is locked tight.")
        print("You need 4 items to enter: Map Fragment, Ancient Key, Treasure Clue, and Temple Coordinates.")
        return False, health, score
