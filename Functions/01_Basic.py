'''
Funtions:
Syntax: 
    def function_name( parameters ):
    "function_docstring"
    function_suite
    return [expression]
'''

## Creating the function
def greeting():
    print("Hellow World!")

greeting()

##***************************************************************************************************
##Calling function without Parameter

def userData():
    userInfo = {"name": "John Doe", "age": 25}
    return userInfo
print(userData())
##O/p:{'name': 'John Doe', 'age': 25}

##Calling function with Parameter
def sumfunction(arg1, arg2):
    print("Inside function:")
    result = arg1 + arg2  
    print("Sum is:", result) 
    return result  

arg1, arg2 = 10, 20
var = sumfunction(arg1, arg2)  
print("Value after function call:", var)
'''O/p:
Inside function:
Sum is: 30
Value after function call: 30
'''

##***************************************************************************************************
## Pass by value: means you pass a copy of the data, so the original value is not modified.
def modify(x):
    print(f"ID of x inside function: {id(x)}")  
    x = x + 10
    print(f"ID of x after modification: {id(x)}")  

a = 5
print(f"ID of a before function call: {id(a)}")
modify(a)
print(f"ID of a after function call: {id(a)}")

## Pass by Reference means you pass the reference (memory address), so the original value can be modified.
def modify(lst):
    print(f"ID of lst inside function: {id(lst)}")  
    lst.append(10)
    print(f"ID of lst after modification: {id(lst)}")  
    print(f"modified lst:",lst)

numbers = [1, 2, 3]
print(f"ID of numbers before function call: {id(numbers)}")
modify(numbers)
print(f"ID of numbers after function call: {id(numbers)}")


##***************************************************************************************************
## Iterators 
# Creating an iterator manually
my_list = [1, 2, 3]
iterator = iter(my_list)  
print(next(iterator))  # O/p: 1
print(next(iterator))  # O/p: 2
print(next(iterator))  # O/p: 3
print(next(iterator))  # Raises StopIteration (no more elements)

## Iterable
# Creating an iterable
my_list = [1, 2, 3]

# Using a for loop to iterate over the iterable
for item in my_list:
    print(item)

''' # O/p:
1
2
3
'''

##***************************************************************************************************
## Generator

def count_up_to(max):
    count = 1
    while count <= max:
        yield count  # Pause and return the current value of count
        count += 1

# Using the generator
counter = count_up_to(5)
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2
print(next(counter))  # Output: 3
print(next(counter))  # Output: 4
print(next(counter))  # Output: 5
print(next(counter))  # Raises StopIteration (No more values)







