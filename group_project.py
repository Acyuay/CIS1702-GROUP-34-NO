import json

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
    product_id = input("Please enter the product id:") #Input function for the user to add the products id
    product_name = input("Please enter the product name:") #Input function for the user to add the products name
    try:
        product_price = float(input("Please enter the product's price: £")) #float is telling python input as a number with decimals
        product_quantity = int(input("Please enter the products quantity:"))
    except ValueError: #If there is a error with the input value print the next line of code
        print("Invalid price and/or quantity provided")
        return #returns the result to the global.
    
    for item in inventory: #This is a loop to go through every item in inventory 1 at a time
        if item ["id"] == product_id:
            item ["quantity"] += product_quantity
            print(f"Restocking of {item["Name"]} completed.  (New stock:  {item["Quantity"]})")
            return

    inventory.append({
        "id": product_id,
        "Name": product_name,
        "Price": product_price,
        "Quantity": product_quantity
    })
    print("---The item has been added successfully---")

def view_stock(inventory):  #this function of the code allows the user to view the stock in the inventory
    if not inventory:                   
        print("The inventory is empty.")    #L40 is if the item is not found in the inventory, then a message will display to the user showing that the inventory is empty
        return
    print("\nCurrent Stock:")   #L42 shows the quantity of the stock in the inventory 
    for item in inventory:              
        print(f"ID: {item['id']}")  #L44 prints the items id for the user 
        print(f"Name: {item['name']}")  #L45 prints the item's name 
        print(f"Price: £{item['price']}")  #L46 prints the price of the item 
        print(f"Quantity: {item['quantity']}") #L47 will print the quantity of the items 
    

def update_item(item, inventory):
   item_id = input("enter item id: ")
   for item in inventory:                 #L39-43 finding item nanme by its id and details
       if item["id"] == item_id:
            print("\nitem found: ")
            print(f"item name: {item['name']}")
            print(f"item priice: {item['price']}")
            print(f"item quantity: {item['quantity']}")
            choice = input("do you want to update this item? (y/n): ")  #comfirms item to update
            if choice.lower() != 'y':
                print("returing to menu")               #goes back to menu
                return
            if choice.lower()== 'y':                   # right it contiunes the update
                choice = input("whaat would you like to upadate? (name/price/quantity):")
                if choice.lower() == 'name':
                    new_name = input(print(f"enter new name:"))
                    item['name'] = new_name  
            elif choice.lower() == 'price':
                try:
                    new_price = float(input(print(f"Enter new price: ")))   # converts str -> decimal
                    item['price']= new_price
                except ValueError:
                    print(f"invalid input please try again")
                    return
            elif choice.lower() == 'quantity':
                try:
                    new_quantity = int(input(print(f"enter new quantity: ")))  # int converts string to number
                    item['quantity'] = new_quantity
                except ValueError:
                    print(f"invalid input please try again")
                    return

def search_item(item, inventory):
     item_id = input("enter item id: ")
     for item in inventory:
         if item["id"] == item_id:
            print("\nitem found: ")
            print(f"item name: {item['name']}")
            print(f"item priice: {item['price']}")
            print(f"item quantity: {item['quamtity']}")
            return
         else:
           print("item not found")
           return

def low_stock_report(inventory):
    try:
        threshold = int(input("Enter low stock threshold: ")) #allows user to enter custom stock threshold
    except ValueError:
        print("Invalid number entered.")
        return

    low_stock_items = [] #creates an empty list to append the low stock items to

    for item in inventory: #loop iterates to find all the items below the threshold quantity
        if item["Quantity"] <= threshold:
            low_stock_items.append(item)

    if not low_stock_items: 
        print("No items are low in stock.")
        return

    print("\n--- Low Stock Report ---") #prints the low stock items out with id, name and quantity
    for item in low_stock_items:
        print(f"ID: {item['id']}")
        print(f"Name: {item['Name']}")
        print(f"Quantity: {item['Quantity']}")
        print("-" * 20)
           
def save_exit(inventory):
    try:
        with open(f{inventory}, "w") as file:
            json.dump(inventory, file, indent=4)
        print(f"Successfully saved inventory to {inventory}") # print confirmation message
    except FileNotFoundError:
        print("No save file found. Starting fresh.")
        return [] # Return an empty list

def display_menu():
    print("\nInventory system")        #/n for new line each print
    print("1. Add item")
    print("2. View stock")
    print("3. Update")
    print("4. Search")
    print("5. Low stock report")
    print("6. Save and exit")


def main():
    inventory = load_inventory("inventory.json")
    while True:
        user_choice = input("Choose an option: ")
        if user_choice == "1":
            add_item(inventory)
            break
        elif user_choice == "2":
            view_stock(inventory)
            break
        elif user_choice == "3":
            update_item(inventory)
            break
        elif user_choice == "4":
            search_item(inventory)
            break
        elif user_choice == "5":
            
            break
        elif user_choice == "6":
            save_exit(inventory)
            break
        else:
            print("Invalid input please try again")
        return

