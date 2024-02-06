#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for idx, contact in enumerate(self.contacts):
            print(f"{idx + 1}. {contact.name}: {contact.phone_number}")

    def search_contact(self, keyword):
        results = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                results.append(contact)
        return results

    def update_contact(self, index, new_contact):
        self.contacts[index] = new_contact

    def delete_contact(self, index):
        del self.contacts[index]

def main():
    address_book = AddressBook()

    while True:
        print("\n*** Address Book Menu ***")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            if address_book.contacts:
                print("\n*** Contact List ***")
                address_book.view_contacts()
            else:
                print("No contacts found.")

        elif choice == "2":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            address_book.add_contact(new_contact)
            print("Contact added successfully.")

        elif choice == "3":
            keyword = input("Enter name or phone number to search: ")
            search_results = address_book.search_contact(keyword)
            if search_results:
                print("\n*** Search Results ***")
                for contact in search_results:
                    print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")
            else:
                print("No matching contacts found.")

        elif choice == "4":
            index = int(input("Enter the index of contact to update: ")) - 1
            if 0 <= index < len(address_book.contacts):
                name = input("Enter new name: ")
                phone_number = input("Enter new phone number: ")
                email = input("Enter new email: ")
                address = input("Enter new address: ")
                new_contact = Contact(name, phone_number, email, address)
                address_book.update_contact(index, new_contact)
                print("Contact updated successfully.")
            else:
                print("Invalid index.")

        elif choice == "5":
            index = int(input("Enter the index of contact to delete: ")) - 1
            if 0 <= index < len(address_book.contacts):
                address_book.delete_contact(index)
                print("Contact deleted successfully.")
            else:
                print("Invalid index.")

        elif choice == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# In[ ]:




