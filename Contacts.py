class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, query):
        results = []
        for contact in self.contacts:
            if query in (contact.name, contact.phone):
                results.append(contact)
        return results

    def update_contact(self, index, updated_contact):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = updated_contact
            print("Contact updated successfully.")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
            print("Contact deleted successfully.")
        else:
            print("Invalid contact index.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            new_contact = Contact(name, phone, email, address)
            contact_manager.add_contact(new_contact)
            print("Contact added successfully.")

        elif choice == "2":
            contact_manager.view_contacts()

        elif choice == "3":
            query = input("Enter name or phone number to search: ")
            results = contact_manager.search_contact(query)
            if results:
                for i, result in enumerate(results, start=1):
                    print(f"{i}. Name: {result.name}, Phone: {result.phone}")
            else:
                print("No matching contacts found.")

        elif choice == "4":
            index = int(input("Enter the index of the contact to update: ")) - 1
            if 0 <= index < len(contact_manager.contacts):
                name = input("Enter New Name: ")
                phone = input("Enter New Phone: ")
                email = input("Enter New Email: ")
                address = input("Enter New Address: ")
                updated_contact = Contact(name, phone, email, address)
                contact_manager.update_contact(index, updated_contact)
            else:
                print("Invalid contact index.")

        elif choice == "5":
            index = int(input("Enter the index of the contact to delete: ")) - 1
            contact_manager.delete_contact(index)

        elif choice == "6":
            print("Thank you for using the Contact Management System!")
            break

if __name__ == "__main__":
    main()
