import re

##String: •	Python string is the collection of characters surrounded by single quotes, double quotes, or triple quotes. 
##        •	The computer does not understand the characters; internally, it stores manipulated character as the combination of the 0's and 1's.


## ACII Representation:
char = "A"
ascii_value = ord(char)
print(ascii_value)

print(ord("F"))

## Print all the ASCII Values A-Z and a-z
# ASCII values of A-Z
print("ASCII values of A-Z:")
for i in range(65, 91):
    print(f"{chr(i)}: {i}", end=" ")
print()
print("\nASCII values of a-z:")
# ASCII values of a-z
for i in range(97, 123):
    print(f"{chr(i)}: {i}", end=" ")


##String Declration
singleQuote = 'String with single quote'
doubleQuote = "String with Double quote"
tripleQuote = '''String with Triple quote'''
print(singleQuote)
print(doubleQuote)
print(tripleQuote)

##Q. Print Multi line string
poem='''Twinkle, twinkle, little star,
How I wonder what you are! 
Up above the world so high,   		
Like a diamond in the sky. 
Twinkle, twinkle, little star, 
How I wonder what you are'''

print(poem)

##String Functions

##1.Concatenation of strings
str_1="Hello"
str_2="Python"
Con_str=str_1 + str_2
print(Con_str)          ##O/P: HelloPython

##Accessing the String

'''
+Ve index:            0   1    2   3   4   5   6
string                S   h    r   e   y   a   s
-Ve index:           -7  -6   -5  -4  -3  -2  -1   
'''
str="Shreyas"
##PArticulare index values
print(str[1])                        ##O/P: h
print(str[-6])                       ##O/P: h

##start and stop
print(str[0:3])                       ##O/P: Shr
print(str[-3:-1])                     ##O/P: ya  
print(str[-3:])                       ##O/P: yas  

##Start,Stop, End                       
print(str[0:5:2])                     ##O/P: Sry
print(str[-5:-1:3])                   ##O/P: ra  

##Accessing the Out of index element
print(str[7])                         ##O/p: IndexError: string index out of range

## String is Immutable
str="hello Python"
str[0]="H"
print(str)
'''
        Traceback (most recent call last):
        File "d:\Rest Assured_ATT\Python\Programs\DataStructure\tempCodeRunnerFile.py", line 2, in <module>
            str[0]="H"
            ~~~^^^
        TypeError: 'str' object does not support item assignment
'''

##***************************************************************************************************

## Common String Methods
## 1. count():
text = "banana"
print(text.count("a"))                              ## O/p: 3

## 2. upper() and lower():
str="Hello World"
print("Upper case:", str.upper())                   ## O/p: Upper case: HELLO WORLD
print("Lower case:", str.lower())                   ## O/p: Lower case: hello world

## 3. split()
buckItems="SoloTrip, Money, Bugaati, Banana"
print(buckItems.split(","))                         ## O/p: ['SoloTrip', ' Money', ' Bugaati', ' Banana']

## 4. join()
buckItems= ['SoloTrip', ' Money', ' Bugaati', ' Banana']    
print(",".join(buckItems))                           ## O/p: SoloTrip, Money, Bugaati, Banana

## 5. replace(old, new)
text = "I like cats"
print(text.replace("cats", "dogs"))                   ## O/p: I like dogs


##***************************************************************************************************

## String Built-In Functions:
## 1. len():
password = "Admin123"
if len(password) >= 8:
    print("Password is valid.")                         ## O/p: Password is valid.

## 2.sorted():
toDoItems= "Apple"
print(sorted(toDoItems))                                ## O/p: ['A', 'e', 'l', 'p', 'p']


##***************************************************************************************************

## Escape Sequences
## \n
adress=""" C-445, \n Standford End,\n Green road, 12345"""
print(adress)
'''O/p:
 C-445, 
 Standford End,
 Green road, 12345
'''

## \t
table="Name\tAge\tGrade \nJhon\t54\t5 \nRam\t\t14\t10"
print(table)
'''O/p:
Name	Age	Grade 
Jhon	54	5 
Ram		14	10
'''
## \' single quote escape
str1= 'I\'m a Jhon Doe '
print(str1)

##\r =moves the cursor to the begining of line
print("Hello, \rI'm Jhon Doe and I'm from India")
'''O/p:
Hello, 
I'm Jhon Doe and I'm from India
''' 




##***************************************************************************************************
#USE Cases
## 1. validate login page

# userName=input("Enter the Username")
# password= input("Enter the password")
userName = 'abc@gmail.com'
password = 'Admin'

# Check if the username contains '@'
if "@" in userName:
    print("Valid Username")
    
    # Check if the password length is at least 6 characters
    if len(password) >= 6:
        print("Valid Password")
    else:
        print("Password must be at least 6 characters long.")
else:
    print("Invalid Username. The username must contain '@'.")


## 2. validate username is alredy in used or not
reg_Usname=["Jhon", "Doe","Ram"]
new_Usname="Sham"
if new_Usname in reg_Usname:
    print("Alredy in use")
else:
    print("Username is available") 

## 3. Arrange the all files name as per order
filesName=["python", "Java", "Postman", "SSMS","API"]
print(sorted(filesName))


## 3. From the user email address extract the Domin
emails = ["john.doe@gmail.com", "alice.smith@outlook.com", "bob@company.org", "invalidemail.com"]
def validate_email(email):
    if "@" in email and "." in email.split("@")[1]:
        return True
    return False

def extrcat_domain(email):
    return email.split("@")[1]

for email in emails:
    if validate_email(email):
        print(f"Valid email: {email}")
        domain=extrcat_domain(email)
        print(f"Domain: {domain}")
    else:
        print(f"Invalid email: {email}")

## 4. Password Strength Checker
import re

passwords = ["admin123", "Admin@2025", "1234", "Passw0rd!"]
for password in passwords:
    if len(password)>=8:
        if re.search(r"\d", password) and re.search(r"[A-Z]", password) and re.search(r"[!@#$$%^&*]", password):
            print ("Strong Password")
        else:
            print("Weak Password: Must include a digit, an uppercase letter, and a special character.")
    else:
       print("Weak Password: Password must be at least 8 characters long.")

'''O/p:
Weak Password: Must include a digit, an uppercase letter, and a special character.
Strong Password
Weak Password: Password must be at least 8 characters long.
Strong Password
'''

## 5. Program to Count Repeated Letters in a String:
name="Programming is fun and Python is awesome."
letter_count={}
for char in name:
    if char.isalpha():
        char=char.lower()
        if char in letter_count:
            letter_count[char]+=1
        else:
             letter_count[char]=1

repeated_letters = {letter: count for letter, count in letter_count.items() if count > 1}
print("Repeated Letters and their Counts:")
for letter, count in repeated_letters.items():
    print(f"'{letter}': {count}")

'''O/p:
Repeated Letters and their Counts:
'p': 2
'r': 2
'o': 3
'g': 2
'a': 3
'm': 3
'i': 3
'n': 4
's': 3
'e': 2
'''
