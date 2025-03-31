## ARGUMENTS

##Parameters
def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")

##Arguments
greet("Alice")  # "Alice" is an argument

## Putting it Together
def add_numbers(a, b):  # 'a' and 'b' are parameters
    return a + b

result = add_numbers(5, 7)  # 5 and 7 are arguments
print("The sum is:", result)


##***************************************************************************************************
## 1)	Positional or Required Arguments
def func(n1, n2):
    print(n1+ n2)

print("# Correct Usage:")
print( "Passing out of order arguments" )    
func( 30, 20 ) 

print("# Inorrect Usage:")
print( "Passing only one argument" )    
func(10) 


## 2)	Keyword Arguments
def func(str, num):
    print(f"String: {str}")
    print(f"Number: {num}")

print("# Correct Usage:")
func(str="Hello, world!", num=42)
func(num=9.4 ,str="Hello Python")

print("# Incorrect Usage:")
func(str="Jhon")


## 3) Default Arguments
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return;

print("# Correct Usage:")
printinfo( age=50, name="Jhon" )
printinfo( name="Alice" )


## 4) Position- Only arguments
def greet(name, age, /, location="Unknown"):
    print(f"Name: {name}, Age: {age}, Location: {location}")

print("# Correct Usage:")
greet("Alice", 25, location="New York")  

print("# Incorrect Usage:")
greet(name="Alice", age=25)  
## greet(location="New York","Elon", 25 ) 

## 5) Keyword- Only arguments
def calculate(price, *, discount=0, tax=0):
    final_price = price - discount + tax
    print(f"Price: {price}, Discount: {discount}, Tax: {tax}")
    print(f"Final Price: {final_price}")

print("# Correct Usage:")
calculate(100, discount=10, tax=5) 
calculate(100, tax=5, discount=10) 
print()
print("# Incorrect Usage:")
calculate(100, 10, 5) 

##calculate(tax=5,100,  discount=10) 


## 6) 	Arbitrary or Variable-length Arguments
## A. With *args
def student_Grade(student_Name, *grades):
    if len(grades)==0:
        print(f"No grades are available for {student_Name}.")
        return
    totalmarks=sum(grades)
    print (f"Toal marks to: {student_Name}:", totalmarks)

    average=totalmarks/len(grades)
    print (f"Average Grade: {student_Name}: {average:.2f}")

    if average >= 90:
        print("Performance: Excellent")
    elif average >= 75:
        print("Performance: Good")
    elif average >= 50:
        print("Performance: Average")
    else:
        print("Performance: Needs Improvement")

student_Grade("Alice", 50,94,43,6,64)    
student_Grade("Bob")    

## B. With **kwargs
def employee_info(employee_name, role, **details):
    print(f"Employee Name: {employee_name}")
    print(f"Role: {role}")

    if details:
        print("\nAdditional Details:")
        for key, value in details.items():
            print(f"{key}: {value}")

employee_info(
    "John Doe", 
    "Software Engineer", 
    department="IT", 
    years_of_experience=5, 
    manager="Alice Smith"
)
print()
employee_info(
    "Jane Smith", 
    "Product Manager", 
    location="San Francisco", 
    remote_work=True
)
print()
employee_info("Mark Brown", "Intern")  # No additional details


##***************************************************************************************************
## Global vs. Local variables
total = 0; 
def sum( arg1, arg2 ):
   total = arg1 + arg2; 
   print ("Inside the function local total : ", total)
   return total;

sum( 10, 20 );
print ("Outside the function global total : ", total)

##***************************************************************************************************
## Function with Return Statement
def calculate_area(radius):
    area = 3.14159 * radius ** 2  
    return area 

circle_radius = 5
area_result = calculate_area(circle_radius) 
print(f"The area of the circle with radius {circle_radius} is {area_result:.2f}")


##***************************************************************************************************
## Function Inside another Function
def calculate_total(price, percentage_Discount):

    def calculate_Discount(price, percentage_Discount):
        return price*(percentage_Discount/100)
    
    total_Discount=calculate_Discount(price, percentage_Discount)
    total_Price= price-total_Discount
    return total_Price

final_Price= calculate_total(500,15)
print("The final price after the Dicount is:", final_Price)




