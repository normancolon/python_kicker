class GroceryList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added '{item}' to the list.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Removed '{item}' from the list.")
        else:
            print(f"'{item}' not found in the list.")

    def show_list(self):
        if self.items:
            print("\nGrocery List:")
            for item in self.items:
                print(f"- {item}")
        else:
            print("The grocery list is empty.")

def main():
    grocery_list = GroceryList()
    while True:
        print("\nOptions:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Show list")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            grocery_list.add_item(item)
        elif choice == '2':
            item = input("Enter the item to remove: ")
            grocery_list.remove_item(item)
        elif choice == '3':
            grocery_list.show_list()
        elif choice == '4':
            print("Exiting the grocery list program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()