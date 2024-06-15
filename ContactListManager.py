# main.py

import contact_manager

def main():
    contacts = []
    while True:
        print("\n1. Add contact\n2. View contacts\n3. Search Contact\n4. Remove contact\n5. Exit")
        choice = input("Enter selection: ")
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contact_manager.add_contact(contacts, name, phone, email)
        elif choice == '2':
            contact_manager.view_contacts(contacts)
        elif choice == '3':
            name = input("Enter the name to search: ")
            contact = contact_manager.search_contact(contacts, name)
            if contact:
                print(f"Contact found: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            else:
                print("Contact not found")
        elif choice == '4':
            name = input("Enter name to remove: ")
            if contact_manager.remove_contact(contacts, name) is not None:
                print("Contact deleted")
            else:
                print("Contact not found")
        elif choice == '5':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
