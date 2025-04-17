
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 10  # Start very hungry
        self.energy = 0   # Start tired
        self.happiness = 0  # Start not happy
        self.tricks = []  # List to store learned tricks

    def eat(self):
        # Reduce hunger by 3 (minimum 0) and increase happiness by 1
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} is eating...")

    def sleep(self):
        # Increase energy by 5 (maximum 10)
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping...")

    def play(self):
        # Decrease energy by 2, increase happiness by 2, increase hunger by 1
        if self.energy >= 2:  # Only play if there's enough energy
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} is playing...")
        else:
            print(f"{self.name} is too tired to play!")

    def get_status(self):
        print(f"🐾 {self.name}'s Status:")
        print(f"  Hunger: {self.hunger}/10")
        print(f"  Energy: {self.energy}/10")
        print(f"  Happiness: {self.happiness}/10")

    def train(self, trick):
        # Add a new trick to the list
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        # Display all learned tricks
        print(f"{self.name}'s Tricks:")
        if self.tricks:
            for trick in self.tricks:
                print(f"  - {trick}")
        else:
            print("  No tricks learned yet.")
