# This creates a dictionary called 'inventory' to store products.
inventory = {}

# This defines a function to add a new product.
def add_product (inventory):
    # Loop to get a valid product name with only letters and spaces.
    while True:
        name = input('Enter the product name:').strip().lower()
        valid = all(char.isalpha() or char == ' ' for char in name)
        print(f'{valid} first') # For debugging
        if valid and name != '':
            print(f'{valid} second') # For debugging
            break
        else:
            print('Product name must have only letters and spaces')
    try:
        # Check if the product already exists.
        if name in inventory:
            print(f'Product {name} exists, use option 3 to update')
        else:
            # Get product price and quantity.
            price = float(input('Enter the price:'))
            quantity = int (input('Enter the quantity:'))
            # Store the product info in the inventory dictionary.
            inventory[name]={'price': price, 'quantity':quantity}
            print(f'Product {name} added successfully')
    except ValueError:
        print('Invalid input, enter numbers for price and quantity')

    # Loop to ask if the user wants to add another product.
    while True:
        continue_adding = input ('Add another product? (Yes/No):') .strip() .lower()
        if continue_adding == 'yes':
            break
        elif continue_adding == 'no':
            print('Returning to the menu')
            return
        else:
            print('Incorrect answer, use Yes/No')

# This defines a function to look up a product.
def consult_product (inventory):
    product_name = input('Enter the product name to search: ') .strip() .lower()
    # Check if the product is in the inventory.
    if product_name in inventory:
        product_data = inventory [product_name]
        price = product_data ['price']
        quantity = product_data ['quantity']
        print (f'Product {product_name} is in stock')
        print (f'Price: {price}')
        print (f'Quantity available: {quantity}')
    else:
        print (f'Product {product_name} not found')

# This defines a function to change the price of a product.
def update_price (inventory):
    product_name = input('Enter the product name to update: ')
    # Check if the product exists.
    if product_name in inventory: # Evaluates to True if the product is a key in the dictionary
       try:
           new_price = float (input ('Enter the new price: '))
           # Ensure the new price is not negative.
           if new_price < 0 :
               print ('Enter a positive value')
               return
           # Update the price in the inventory.
           inventory[product_name]['price'] = new_price # Access the 'price' key of the product's dictionary
           print(f'{product_name} price updated')
       except ValueError:
           print(f"Invalid input, enter a valid number")
    else:
        print(f'Product {product_name} does not exist')

# This defines a function to remove a product.
def delete_product (inventory):
    product_name = input('Enter the product name to delete: ')
    # Check if the product exists.
    if product_name in inventory:
        # 'del' keyword removes the product from the dictionary.
        del inventory[product_name]
        print(f'{product_name} Deleted successfully')
    else:
        print(f'Product {product_name} does not exist')

# This defines a function to calculate the total value of all products.
def total_inventory_value (inventory):
    # A small function to multiply price by quantity for a product.
    calculate_value = lambda product:product['price'] * product['quantity']
    total_value = 0
    # Go through each product's information in the inventory.
    for product in inventory.values():
        # Add the value of the current product to the total.
        total_value += calculate_value(product)
    print(f'Total inventory value: ${total_value:.2f}')

# This defines a function to show the menu and get the user's choice.
def show_menu_and_get_option():
    print("\n===== Inventory Menu =====")
    print("1. Add a product")
    print("2. Consult a product")
    print("3. Update product price")
    print("4. Delete a product")
    print("5. Calculate total inventory value")
    print("6. Exit")
    return input("Select an option (1-6): ")

# This is the main part of the program that runs the menu.
def main():
    # Keep showing the menu until the user chooses to exit.
    while True:
        option = show_menu_and_get_option()

        # Perform action based on the user's choice.
        if option == "1":
            add_product(inventory)
        elif option == "2":
            consult_product(inventory)
        elif option == "3":
            update_price(inventory)
        elif option == "4":
            delete_product(inventory)
        elif option == "5":
            total_inventory_value(inventory)
        elif option == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option, select from the menu (1-6)")

# Start the program by calling the main function.
main ()
