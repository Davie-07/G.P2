# OOP Challenge: Pet Simulator
from pet import Pet

# Get pet name from user
pet_name = input("What would you like to name your pet? ")
my_pet = Pet(pet_name)

while True:
    print("\nWhat would you like to do with your pet?")
    print("1. Check status")
    print("2. Feed pet")
    print("3. Let pet sleep")
    print("4. Play with pet")
    print("5. Teach a new trick")
    print("6. Show learned tricks")
    print("7. Quit")
    
    choice = input("Enter your choice (1-7): ")
    
    if choice == "1":
        my_pet.get_status()
    elif choice == "2":
        my_pet.eat()
    elif choice == "3":
        my_pet.sleep()
    elif choice == "4":
        my_pet.play()
    elif choice == "5":
        trick = input("What trick would you like to teach your pet? ")
        my_pet.train(trick)
    elif choice == "6":
        my_pet.show_tricks()
    elif choice == "7":
        print(f"Goodbye! Take care of {my_pet.name}!")
        break
    else:
        print("Invalid choice. Please try again.")
