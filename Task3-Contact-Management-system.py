import json
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"Contact for {name} added successfully.")

def view_contacts(contacts):
    if contacts:
        for i, contact in enumerate(contacts):
            print(f"{i + 1}. {contact['name']} - {contact['phone']} - {contact['email']}")
    else:
        print("No contacts found.")

def edit_contact(contacts):
    view_contacts(contacts)
    index = int(input("Enter the number of the contact to edit: ")) - 1
    if 0 <= index < len(contacts):
        name = input(f"Enter new name ({contacts[index]['name']}): ") or contacts[index]['name']
        phone = input(f"Enter new phone number ({contacts[index]['phone']}): ") or contacts[index]['phone']
        email = input(f"Enter new email address ({contacts[index]['email']}): ") or contacts[index]['email']
        contacts[index] = {"name": name, "phone": phone, "email": email}
        save_contacts(contacts)
        print(f"Contact for {name} updated successfully.")
    else:
        print("Invalid contact number.")

def delete_contact(contacts):
    view_contacts(contacts)
    index = int(input("Enter the number of the contact to delete: ")) - 1
    if 0 <= index < len(contacts):
        removed_contact = contacts.pop(index)
        save_contacts(contacts)
        print(f"Contact for {removed_contact['name']} deleted successfully.")
    else:
        print("Invalid contact number.")

def main():
    contacts = load_contacts()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__=="__main__":
    main()