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

