'''
Dictionary:
    A Python dictionary is a data structure that stores the value in key: value pairs. 
    Values in a dictionary can be of any data type and can be duplicated, 
    whereas keys can’t be repeated and must be immutable.
'''
## Create a dictionary
## using dict() method
student_info = dict(name="Jhon Doe", age=21, major="Computer Science")
print("Dictionary using dict():",student_info)                                                                                          
##O/p: Dictionary using dict(): {'name': 'Jhon Doe', 'age': 21, 'major': 'Computer Science'}

## using key: Value pair
capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print("Dictionary using key: Value pair:",capitals)                                                                                     
##O/p: Dictionary using key: Value pair: {'Maharashtra': 'Mumbai', 'Gujarat': 'Gandhinagar', 'Telangana': 'Hyderabad', 'Karnataka': 'Bengaluru'}


##***************************************************************************************************
## Accessing the dictionary values
capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print(capitals["Maharashtra"])                                                                                                            
##O/p: Mumbai

my_dict = {
    'name': 'Jhon Doe',
    'age': 25,
    'city': 'New York',
    'subject':['Science','Maths','History','Scoial']
}

for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")
'''O/p:
    Key: name, Value: Jhon Doe
    Key: age, Value: 25
    Key: city, Value: New York
    Key: subject, Value: ['Science', 'Maths', 'History', 'Scoial']
'''

##***************************************************************************************************
## Updating the dictionary
student_info = {
   "name": "Alice",
   "age": 21,
   "major": "Computer Science"
}
student_info["age"] = 22
student_info["graduation_year"] = 2023
print("The modified dictionary is:")
for key, value in student_info.items():
    print(f"Key: {key}, Value: {value}")
'''O/p
The modified dictionary is:
Key: name, Value: Alice
Key: age, Value: 22
Key: major, Value: Computer Science
Key: graduation_year, Value: 2023
'''
##***************************************************************************************************

## Using del Keyword: it is used to remove an item or a slice of items from the dictionary, based on the specified key(s).

numbers={10:"Ten",20:"Twenty",30:"Thirty",40:"Forty"}
print(numbers)                                                                                  
##O/p: {10: 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Forty'}
del numbers[30]
print(numbers)                                                                                  
##O/p: {10: 'Ten', 20: 'Twenty', 40: 'Forty'}

## Using pop() Method:used to remove a specified key from a dictionary and return the corresponding value.

numbers={10:"Ten",20:"Twenty",30:"Thirty",40:"Forty"}
print("The Dictionary Before Pop: ", numbers)                                                   
 ##O/p: The Dictionary Before Pop:  {10: 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Forty'}
popnumbers= numbers.pop(30)
print("Pop element is: ", popnumbers)                                                            
##O/p: Pop element is:  Thirty
print("The Dictionary after Pop: ", numbers)                                                     
##O/p: The Dictionary after Pop:  {10: 'Ten', 20: 'Twenty', 40: 'Forty'}



## Using popitem() Method: used to remove and return the last key-value pair from a dictionary.

numbers={10:"Ten",20:"Twenty",30:"Thirty",40:"Forty"}
print("The Dictionary Before Pop: ", numbers)                                                    
##O/p: The Dictionary Before Pop:  {10: 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Forty'}
popnumbers= numbers.popitem()
print("popitem element is: ", popnumbers)                                                        
##O/p: popitem element is:  (40, 'Forty')
print("The Dictionary after popitem: ", numbers)                                                 
##O/p: The Dictionary after popitem:  {10: 'Ten', 20: 'Twenty', 30: 'Thirty'}


## Using clear() Method: used to remove all items from a dictionary. It effectively empties the dictionary, leaving it with a length of 0.

numbers={10:"Ten",20:"Twenty",30:"Thirty",40:"Forty"}
print("The Dictionary Before Pop: ", numbers)                                                    
##O/p: The Dictionary Before Pop:  {10: 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Forty'}
popnumbers= numbers.clear()
print("The Dictionary after clear: ", popnumbers)                                                
##O/p: The Dictionary after clear:  None

##***************************************************************************************************
## Loop Through Dictionaries

## Using a For Loop:  It repeatedly executes a block of code for each item in the sequence.
##1. Iterating over Keys
student = {"name": "Alice", "age": 21, "major": "Computer Science"}
for key in student:
   print(key, "= ",student[key])

##2. Iterating over Key-Value Pairs
student = {"name": "Alice", "age": 21, "major": "Computer Science"}
for key, value in student.items():
    print(key,":",value)


##***************************************************************************************************
## USe Cases:
##1. Storing User Information
reg_user={
    "Name" : "Jhon Doe",
    "Age"  : 32,
    "Email": "jhondoe@gmail.com",
    "Allow MFA": True
}

print("User Information:")
for key, value in reg_user.items():
   print(key ,":", value)

## 2. Product Stock Tracking
inventory = {
    'apple': 50,
    'banana': 30,
    'orange': 20,
    'grape': 10
}
def update_stock(product, quantity):
    if product in inventory:
        inventory[product] += quantity
    else:
        inventory[product] = quantity

def check_stock(product):
    return inventory.get(product,"Product not available")

update_stock('banana', 10)  
print(check_stock('banana'))


## 3. Mapping Routes to Handlers
routes = {
    '/home': 'home_page_handler',
    '/about': 'about_page_handler',
    '/contact': 'contact_page_handler'
}

def home_page_handler():
    return "Welcome to the Home Page"

def about_page_handler():
    return "This is the About Page"

def contact_page_handler():
    return "Contact us at contact@example.com"

def handle_request(route):
    handler = routes.get(route)
    if handler:
        if handler == 'home_page_handler':
            return home_page_handler()
        elif handler == 'about_page_handler':
            return about_page_handler()
        elif handler == 'contact_page_handler':
            return contact_page_handler()
    else:
        return "404 Not Found"

print(handle_request('/about'))  

