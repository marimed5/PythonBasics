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

import logging
import datetime

def logger_helper():
        logging.basicConfig(filename='task1.log',
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO)

        return logging.getLogger(__name__)

logger = logger_helper()

# Dictionary
inventory = {}
# Set
category = set()
# List of actions done
actions = []

# Decorator for adding product
def add_decorator(f):
    def wrap(inventory, name, price, quantity):
        logger.info("Before adding product")
        # print("Actions before adding product: ", actions)
        f(inventory, name, price, quantity)
        logger.info("After adding product")
        # print("Actions after adding product: ", actions)
    return wrap

# Decorator for updating stock
def update_decorator(f):
    def wrap(inventory, name, change):
        logger.info("Before updating product")
        # print("Quantity before updating stock: ", inventory[name].quantity)
        f(inventory, name, change)
        logger.info("After updating product")
        # print("Quantity after updating stock: ", inventory[name].quantity)
    return wrap

# Decorator for displaying inventory
def display_decorator(f):
    def wrap(inventory):
        logger.info("Before displaying inventory")
        # print("\nBefore displaying inventory")
        f(inventory)
        logger.info("After displaying inventory")
        # print("After displaying inventory")
    return wrap

# Decorator for removing product
def remove_decorator(f):
    def wrap(inventory, name):
        logger.info("Before removing")
        # print("\nBefore removing product: ", actions)
        f(inventory, name)
        logger.info("After removing product")
        # print("After removing product: ", actions)
    return wrap

# Decorator for searching
def search_decorator(f):
    def wrap(inventory, name):
        logger.info("Before searching product")
        # print("\nBefore searching product")
        f(inventory, name)
        logger.info("After searching product")
        # print("After searching product")
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
        logger.error("Name doesn't exist")
        # print("Name doesn't exist")


# remove_product(inventory, name) → Deletes a product.
@remove_decorator
def remove_product(inventory, name):
    try:
        del inventory[name]
        actions.append("Removed " + name)
    except KeyError:
        logger.error("Name doesn't exist")
        # print("Name doesn't exist")

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
        logger.error("Name doesn't exist")
        # print("Name not found")


quit = False
# Run until user doesn't quit
while not quit:
    # Print menu and take input
    print("1. Add Product\n2. Update Quantity\n3. Remove Product\n4. Display Inventory\n5. Search Product\n6. Exit")
    entry = int(input("Enter your choice: "))

    # Handle different inputs
    if entry == 1:
        name = input("Name: ").lower()
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        add_product(inventory, name, price, quantity)
    elif entry == 2:
        name = input("Name: ").lower()
        change = int(input("Add quantity: "))
        try:
            update_quantity(inventory, name, change)
        except KeyError:
            logger.error("Name doesn't exist")
            # print("Name doesn't exist")
    elif entry == 3:
        name = input("Name: ").lower()
        remove_product(inventory, name)
    elif entry == 4:
        display_inventory(inventory)
    elif entry == 5:
        name = input("Name: ").lower()
        search_product(inventory, name)
    elif entry == 6:
        # Create tuple of last three actions, print, and exit
        if len(actions) >= 3:
            lastThree = (actions.pop(), actions.pop(), actions.pop())
            logger.info(f"Last three actions: {lastThree}")
            # print("Last three actions: ", lastThree)
        else:
            logger.info(f"Last actions were: {actions}")
            # print("Last actions were: ", actions)
        quit = True
        break
    else:
        logger.error("Invalid choice")
        # print("Invalid input. Try again.")
        continue

    # Debug
    logger.debug("\nDebugging\n\tCategories: ", category)
    logger.debug("\tActions done: ", actions)
    # print ("\nDebugging\n\tCategories: ", category)
    # print ("\tActions done: ", actions, "\n")