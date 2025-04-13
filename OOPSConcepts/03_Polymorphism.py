'''
## Plymorphism:
    Poly means many and morphism means forms/states
    Refers to an object taking several forms depending on the methods/area


    
'''

##***************************************************************************************************
class Vehicle:
    def start_engine(self):
        print("Starting the vehicle")

class Car(Vehicle):
    def start_engine(self):
        print("Starting the car engine ... Vroom!")

class Bike(Vehicle):
    def start_engine(self):
        print("Starting the bike engine ... Brrrmm!")

def start_vehicle_engine(vehicle):
    vehicle.start_engine()

# Create objects
car = Car()
bike = Bike()
vehicle = Vehicle()

# Call the function with different types
start_vehicle_engine(car)
start_vehicle_engine(bike)
start_vehicle_engine(vehicle)

##***************************************************************************************************
#METHOD OVERLOADING:student method is taking different forms, the last methods overloading
# Method overloading happens in same class

class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(5, 10))       # Output: 15
print(calc.add(1, 2, 3))     # Output: 6
print(calc.add(7))           # Output: 7

##***************************************************************************************************
## Ways of implementing Polymorphism in Python
## 1. Duck typing:
class Duck:
    def quack(self):
        print("Quack!!...")

class Person:
    def quack(self):
        print("I'm pretending to be a duck!")

def make_it_quack(thing):
    thing.quack()

duck = Duck()
person = Person()

make_it_quack(duck)
make_it_quack(person)


## 2. Method Overriding: Polymorphism through inheritance and method overriding
class Vechicle:
    def move(self):
        return "Moving..."

class Car(Vechicle):
    def move(self):
        return "Driving on the road"

class Airplane(Vechicle):
    def move(self):
        return "Flying in the air"
    
Vechicles =[Car(), Airplane()]
for vechicle in Vechicles:
    print(vechicle.move())

## 3. Operator Overloading: Python also supports polymorphism through operator overloading
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __add__(self, Other):
        return Point(self.x+Other.x, self.y+ Other.y)
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
p1= Point(1,2)
p2= Point(3,4)
print(p1+ p2)


## 4. Built-in Polymorphic Functions
print(len("Python"))   
print(len([1, 2, 3, 4]))  
print(len({"a": 1, "b": 2}))  

print(10 + 5)       
print("Hello " + "World")  
print([1, 2] + [3, 4])  

##***************************************************************************************************

## Types of Polymorphism:
# Complietimes Polymorphism:  Occurs when the method to be executed is determined at compile time.

class AddNumbers:
    def __init__(self, value):
        self.value=value
    
    def __add__(self, other):
        return AddNumbers(self.value+other.value)

obj1= AddNumbers(10)
obj2=AddNumbers(20)
resilt= obj1+ obj2
print(resilt.value)

## Runtime Polymorphism: Occurs when the method to be executed is determined at runtime, typically using method overriding.
class Parent:
    def display(self):
        print("This is the Parent class")

class Child(Parent):
    def display(self):
        print("This is the Child class")

obj = Child()
obj.display() 
