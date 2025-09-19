# This script provides an interactive menu for managing a shopping list. The core of the application is a Python list named shopping_list.

import os

def menu():
    print("\n---- 🛒 Shopping Menu ----")
    print("1. View Shopping List")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Clear All")
    print("5. Quit")
    print("-------------------------")

def view(shop_list):
    os.system('cls' if os.name=='nt' else 'clear')
    print("---- Your Shopping List ----")
    if not shop_list:
        print("Your list is empty. 🫢")
    else:
        for i, item in enumerate(shop_list,start=1):
            print(f"{i}.{item}")
    print("----------------------------")

def add(shop_list):
    item=input("Enter item you want to add : ")
    if item:
        shop_list.append(item)
        print(f"{item} has been added to your list. ☑️")
    else:
        print("You did not enter an item. ")

def remove(shop_list):
    view(shop_list)

    if not shop_list:
        return

    try:
        item_num=int(input("Enter the number of item to remove : "))
        if 1<=item_num<=len(shop_list):
            removed=shop_list.pop(item_num-1)
            print(f"'{removed}' has been successfully removed from list. ❌")
        else:
            print("Invalid number. Please Choose number from list.")

    except ValueError:
        print("Invalid input. Please enter a number.")

def clear(shop_list):
    if shop_list:
        confirm=input("Are you sure you want to clear list? (y/n) : ").lower()
        if confirm=='y':
            shop_list.clear()
            print("List has been cleared.")
        else:
            print("Action cancelled.")

def main():
    shop_list=[]

    while True:
        menu()
        choice=input("Enter your choice(1-5) : ")

        if choice=='1':
            view(shop_list)
        elif choice=='2':
            add(shop_list)
        elif choice=='3':
            remove(shop_list)
        elif choice=='4':
            clear(shop_list)
        elif choice=='5':
            print("Happy shopping!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

        input("\nPress Enter to return to menu....")
        os.system('cls' if os.name=='nt' else 'clear')

if __name__=='__main__':
    main()