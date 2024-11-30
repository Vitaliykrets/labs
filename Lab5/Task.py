class Fish:
    def __init__(self, name, age, species, size, preferredFood, isAggressive, neededSpace):
        self.name = name
        self.age = age
        self.species = species
        self.size = size
        self.preferredFood = preferredFood
        self.isAggressive = isAggressive
        self.neededSpace = neededSpace

    def __str__(self):
        return f"{self.name} ({self.species}), Size: {self.size}m, Aggressive: {self.isAggressive}"


class Aquarium:
    def __init__(self, totalVolume):
        self.totalVolume = totalVolume
        self.freeSpace = totalVolume
        self.fishes = []

    def add_fish(self, fish):
        if fish.isAggressive:
            if not self.has_aggressive_fish() and len(self.fishes) > 0:
                print(f"Cannot add aggressive fish {fish.name} to the aquarium, as there are no other aggressive fishes.")
                return False
        
        if self.freeSpace >= fish.neededSpace:
            self.fishes.append(fish)
            self.freeSpace -= fish.neededSpace
            print(f"{fish.name} has been added to the aquarium.")
            return True
        else:
            print(f"There is not enough space for {fish.name}.")
            return False

    def has_aggressive_fish(self):
        return any(fish.isAggressive for fish in self.fishes)

    def three_large_fish(self):
        largest_fish = sorted(self.fishes, key = lambda f: f.size, reverse = True)[:3]
        print("Top 3 largest fish in the aquarium:")
        for fish in largest_fish:
            print(fish)

    def __str__(self):
        return f"Aquarium Volume: {self.totalVolume}m³, Free Space: {self.freeSpace:.2f}m³, Fish Count: {len(self.fishes)}"


def main():
    fish1 = Fish("Bubbles", 1, "Neon Tetra", 0.2, "Flakes", False, 0.1)
    fish2 = Fish("Glimmer", 2, "Betta", 0.5, "Pellets", True, 0.3)
    fish3 = Fish("Spark", 1, "Guppy", 0.3, "Insects", False, 0.1)
    fish4 = Fish("Finny", 3, "Clownfish", 0.1, "Plankton", False, 0.2)
    fish5 = Fish("Swimmy", 4, "Zebra Danio", 0.4, "Flakes", True, 0.15)
    fish6 = Fish("Splash", 2, "Goldfish", 0.4, "Flakes", False, 0.2)
    fish7 = Fish("Luna", 1, "Angelfish", 0.3, "Worms", False, 0.15)
    fish8 = Fish("Zara", 3, "Oscar", 1.2, "Meat", True, 0.6)
    fish9 = Fish("Finn", 2, "Guppy", 0.05, "Insects", False, 0.05)
    fish10 = Fish("Toby", 4, "Betta", 0.3, "Pellets", True, 0.25)

    aquarium1 = Aquarium(2)
    aquarium2 = Aquarium(3)

    aquarium1.add_fish(fish1)
    aquarium1.add_fish(fish2)  
    aquarium1.add_fish(fish3)
    aquarium1.add_fish(fish6)
    aquarium1.add_fish(fish7)
    
    aquarium2.add_fish(fish10)
    aquarium2.add_fish(fish8)
    aquarium2.add_fish(fish5)
    aquarium2.add_fish(fish9)
    aquarium2.add_fish(fish4)

    aquarium1.three_large_fish()
    aquarium2.three_large_fish()

    print(aquarium1)
    print(aquarium2)

if __name__ == "__main__":
    main()
