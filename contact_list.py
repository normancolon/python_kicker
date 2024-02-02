#!/bin/python3
contact_book = {}

# Function to add a new contact
def add_new_contact():
    name = input("Enter the contact's name: ")
    if name in contact_book:
        print("This contact already exists.")
    else:
        phone_number = input("Enter the contact's phone number: ")
        contact_book[name] = phone_number
        print("Contact added successfully.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the contact's name to delete: ")
    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully.")
    else:
        print("This contact does not exist.")

# Function to update a contact's phone number
def update_contact():
    name = input("Enter the contact's name to update: ")
    if name in contact_book:
        phone_number = input("Enter the new phone number: ")
        contact_book[name] = phone_number
        print("Contact updated successfully.")
    else:
        print("This contact does not exist.")

# Function to display all contacts
def display_all_contacts():
    if contact_book:
        for name, phone_number in contact_book.items():
            print(f"Name: {name}, Phone Number: {phone_number}")
    else:
        print("The contact book is empty.")

# Main function to run the contact book application
def run_contact_book_application():
    while True:
        print("\nContact Book Application")
        print("1: Add a new contact")
        print("2: Delete a contact")
        print("3: Update a contact's phone number")
        print("4: Display all contacts")
        print("5: Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_new_contact()
        elif choice == "2":
            delete_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            display_all_contacts()
        elif choice == "5":
            print("Exiting the contact book application.")
            break
        else:
            print("Invalid choice. Please try again.")

# run_contact_book_application()

