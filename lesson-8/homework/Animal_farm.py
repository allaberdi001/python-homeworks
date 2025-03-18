class Animal:
    def __init__(self,name):
        self.name=name
    def sleep(self):
        print(f"{type(self).__name__} {self.name} is sleeping")
    def walk(self):
        print(f"{type(self).__name__} {self.name} is walking")
    def eat(self):
        print(f"{type(self).__name__} {self.name} is eating")
    def __str__(self):
        return (f"{self.name} is {type(self).__name__}")
class Cow(Animal):
    def give_milk(self):
        print(f"{type(self).__name__} {self.name} is giving milk")
    def Moo(self):
        print(f"{type(self).__name__} {self.name} is mooing")
class Cat(Animal):
    def drink_milk(self):
        print(f"{type(self).__name__} {self.name} is drinking milk")
    def catch_mouse(self):
        print(f"{type(self).__name__} {self.name} is catching mouse")
class Dog(Animal):
    def bark(self):
        print(f"{type(self).__name__} {self.name} is barking")
    def protect(self):
        print(f"{type(self).__name__} {self.name} is protecting the house")

my_dog=Dog("Ricar")
print(my_dog)

my_cow=Cow("Margaretta")
print(my_cow)
