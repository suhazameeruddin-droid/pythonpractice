def add_menu_item(menu, item):
    menu.append(item)
    return menu

def remove_menu_item(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(f"{item} not found in the menu.")
    return menu

def check_availability(menu, item):
    if item in menu:
        return f"{item} is available"
    else:
        return f"{item} is not available"

# Example input
initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item = "Tacos"
remove_item = "Salad"
check_item = "Pizza"

# Operations
menu = add_menu_item(initial_menu, add_item)
menu = remove_menu_item(menu, remove_item)
availability = check_availability(menu, check_item)

# Output
print("Updated menu:", menu)
print("Availability:", availability)
