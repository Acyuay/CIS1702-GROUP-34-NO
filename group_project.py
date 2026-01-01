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

def add_item(new_item, inventory):


def view_stock(item):

def update_item(item, stock):

def search_item(item):

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
        user_choice = input("Do you want to Add item, view stock, update item, search or save and exit? (first word of action) ").lower()
        if user_choice == "add":
            add_item()
            break
        elif user_choice == "view":
            view_stock()
            break
        elif user_choice == "update":
            update_item()
            break
        elif user_choice == "search":
            search_item()
            break
        elif user_choice == "save":
            save_exit()
            break
        else:
            print("Invalid input please try again")
        return

