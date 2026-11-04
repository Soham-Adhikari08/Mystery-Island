import player
import locations
import inventory
def show_welcome():
    print("\n" + "=" * 45)
    print("          THE MYSTERY ISLAND")
    print("             TREASURE HUNT")
    print("=" * 45)
    print("\nAn ancient treasure lies hidden on this island.")
    print("Explore the island, solve puzzles and collect")
    print("four essential items to unlock the treasure.")
    print("\nBut be careful! You only have three lives.")
    print("=" * 45)
    
def show_menu():
    print("\nWHERE DO YOU WANT TO EXPLORE?")
    print("-" * 35)
    print("1. Dark Forest")
    print("2. Crystal Cave")
    print("3. Abandoned Ship")
    print("4. Ancient Temple")
    print("5. Treasure Chamber")
    print("6. View Inventory")
    print("7. Exit Game")
    print("-" * 35)
    
def show_inventory(inv):
    print("\n========== INVENTORY ==========")

    if len(inv) == 0:
        print("Your inventory is empty.")
    else:
        for item in inv:
            print("- " + item)

    print("===============================")
    
def start_game():
    show_welcome()
    name = player.get_player_name()
    health = 5
    score = 0
    inv = []
    completed_locations = []
    required_items = [
        "Map Fragment",
        "Ancient Key",
        "Treasure Clue",
        "Temple Coordinates"
    ]
    print("\nWelcome, " + name + "!")
    print("Your adventure begins now.")
    game_running = True
    while game_running:
        if health <= 0:
            print("\nGAME OVER!")
            print("You have lost all three lives.")
            print("Final Score:", score)
            break
        player.show_status(health, score, inv)

        show_menu()

        choice = input("\nEnter your choice: ").strip()
        location_options = {
            "1": ("Dark Forest", locations.explore_dark_forest),
            "2": ("Crystal Cave", locations.explore_crystal_cave),
            "3": ("Abandoned Ship", locations.explore_abandoned_ship),
            "4": ("Ancient Temple", locations.explore_ancient_temple)
        }
        if choice in location_options:

            location_name, explore_function = location_options[choice]
            if location_name in completed_locations:
                print("\nYou have already explored this location.")
                continue

            print("\nEntering", location_name, "...")

            old_inventory_count = len(inv)
            health, score = explore_function(health, score, inv)
            if len(inv) > old_inventory_count:
                completed_locations.append(location_name)

        elif choice == "5":
            has_all_items = True
            for item in required_items:
                if not inventory.has_item(inv, item):
                    has_all_items = False
            if has_all_items:
                won, health, score = locations.explore_treasure_chamber(
                    health, score, inv
                )
                if won:
                    print("\n" + "=" * 45)
                    print("       CONGRATULATIONS, " + name.upper() + "!")
                    print("       YOU FOUND THE LEGENDARY TREASURE!")
                    print("=" * 45)
                    print("Final Score:", score)
                    print("Remaining Lives:", health)
                    game_running = False
            else:
                print("\nThe Treasure Chamber is still locked!")
                print("You need to collect all four items:")

                for item in required_items:
                    if not inventory.has_item(inv, item):
                        print("- " + item)
        elif choice == "6":
            show_inventory(inv)
        elif choice == "7":
            print("\nThank you for playing, " + name + "!")
            print("Final Score:", score)
            print("Goodbye, explorer!")
            game_running = False
        else:
            print("\nInvalid choice! Please select 1 to 7.")
    print("\n========== GAME ENDED ==========")

if __name__ == "__main__":
    start_game()
