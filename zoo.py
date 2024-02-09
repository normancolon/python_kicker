#!/usr/bin/python3
class Animal:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def sleep(self):
        return f"{self.name} is sleeping."

    def eat(self):
        return f"{self.name} is eating."


class Lion(Animal):
    def roar(self):
        return f"{self.name} is roaring."


class Elephant(Animal):
    def play(self):
        return f"{self.name} is playing."


# Dictionary to store animals
zoo = {}

# Dictionary to store animal sounds
animal_sounds = {
    'Lion': 'roar',
    'Elephant': 'trumpet',
}


# Function to add animals
def add_animal():
    animal_type = input("Enter animal type (Lion/Elephant): ").capitalize()
    name = input("Enter the animal's name: ")
    age = int(input("Enter the animal's age: "))
    
    if animal_type == 'Lion':
        animal = Lion(age, name)
    elif animal_type == 'Elephant':
        animal = Elephant(age, name)
    else:
        print("Unknown animal type.")
        return
    
    zoo[name] = animal
    print(f"{name} the {animal_type} has been added to the zoo.")


# Function to remove animals
def remove_animal():
    name = input("Enter the name of the animal to remove: ")
    
    if name in zoo:
        del zoo[name]
        print(f"{name} has been removed from the zoo.")
    else:
        print(f"{name} is not found in the zoo.")


# Function to display animals
def display_animals():
    if zoo:
        for name, animal in zoo.items():
            print(f"{name} the {type(animal).__name__}, Age: {animal.age}")
    else:
        print("The zoo is currently empty.")


# Interactive loop
def main():
    while True:
        print("\nWelcome to the Zoo Simulator!")
        print("1. Add an animal")
        print("2. Remove an animal")
        print("3. Display all animals")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_animal()
        elif choice == '2':
            remove_animal()
        elif choice == '3':
            display_animals()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
