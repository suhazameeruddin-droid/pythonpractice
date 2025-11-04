def calculate_total(cart_items):
    # Check if the cart is empty
    if not cart_items:
        return "Cart is empty."

    # Calculate total price
    total = sum(cart_items.values())

    # Apply 10% discount if more than 5 items
    if len(cart_items) > 5:
        total *= 0.9  # Apply 10% discount

    return f"Total Price: {int(total)}"


# Example input
cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}

# Output
print(calculate_total(cart_items))
