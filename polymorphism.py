class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"i am cat my name is {self.name} , and i am {self.age} years old")
    def make_sound(self):
        print("the sound of cat is meow")
cat1=cat("tom",2)
cat1.info()
cat1.make_sound()

class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"i am dog my name is {self.name} , and i am {self.age} years old")
    def make_sound(self):
        print("the sound of dog is bark")
dog1=dog("jerry",3)
dog1.info()
dog1.make_sound()

class bird:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"i am bird my name is {self.name} , and i am {self.age} years old")
    def make_sound(self):
        print("the sound of bird is chirp")
bird1=bird("parrot",1)


for animal in (cat1,dog1,bird1):
    animal.info()
    animal.make_sound()