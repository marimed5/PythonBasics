
class Product:
    def __init__(self, name, price, quantity):
        self.name = str(name)
        self.price = float(price)
        self.quantity = int(quantity)

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

# add_product(inventory, name, price, quantity) → Adds a new product.
def add_product(inventory, name, price, quantity):
    inventory[name] = Product(name, price, quantity)

    currCategory = str(input("Enter product category: "))
    if currCategory not in category:
        category.add(currCategory)

    actions.append(f'Added {name}')

# update_quantity(inventory, name, change) → Adjusts stock (+/-).
def update_quantity(inventory, name, change):
    if name in inventory:
        inventory[name].quantity += change
        actions.append("Updated Stock")
    else:
        print("Name doesn't exist")


# remove_product(inventory, name) → Deletes a product.
def remove_product(inventory, name):
    if name in inventory:
        del inventory[name]
        actions.append("Removed " + name)
    else:
        print("Name doesn't exist")

# display_inventory(inventory) → Prints all products.
def display_inventory(inventory):
    for key, value in inventory.items():
        print(f'Key: {key}, Value: {value}')

# search_product(inventory, name) → Shows product details if found.
def search_product(inventory, name):
    if name in inventory:
        print(f'Name: {name}, Price: {inventory[name].price}, Quantity: {inventory[name].quantity}')
    else:
        print("Name not found")


quit = False
# Run until user doesn't quit
while not quit:
    # Print menu and take input
    print("1. Add Product\n2. Update Quantity\n3. Remove Product\n4. Display Inventory\n5. Search Product\n6. Exit")
    entry = int(input("Enter your choice: "))

    # Handle different inputs
    if entry == 1:
        name = str(input("Name: "))
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        add_product(inventory, name, price, quantity)
    elif entry == 2:
        name = str(input("Name: "))
        change = int(input("Add quantity: "))
        update_quantity(inventory, name, change)
    elif entry == 3:
        name = str(input("Name: "))
        remove_product(inventory, name)
    elif entry == 4:
        display_inventory(inventory)
    elif entry == 5:
        name = str(input("Name: "))
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
    print ("\tCategories: ", category)
    print ("\tActions done: ", actions)