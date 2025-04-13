'''
    Property Decorator:
       Python's property() built-in function is an interface for accessing instance variables of a class. 
'''
##***************************************************************************************************
## Normal Approach
class Student:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

stud = Student("Sachin", 3008)
#print (stud.__name)
'''
AttributeError: 'Student' object has no attribute '__name'
'''    
print(stud._Student__name)


## Using Property Approach
class Student: 
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
    
    @property
    def access_price(self):
        return self.__price

stud = Student("Sachin", 3008)
print(stud.access_price)


## EX: 1
class HotelRoom:
    def __init__(self, room_type, base_price):
        self._room_type = room_type
        self._base_price = base_price
        self._discount = 0
    
    @property
    def price(self):
        return self._base_price - (self._base_price * self._discount / 100)
    
    @price.setter
    def price(self, discount):
        if discount <0 or discount >100:
            raise ValueError ("Discount must be between 0 and 100 percent")
        self._discount = discount

    @property
    def room_details(self):
        return f"Room Type: {self._room_type}, Base Price: ${self._base_price:.2f}"
    

room1 = HotelRoom("Deluxe", 200)
print(room1.room_details)
print("Price after discount: $", room1.price)

# Apply a discount
room1.price = 10  
print("Price after applying 10% discount: $", room1.price)

# Invalid discount (raises error)
# room1.price = -5  
        

