class Fish:
    def __init__(self, name, age, species, size, preferredFood, isAggressive, neededSpace, strengthCoefficient):
        self.name = name
        self.age = age
        self.species = species
        self.size = size
        self.preferredFood = preferredFood
        self.isAggressive = isAggressive
        self.neededSpace = neededSpace
        self.strengthCoefficient = strengthCoefficient

    def __str__(self):
        return f"{self.name} ({self.species}), Size: {self.size}m, Aggressive: {self.isAggressive}, Strength: {self.strengthCoefficient}"


class Aquarium:
    def __init__(self, totalVolume):
        self.totalVolume = totalVolume
        self.freeSpace = totalVolume
        self.fishes = []

    def add_fish(self, fish):
        if self.freeSpace >= fish.neededSpace:
            self.fishes.append(fish)
            self.freeSpace -= fish.neededSpace
            print(f"{fish.name} has been added to the aquarium.")
            return True
        else:
            print(f"There is not enough space for {fish.name}.")
            return False

    def update_fish_states(self):
        aggressive_sum = 0
        non_aggressive_sum = 0

        for fish in self.fishes:
            if fish.isAggressive:
                aggressive_sum += fish.strengthCoefficient
            else:
                non_aggressive_sum += fish.strengthCoefficient

        if aggressive_sum > non_aggressive_sum:
            for fish in self.fishes:
                if not fish.isAggressive:
                    fish.isAggressive = True
            print("Non-aggressive fish become aggressive!")
            
        elif non_aggressive_sum > aggressive_sum:
            for fish in self.fishes:
                if fish.isAggressive:
                    fish.isAggressive = False
            print("Aggressive fish become non-aggressive!")

    def __str__(self):
        return f"Aquarium Volume: {self.totalVolume}m³, Free Space: {self.freeSpace:.2f}m³, Fish Count: {len(self.fishes)}"


def main():
    fish1 = Fish("Bubbles", 1, "Neon Tetra", 0.2, "Flakes", False, 0.1, 0.1)
    fish2 = Fish("Glimmer", 2, "Betta", 0.5, "Pellets", True, 0.3, 0.3)
    fish3 = Fish("Spark", 1, "Guppy", 0.3, "Insects", False, 0.1, 0.2)
    fish4 = Fish("Finny", 3, "Clownfish", 0.1, "Plankton", False, 0.2, 0.4)
    fish5 = Fish("Swimmy", 4, "Zebra Danio", 0.4, "Flakes", True, 0.15, 0.2)
    fish6 = Fish("Splash", 2, "Goldfish", 0.4, "Flakes", False, 0.2, 0.1)

    aquarium = Aquarium(3)
    aquarium.add_fish(fish1)
    aquarium.add_fish(fish2)
    aquarium.add_fish(fish3)
    aquarium.add_fish(fish4)
    aquarium.add_fish(fish5)
    aquarium.add_fish(fish6)

    print("\nBefore updating fish states:")
    for fish in aquarium.fishes:
        print(fish)

    aquarium.update_fish_states()

    print("\nAfter updating fish states:")
    for fish in aquarium.fishes:
        print(fish)


if __name__ == "__main__":
    main()
