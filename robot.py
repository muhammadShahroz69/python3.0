class Robot:
    species = "machine"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hello, my name is", self.name)

    def details(self):
        print("I am", self.age, "years old")


# creating robot objects
r1 = Robot("Robo", 5)
r2 = Robot("Techy", 3)

# accessing class variable
print("Robo is a", r1.species)
print("Techy is also a", r2.species)

# calling methods
r1.introduce()
r1.details()

r2.introduce()
r2.details()