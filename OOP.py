# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin
    
    def introduce(self):
        print(f"I am {self.name} from {self.origin}, and my power is {self.power}!")
    
    def use_power(self):
        print(f"{self.name} uses {self.power} 💥")

# Subclass 1: AlienHero inherits from Superhero
class AlienHero(Superhero):
    def __init__(self, name, power, origin, planet):
        super().__init__(name, power, origin)
        self.planet = planet
    
    def introduce(self):
        print(f"I am {self.name}, an alien from {self.planet}. I use {self.power}!")

# Subclass 2: TechHero inherits from Superhero
class TechHero(Superhero):
    def __init__(self, name, power, origin, gadget):
        super().__init__(name, power, origin)
        self.gadget = gadget
    
    def use_power(self):
        print(f"{self.name} activates {self.gadget} to unleash {self.power} 🛠️")

# Example usage:
hero1 = Superhero("Valor", "Super Strength", "Metro City")
hero2 = AlienHero("Zorax", "Telepathy", "Nebula Base", "Zentauron")
hero3 = TechHero("Circuit", "EMP Blast", "Neo Tokyo", "Power Suit")

hero1.introduce()
hero2.introduce()
hero3.introduce()

hero1.use_power()
hero2.use_power()
hero3.use_power()

class Vehicle:
    def move(self):
        print("The vehicle moves.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")

# Example usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
