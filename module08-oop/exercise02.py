# abstract class, interface
class Animal:  # abstract class
    def __init__(self, legs):
        self.legs = legs

    def walk(self):
        print(f"Animal with {self.legs} legs is walking now...")

    def eat(self):  # abstract method
        pass


class Pet:  # interface
    def setName(self, name):  # abstract method
        pass

    def getName(self):  # abstract method
        pass

    def play(self):  # abstract method
        pass


class Spider(Animal):

    def __init__(self):
        super().__init__(8)

    def eat(self):
        print(f"Spider is eating now...")


class Cat(Animal, Pet):  # Multiple Inheritance
    def __init__(self):
        super().__init__(4)
        self.name = "Tekir"

    def eat(self):
        print(f"{self.name} is eating now...")

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def play(self):
        print(f"{self.name} is playing now...")


class Fish(Animal, Pet):
    def __init__(self):
        super().__init__(0)
        self.name = "Free Willy"

    def walk(self):
        print(f"{self.name} is swimming now...")

    def eat(self):
        print(f"{self.name} is eating now...")

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def play(self):
        print(f"{self.name} is playing now...")


garfield = Cat()
garfield.setName("garfield")

jaws = Fish()
jaws.setName("jaws")

animals = [Cat(), Spider(), jaws, Spider(), garfield, Fish()]

for animal in animals:
    animal.walk()
    animal.eat()
    if isinstance(animal, Pet):
        animal.play()

total_legs = sum(map(lambda animal: animal.legs, animals))

print(total_legs)

# cluster animals into 2 classes: pet vs wild and count them!
countAnimals = {
    "pet": 0,
    "wild": 0
}

from functools import reduce


def reducer(count, petOrWild):
    count[petOrWild] += 1
    return count


mapAnimal2WildOrPet = lambda animal: "pet" if isinstance(animal, Pet) else "wild"

result = reduce(reducer, map(mapAnimal2WildOrPet, animals), countAnimals)

print(result)

