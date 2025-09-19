''' if local variable
. dictionary created inside main().
. Every function call include contacts as argument.
. Functions that modify the dictionary don't return it
because dictionaries are mutable (the changes affect the original object)'''

contacts={}

def menu():
    print("\n----Contact Book Menu----")
    print("1. Add new contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Quit")
    print("-------------------------")

def add():
    name=input("Enter contact's name : ").strip()

    if name in contacts:
        print(f"ERROR: Contact '{name}' already exists.")
        return

    phone=input("Enter contact's phone number : ")
    email=input("Enter contact's email address : ")

    contacts[name]={"phone":phone, "email":email}
    print(f"Success: Contact '{name}' added. ☑️")

def view():
    if not contacts:
        print("Your contact book is empty. Add some first!!")
        return

    print("\n----All Contacts----")
    for name,details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
    print("--------------------")

def search():
    name=input("Enter name to search for : ").strip()

    if name in contacts:
        details=contacts[name]
        print("\n----Contact Found----")
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
        print("---------------------")
    else:
        print(f"ERROR: Contact '{name}' not found. ❌")

def update():
    name = input("Enter name to update : ").strip()
    if name in contacts:
        print(f"Updating contact '{name}'Leave a field blank to keep current information.")

        new_phone=input(f"Enter new phone(current: {contacts[name]['phone']}): ").strip()
        new_email = input(f"Enter new email(current: {contacts[name]['email']}): ").strip()

        if new_phone:
            contacts[name]['phone']=new_phone
        if new_email:
            contacts[name]['email']=new_email

        print(f"Success: Contact '{name}' updated successfully!")
    else:
        print(f"ERROR: Contact '{name}' not found.")

def delete():
    name = input("Enter name to delete : ").strip()

    if name in contacts:
        del contacts[name]
        print(f"Success: Contact '{name}' deleted.")
    else:
        print(f"ERROR: Contact '{name}' not found.")

def main():

    while True:
        menu()
        choice = input("Enter your choice(1-6) : ")

        if choice == '1':
            add()
        elif choice == '2':
            view()
        elif choice == '3':
            search()
        elif choice == '4':
            update()
        elif choice == '5':
            delete()
        elif choice == '6':
            print("Thank you for using contact book.")
            break
        else:
            print("Invalid choice. Please enter number between 1 and 6.")

if __name__=="__main__":
    main()