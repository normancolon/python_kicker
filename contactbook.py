def add_contact(contact_book):
    name = input("Enter contact's name: ")
    if name not in contact_book:
        phone_number = input("Enter contact's phone number: ")
        contact_book[name] = phone_number
        print("Contact added.")
    else:
        print("Contact already exists.")

def delete_contact(contact_book):
    name = input("Enter contact's name to delete: ")
    if name in contact_book:
        del contact_book[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

def update_contact(contact_book):
    name = input("Enter contact's name to update: ")
    if name in contact_book:
        phone_number = input("Enter the new phone number: ")
        contact_book[name] = phone_number
        print("Contact updated.")
    else:
        print("Contact not found.")

def display_contacts(contact_book):
    for name, phone_number in contact_book.items():
        print(f"Name: {name}, Phone Number: {phone_number}")

def main():
    contact_book = {}

    while True:
        print("\nOptions: Add, Delete, Update, Display, Exit")
        choice = input("Choose an action: ").lower()

        if choice == 'add':
            add_contact(contact_book)
        elif choice == 'delete':
            delete_contact(contact_book)
        elif choice == 'update':
            update_contact(contact_book)
        elif choice == 'display':
            display_contacts(contact_book)
        elif choice == 'exit':
            print("Exiting the contact book application.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

