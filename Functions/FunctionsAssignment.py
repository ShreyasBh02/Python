
## Q1. WAP function that takes a list of numbers as input and returns the sum of all even numbers in the list.

def evenNumAdd(numbers):
    even_Sum = 0  
    for num in numbers: 
        if num % 2 == 0: 
            even_Sum += num 
    return even_Sum  

numbers = [6, 9, 1, 4, 3, 13, 10]
result = evenNumAdd(numbers)
print(result)

## Q2. Create a Python function that accepts a string and returns the reverse of that string.

def reverse_string(input_string):
    return input_string[::-1]
string = "Python function"
result = reverse_string(string)
print(result) 


## Q3.  Implement a Python function that takes a list of integers and returns a new list containing the squares of each number.
def squareNum(numbers):
    return [num **2 for num in numbers]

num=[6, 9, 1, 4, 3, 10]
result =squareNum(num)
print(result )

## Q4. Write a Python function that checks if a given number is prime or not from 1 to 200.
def is_Prime(number):
    if number < 1 or number >200:
        return  f"{number} is outside the range of 1 to 200."
    
    if number<2:
        return False
    for i in range(2, int (number**0.5)+1):
        if number%i==0:
            return False
    return True

## Non Prime no
number = 39
result = is_Prime(number)
print(f"{number} is: ", result)

## prime no
number = 19
result = is_Prime(number)
print(f"{number} is: ", result)

## no not between 1 -200
number = 250
result = is_Prime(number)
print(result)  

## Q5. Create an iterator class in Python that generates the Fibonacci sequence up to a specified number of terms. 

fib =lambda num: num if num <=1 else fib(num-1) + fib(num-2)
print([fib(i) for i in range (10)])

## Q6. Write a generator function in Python that yields the powers of 2 up to a given exponent.
def powers(exponent):
    for i in range(exponent + 1):
        yield 2 ** i

exponent = 5
for power in powers(exponent):
    print(power)

## Q7. Implement a generator function that reads a file line by line and yields each line as a string.
def read_the_line(string):
    for line in string.splitlines():
        yield line

input_string="""Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.
Twinkle, twinkle, little star,
How I wonder what you are."""


for line in read_the_line(input_string):
    print(line)

## Q8.  Use a lambda function in Python to sort a list of tuples based on the second element of each tuple.
fruit_list= [('apple', 5), ('banana', 2), ('cherry', 8), ('pineapple', 1), ('strawberry', 4)]

sorted_fruit=sorted(fruit_list, key= lambda x:x[1])
print(sorted_fruit)

## Q9. Write a Python program that uses `map()` to convert a list of temperatures from Celsius to Fahrenheit.'
celsius_temperatures = [0, 20, 25, 30, 35, 40]

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) +32

fahrenheit_temperatures = list(map (celsius_to_fahrenheit, celsius_temperatures))

print(fahrenheit_temperatures)


## Q10. Create a Python program that uses `filter()` to remove all the vowels from a given string.

input_string = "Hello, how are you?"
filtered_string = ''.join(filter(lambda char : char.lower() not in 'aeiou', input_string))
print(filtered_string)


## Q11. 

def process_ordre(orders):
    '''
    Process book shop orders and return a list of 2-tuples.
    Each tuple contains the order number and the product of price and quantity.
    If the order value is less than 100.00 €, the product is increased by 10.00 €.
      
    orders: List of orders, where each order is a list/tuple containing
            [order_number, book_title, quantity, price_per_item]
    
    '''
    result = list(map(
        lambda order: (
            order[0],  
            order[3] * order[2] + (10 if order[3] * order[2] < 100 else 0)  # Product with adjustment
        ),
        orders
    ))
    return result

if __name__  == "__main__":
    orders = [
         [34587, "Learning Python, Mark Lutz", 4, 40.95],
        [98762, "Programming Python, Mark Lutz", 5, 56.80],
        [77226, "Head First Python, Paul Barry", 3, 32.95],
        [88112, "Einführung in Python3, Bernd Klein", 3, 24.99]
    ]
    result = process_ordre(orders)

print("Order Number | Order Value")
print("------------------------")
for order_num, value in result:
    print(f"{order_num:<12} | {value:.2f} €")
