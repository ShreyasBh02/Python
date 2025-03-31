'''
Lambda or Anonymous Function:
    •	A lambda function in Python is a concise way to create anonymous functions, also known as lambda expressions.
    •	They don't have a name.
    •   SYNTAX: lambda arguments: expression      
'''

greet= lambda x: "Hello " + x
print(greet("World"))

add =lambda x,y,z:(x+y+z)
print(add(5,6,74))
##***************************************************************************************************

##EX:
##Define lambda functions
add =lambda x, y: x+y
subtract=lambda x, y: x-y
multiply=lambda x, y: x*y
divide= lambda x, y: x/y

## Functions with def
def calculate_Operations(x,y, operation):
    if operation == 'add':
        return add(x, y)
    elif operation == 'subtract':
        return subtract(x, y)
    elif operation == 'multiply':
        return multiply(x, y)
    elif operation == 'divide':
        return divide(x, y)
    else:
        return "Invalid operation"

## Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

## Perform the calculation
result = calculate_Operations(num1, num2, operation)

## Print the result
print(f"The result of {operation}ing {num1} and {num2} is: {result}")

##***************************************************************************************************

##Fibonachi series
fib=lambda n: n if n<=1 else fib(n-1) +fib (n-2)
print([fib(i) for i in range(5)])


user_Data=[
    {"Name": "Jhon Doe", "Age":26, "UId":679},
    {"Name": "Bob", "Age":40, "UId":605},
    {"Name": "Alice Border", "Age":14, "UId":658}
]

sorted_User= sorted(user_Data, key= lambda person: person["UId"])
print(sorted_User)


## Factorial
## Using a Regular Function
def fact_num(num):
    if num==0:
        return 1
    else:
        return num*fact_num(num-1)
    
print(fact_num(5))


## Using a Lambda Function
fact=lambda num: 1 if num==0 else num *fact(num-1)
print(fact(5))


##***************************************************************************************************
## MAP(): map() function is a built-in function used to apply a given function to all items in an iterable (such as a list, tuple, or set) and return a map object (which is an iterator).

## map()
def square(x):
    return x*x
number=(1,2,3,4)
sqnumber=map(square,number)
print("funtion with map()")
print(list(sqnumber))


## Lambda Function with MAP()
## EX:1
num=[5,9,7,6,3]
doubled_Num=list(map(lambda x:x*2, num))
print("Lambda Function with MAP()")
print(doubled_Num)


##***************************************************************************************************
## Reduce():It reduces the iterable to a single value.
#Reduce will always take two argument functions
from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
result = reduce(add, numbers)
print(result)

## Lambda Function with Reducee()
numbers = [1, 2, 3, 4, 5]
print(reduce(lambda x,y:x+y, numbers))

## WAP to give largest no
numList=[7,0,8,100,156,9,600]
largestNum=reduce(lambda x,y: x if x>y else y, numList )
print(largestNum)

## Lambda Function with Reducee() using an Initializer 
num=[9,6,4,5,4]
results= reduce(lambda x,y: x*y, num, 10)
print(results)


##***************************************************************************************************
## filter():

number=[6,9,4,6,5]
evenNum=filter(lambda x:x%2==0, number )
print(list(evenNum))

names = ["Alice", "Bob", "Charlie", "Dave"]
filtered_names = filter(lambda name: len(name) > 3, names)
print(list(filtered_names)) 


from functools import reduce
numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x + y, numbers)

print(result)