# inventory.py
# Adds, removes and displays collected items

def add_item(inventory_list, item_name):
    """Adds a newly found object to the inventory list if it isn't already there."""
    if item_name not in inventory_list:
        inventory_list.append(item_name)
        print(f"\nYou discovered a {item_name}!")
        print("Item added to inventory.")
    else:
        print(f"\nYou already have the {item_name} in your inventory.")
        
    return inventory_list