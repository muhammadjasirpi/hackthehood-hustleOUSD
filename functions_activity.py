# Menu dictionary
menu = {'Pizza': 2.99, 'Burger': 3.99, 'Hot dog': 1.99, 'Cheese': 0.59, 'Ice cream': 1.49, 'Churro': 0.79, 'Soda': 0.89}

def total_price(*items):
    """Calculate total price of menu items"""
    if not items:
        return "Error: No items provided"
    
    total = 0
    for item in items:
        if item not in menu:
            return f"Error: {item} not on menu"
        total += menu[item]
    
    item_list = " and ".join(items)
    return f"The total price of {item_list} is ${total:.2f}"

def price_difference(item1, item2):
    """Calculate price difference between two items"""
    if item1 not in menu:
        return f"Error: {item1} not on menu"
    if item2 not in menu:
        return f"Error: {item2} not on menu"
    
    difference = abs(menu[item1] - menu[item2])
    return f"The difference between {item1} and {item2} is ${difference:.2f}"

def inflation(item, multiplier):
    """Multiply item price and return updated menu"""
    if item not in menu:
        return f"Error: {item} not on menu"
    
    updated_menu = menu.copy()
    updated_menu[item] = round(menu[item] * multiplier, 2)
    return updated_menu

def deflation(item, divisor):
    """Divide item price and return updated menu"""
    if item not in menu:
        return f"Error: {item} not on menu"
    
    updated_menu = menu.copy()
    updated_menu[item] = round(menu[item] / divisor, 2)
    return updated_menu

def loyalty_discount(item, visits):
    """Custom function using modulus for loyalty discount"""
    if item not in menu:
        return f"Error: {item} not on menu"
    
    # Every 3 visits gets 10% discount
    if visits % 3 == 0 and visits > 0:
        discounted_price = menu[item] * 0.9
        return f"{item} loyalty price: ${discounted_price:.2f} (10% off!)"
    else:
        return f"{item} regular price: ${menu[item]:.2f}"

# Test the functions
if __name__ == "__main__":
    print("Menu:", menu)
    print()
    
    print(total_price('Pizza', 'Burger'))
    print(price_difference('Burger', 'Pizza'))
    
    inflated = inflation('Pizza', 1.5)
    print(f"After inflation: Pizza = ${inflated['Pizza']}")
    
    deflated = deflation('Burger', 2)
    print(f"After deflation: Burger = ${deflated['Burger']}")
    
    print(loyalty_discount('Pizza', 6))
    print(loyalty_discount('Pizza', 5))