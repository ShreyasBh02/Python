''' OOPS:
Object-oriented programming paradigm is characterized by the following principles −
    Class
    Object
    Encapsulation
    Inheritance
    Polymorphism
'''

##Self: Mandatory in class definitions: While calling a method, 
# Python automatically passes the instance as the first argument, so it's necessary to include  in method definitions.

class Car:
    def __init__(self, model):
        self.model = model  # Using self to assign the attribute to the instance

    def show_model(self):
        print(f"The car model is {self.model}")

my_car = Car("Tesla Model 3")
my_car.show_model()  


##***************************************************************************************************

## Class: A class is a blueprint for creating objects, defining properties and behaviors.
# Class definition
class car:
    def car_property(self, model):
        self.model= model
        return self.model
    
# Creating an object of the class
ob = car()
print(ob.car_property("Bugatti Chiron"))

##***************************************************************************************************
## Object: An object is an instance of a class.
ob = car()

##***************************************************************************************************
##Encapsulation: Encapsulation is the concept of hiding internal details of an object and exposing only necessary information.
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def display_info(self):
        print(f"{self.make} {self.model}")

my_car = Car("Toyota", "Corolla")
my_car.display_info()  

##***************************************************************************************************
## Inheritance: Inheritance allows a class to inherit attributes and methods from another class.
class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size
    
    def display_battery(self):
        print(f"Battery size: {self.battery_size} kWh")

my_electric_car = ElectricCar("Tesla", "Model S", 100)
my_electric_car.display_battery()

##***************************************************************************************************
## Polymorphism: Polymorphism allows a method to have different behaviors based on the object calling it.
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

animal = Dog()
animal.speak()  # Polymorphism in action

##***************************************************************************************************
## Abstraction: Abstraction hides complex implementation details and shows only the essential features of an object.
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

dog = Dog()
dog.speak()








