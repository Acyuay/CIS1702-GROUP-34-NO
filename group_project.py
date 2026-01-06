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
    product_id = input("Please enter the product id:")
    product_name = input("Please enter the product name:")
    try:
        product_price = float(input("Please enter the product's price:"))
        product_quantity = int(input("Please enter the products quantity:"))
    except ValueError:
        print("Invalid price and/or quantity provided")
        return
    
    for item in inventory:
        if item ["id"] == product_id:
            item ["quantity"] += product_quantity
            print(f"Restocking of {item["Name"]}  (New stock:  {item["Quantity"]})")
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
            print(f"item quantity: {item['quamtity']}")
            choice = input("do you want to update this item? (y/n): ")  #comfirms item to update
            if choice.lower() != 'y':
                print("returing to menu")               #goes back to menu
                return
            if choice.lower()== 'y':                   # right it contiunes the update
                choice = input("whaat would you like to upadate? (neam/price/quantity):")
                if choice.lower() == 'name':
                    new_name = input(print(f"enter ne name:"))
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

def search_item(item):

def display_menu():
    print("\nInventory system")        #/n for new line each print
    print("1. Add item")
    print("2. View stock")
    print("3. Update")
    print("4. Search")
    print("5. save and exit")

def save_exit(inventory):
    with open(filename, "w") as file:
        json.dump(inventory, file, indent=4)
        print(f"successfully saved inventory to{filename}")
    return True
    except Exception as e:
        print(f"there was an error while saving {filename}:{e}")
    return False



def main():
    inventory = load_inventory("inventory.json")
    while True:
        user_choice = input("Choose an option: ")
        if user_choice == "1":
            add_item()
            break
        elif user_choice == "2":
            view_stock()
            break
        elif user_choice == "3":
            update_item()
            break
        elif user_choice == "4":
            search_item()
            break
        elif user_choice == "5":
            save_exit()
            break
        else:
            print("Invalid input please try again")
        return

