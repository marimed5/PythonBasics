
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # Print out function
    def display_info(self):
        print("Name: " + self.name)
        print("Price: " + self.price)
        print("Quantity: " + self.quantity)

# Dictionary
inventory = {}
# Set
category = set()
# List of actions done
actions = []

# Decorator for adding product
def add_decorator(f):
    def wrap(inventory, name, price, quantity):
        print("Actions before adding product: ", actions)
        f(inventory, name, price, quantity)
        print("Actions after adding product: ", actions)
    return wrap

# Decorator for updating stock
def update_decorator(f):
    def wrap(inventory, name, change):
        print("Quantity before updating stock: ", inventory[name].quantity)
        f(inventory, name, change)
        print("Quantity after updating stock: ", inventory[name].quantity)
    return wrap

# Decorator for displaying inventory
def display_decorator(f):
    def wrap(inventory):
        print("\nBefore displaying inventory")
        f(inventory)
        print("After displaying inventory")
    return wrap

# Decorator for removing product
def remove_decorator(f):
    def wrap(inventory, name):
        print("\nBefore removing product: ", actions)
        f(inventory, name)
        print("After removing product: ", actions)
    return wrap

# Decorator for searching
def search_decorator(f):
    def wrap(inventory, name):
        print("\nBefore searching product")
        f(inventory, name)
        print("After searching product")
    return wrap

# add_product(inventory, name, price, quantity) → Adds a new product.
@add_decorator
def add_product(inventory, name, price, quantity):
    inventory[name] = Product(name, price, quantity)

    currCategory = input("Enter product category: ")
    if currCategory not in category:
        category.add(currCategory)

    actions.append(f'Added {name}')

# update_quantity(inventory, name, change) → Adjusts stock (+/-).
@update_decorator
def update_quantity(inventory, name, change):
    try:
        inventory[name].quantity += change
        actions.append("Updated Stock")
    except KeyError:
        print("Name doesn't exist")


# remove_product(inventory, name) → Deletes a product.
@remove_decorator
def remove_product(inventory, name):
    try:
        del inventory[name]
        actions.append("Removed " + name)
    except KeyError:
        print("Name doesn't exist")

# display_inventory(inventory) → Prints all products.
@display_decorator
def display_inventory(inventory):
    for item in inventory:
        print(f'Name: {inventory[item].name}, Price: {inventory[item].price}, Quantity: {inventory[item].quantity}')

# search_product(inventory, name) → Shows product details if found.
@search_decorator
def search_product(inventory, name):
    try:
        print(f'Item found:\nName: {name}, Price: {inventory[name].price}, Quantity: {inventory[name].quantity}')
    except KeyError:
        print("Name not found")


quit = False
# Run until user doesn't quit
while not quit:
    # Print menu and take input
    print("1. Add Product\n2. Update Quantity\n3. Remove Product\n4. Display Inventory\n5. Search Product\n6. Exit")
    entry = int(input("Enter your choice: "))

    # Handle different inputs
    if entry == 1:
        name = input("Name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        add_product(inventory, name, price, quantity)
    elif entry == 2:
        name = input("Name: ")
        change = int(input("Add quantity: "))
        try:
            update_quantity(inventory, name, change)
        except KeyError:
            print("Name doesn't exist")
    elif entry == 3:
        name = input("Name: ")
        remove_product(inventory, name)
    elif entry == 4:
        display_inventory(inventory)
    elif entry == 5:
        name = input("Name: ")
        search_product(inventory, name)
    elif entry == 6:
        # Create tuple of last three actions, print, and exit
        lastThree = (actions.pop(), actions.pop(), actions.pop())
        print("Last three actions: ", lastThree)
        quit = True
        break
    else:
        print("Invalid input. Try again.")
        continue

    # Debug
    print ("\nDebugging\n\tCategories: ", category)
    print ("\tActions done: ", actions, "\n")