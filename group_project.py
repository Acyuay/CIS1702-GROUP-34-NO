import json

"""
This is our inventory system that is capable of adding items, viewing the stock
updating the stock, searching the stock, generating low stock reports and saving the data to a json file
"""
def load_inventory(filename):
    #Basic loading inventory to file and crash protection
    try:
        with open(f"{filename}", "r+") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def add_item(inventory):
    """Add a new item to the inventory."""
    product_id = input("Please enter the product id:").strip() #Input function for the user to add the products id
    product_name = input("Please enter the product name:").strip() #Input function for the user to add the products name
    
    for item in inventory:
        if str(item["id"]).strip() == product_id:
            print("Error: An item with this ID already exists.")
            return
        if item["name"].strip().lower() == product_name.lower():
            print("Error: An item with this name already exists.")
            return
    try:
        product_price = float(input("Please enter the product's price: £")) #float is telling python input as a number with decimals
        product_quantity = int(input("Please enter the products quantity:"))
    except ValueError: #If there is a error with the input value print the next line of code
        print("Invalid price and/or quantity provided")
        return #returns the result to the global.   

    inventory.append({
        "id": product_id,
        "name": product_name,
        "price": product_price,
        "quantity": product_quantity
    })
    print("---The item has been added successfully---")

def view_stock(inventory):  #this function of the code allows the user to view the stock in the inventory
    if not inventory:                   
        print("The inventory is empty.")    #L44 is if the item is not found in the inventory, then a message will display to the user showing that the inventory is empty
        return
    print("\nCurrent Stock:")   #L46 shows the quantity of the stock in the inventory 
    for item in inventory:              
        print(f"ID: {item['id']}")  #L48 prints the items id for the user 
        print(f"Name: {item['name']}")  #L49 prints the item's name 
        print(f"Price: £{item['price']}")  #L50 prints the price of the item 
        print(f"Quantity: {item['quantity']}") #L51 will print the quantity of the items 
        print("-" * 20) #prints 20 - out for formatting so it looks neater 

def update_item(inventory):
    item_id = input("enter item id: ")

    for item in inventory:
        if str(item["id"]) == str(item_id):
            print("\nItem found:")
            print(f"Item name: {item['name']}")
            print(f"Item price: {item['price']}")
            print(f"Item quantity: {item['quantity']}")                #edited function similar to search function  

            confirm = input("do you want to update this item? (y/n): ")
            if confirm.lower() != 'y':
                print("returning to menu")
                return

            choice = input("what would you like to update? (name/price/quantity): ").lower()  #allows user to pick option

            if choice == 'name':
                item['name'] = input("enter new name: ")

            elif choice == 'price':
                try:
                    item['price'] = float(input("enter new price: "))  # converts str - decimal 
                except ValueError:
                    print("invalid price")
                    return

            elif choice == 'quantity':
                try:
                    item['quantity'] = int(input("enter new quantity: "))     # converts str - whole number
                except ValueError:
                    print("invalid quantity")
                    return

            print("Item updated successfully!")
            return

    print("Item not found")

def search_item(inventory):
    item_id = input("enter item id: ")     
    for item in inventory:
        if str(item["id"]) == str(item_id): #converts both to string otherwise will always not find the item
            print("\nitem found: ")
            print(f"item name: {item['name']}")
            print(f"item price: {item['price']}")
            print(f"item quantity: {item['quantity']}")
            return

    print("Item not found")

def low_stock_report(inventory):
    try:
        threshold = int(input("Enter low stock threshold: ")) #allows user to enter custom stock threshold
    except ValueError:
        print("Invalid number entered.")
        return

    low_stock_items = [] #creates an empty list to append the low stock items to

    for item in inventory: #loop iterates to find all the items below the threshold quantity
        if item["quantity"] <= threshold:
            low_stock_items.append(item)

    if not low_stock_items: 
        print("No items are low in stock.")
        return

    print("\n--- Low Stock Report ---") #prints the low stock items out with id, name and quantity
    for item in low_stock_items:
        print(f"ID: {item['id']}")
        print(f"Name: {item['name']}")
        print(f"Quantity: {item['quantity']}")
        print("-" * 20) #prints 20 - out for formatting to look neater 

def save_exit(inventory):
    try:
        with open("inventory.json", "w") as f:
            json.dump(inventory, f, indent=4)
        print(f"Successfully saved inventory to inventory") # print confirmation message
    except FileNotFoundError:
        print("No save file found. Starting fresh.")
        return [] # Return an empty list

def display_menu():
    print("\n---Inventory system---")        #/n for new line each print
    print("1. Add item")
    print("2. View stock")
    print("3. Update")
    print("4. Search")
    print("5. Low stock report")
    print("6. Save and exit")

def main():
    inventory = load_inventory("inventory.json")
    while True:
        display_menu()
        user_choice = input("Choose an option: ")
        if user_choice == "1":
            add_item(inventory)
        elif user_choice == "2":
            view_stock(inventory)
        elif user_choice == "3":
            update_item(inventory)
        elif user_choice == "4":
            search_item(inventory)
        elif user_choice == "5":
            low_stock_report(inventory)
        elif user_choice == "6":
            save_exit(inventory)
            break  #only one with break so the code loops until you want to save and exit
        else:
            print("Invalid input please try again")
    return

main()