
## Function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  
##O/p: Hello, Alice!



## Method
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

person1 = Person("Bob")
print(person1.greet())
##O/p: Hello, Bob!

##***************************************************************************************************
##  Defining and Calling a Function

## Method 1: Basic
def greet():
    print("Hello World!")

#Calling a Function:
greet()
## O/p: Hello World!

## Method 2: Function with Parameter
#Defining a Function with Parameters:
def greet(name):
    print(f"Hello {name}")

#Calling a Function with Arguments:
greet("jhon doe")
##O/p: Hello jhon doe

## Method 3: Function with return
def operation(x,y):
    return x+y

print("The value of add operation is:", operation(2,9))
##O/p: The value of add operation is: 11





from functools import reduce

numbers = [47, 11, 42, 13]
result = reduce(lambda x, y: x + y, numbers)
print(result)  # Output: 113

