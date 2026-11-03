# inventory.py
# Adds, removes and displays collected items

def add_item(inventory_list, item_name):
    """Adds a newly found object to the inventory list."""
    inventory_list.append(item_name)
    print(f"\nYou discovered a {item_name}!")
    print("Item added to inventory.")
    return inventory_list