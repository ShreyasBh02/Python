'''
    Decorator:
        Decorators allows to modify or to extend the behaviour or functions/class without modifiying them
        Similar to our Decorating our Home (Installing lights, Posters, etc)
    Whe we need Dcorators?
        Reusability of code
        Enhancing the unction without modifyting the original functions

'''
##***************************************************************************************************
## Function Decorators:
# Normal Approach:
def without_decorator_func():
    print("Something happens before the function is called")
    print(20+69)
    print("Something happens after the function is called")

## In this above approach you have to write all the lines as many times as we are computing the operation
## Thus it will take a lots of time

# Decorator Approach:
##Ex:1
def with_decorator_func(func): 
    def wrapper():
        print("Something happens before the function is called")
        func()
        print("Something happens after the function is called")
    return wrapper 

@with_decorator_func 
def add ():
    print("The addition is: ",12+54)

def say_Hello():
    print("Hello Bob!")

add()
say_Hello()


##Ex:2
import time
def time_decorator(func):
    def timer():
        start = time.time()
        func()
        end = time.time()
        print("The execution time is: ", end - start)
    return timer
    
@time_decorator
def operation():
    print(561016*6664+1002111)

operation()

## Function Decorators With Argument:
def repeat(n=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = []
            for _ in range(n):
                result.append(func(*args, **kwargs))
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    return (f"Hello {name}!")

print(greet("John Doe"))

##***************************************************************************************************
## Class Decorators:

## EX: 1
class ClassDecorator:
    def __init__(self, func):
        self.func=func

    def __call__(self): 
        print("Something happens before the function is called")
        self.func()
        print("Something happens after the function is called")
        

@ClassDecorator
def say_hello():
    print(f"Hello ")

say_hello()

## EX: 2
class AuthRequired:
    def __init__(self, func):
        self.func = func
        self.is_authenticated = False
    
    def login(self):
        self.is_authenticated = True
        print("[INFO] Usre logged in.")
    
    def logout(self):
        self.is_authenticated = False
        print("[INFO] User Logged out.")
    
    def __call__(self, *args, **kwargs):
        if not self.is_authenticated:
            print("[ERROR] Access denied: User is not authenticated.")
        else:
            print("[INFO] Access granted.")
            return self.func(*args, **kwargs)

@AuthRequired
def view_dashboard():
    print("Welcome to the Admin Dashboard!!")

view_dashboard()

view_dashboard.login()
view_dashboard()

view_dashboard.logout()
view_dashboard()

##***************************************************************************************************
## 3. Property Decorator: It allows method to be accessed as attributes
#                   

##***************************************************************************************************
## Built_in Decorators:
## 1. @ClassMethod: IT takes the class as the first argument
#                   Classmethod is bound to class and not the instance of the class
#                   class itself as thefirst argument >> conventionally cls
#     When Used: When we want to modify the class leve data 

class Math:
    @classmethod
    def add(cls, x ,y):
        return cls.__name__, x +y

result =  Math.add(3,5)
print(result)

##EX:1
class BankAccount:
    interest_rate = 0.03
    def __init__(self, account_number, balance =0):
        self.account_number = account_number
        self.balance = balance

    @classmethod
    def set_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
    
    @classmethod
    def from_string(cls, account_string):
        account_number , balance = account_string.split(",")
        return cls (account_number , float(balance ))

    def get_account_info(self):
        print(f"Accoount Number: {self.account_number}, Balance: {self.balance:.2f}, Interest Rate: {BankAccount.interest_rate:.2f}")


# Create an account using the factory method
account1 = BankAccount.from_string("123456, 5000")
account1.get_account_info()

# Modify the interest rate using the class method
BankAccount.set_interest_rate(0.05)
account1.get_account_info()

# Create another account
account2 = BankAccount("789012", 10000)
account2.get_account_info()

##***************************************************************************************************
## 2. @StaticMethod: The method whcih can be calle withiut creatubg any instance of class, method
#                   Classmethod is bound to class and not the instance of the class
#                   class itself as thefirst argument >> conventionally cls
#      When Used: When we dont want to interact with the class level data 

# Normal Approach
class Math():
    def add(self, x, y ):
        return x +y
a = Math()
print(a.add(2 ,6))

# Using Static Approach
class Math():
    @staticmethod
    def add( x, y ):
        return x +y

print(Math.add(2 ,6))

## EX:1
class Validator:
    @staticmethod
    def is_Valid_email(email):
        if "@" in email and "." in email and email.index("@") < email.index("."):
            return True
        return False
    
    @staticmethod
    def is_valid_password(password):
        if len(password) < 8:
            return False
        has_upper = any(char.isupper() for char in password)
        has_lower = any(char.islower() for char in password)
        has_digit = any(char.isdigit() for char in password)
        has_special = any(char in "!@#$%^&*.=+-/*" for char in password)
        return has_upper and has_lower and has_digit and has_special
    

emails =["abc@gmail.com" , "xyzgmail.com" , "user@domain"]
passwords = ["passwords@123", "password","AS123", "SecuRe$1"]

for email in emails:
    print(f"Is {email} a valid email? {Validator.is_Valid_email(email)}")
print()
for password in passwords:
    print(f"Is {password} a valid password? {Validator.is_valid_password(password)}")


##***************************************************************************************************

