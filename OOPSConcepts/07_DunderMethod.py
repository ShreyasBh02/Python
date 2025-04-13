'''
    Dunder/ Magic/ Special Method:
        This are the methods defined by Built-in classes in python
        Classes define these type of methods for creating custom objects
        Implementing operator overloading in python
        All the methods surrounding by doule Underscore is a dunder method
        
'''
a="Rohit"
b= "Sharma"
add=a.__add__(b)
print(add)
print()
num1 = 6
num2 = 5
print(num1.__mul__(num2))
print()

## List of all Dunder Method
print(dir(str)) 

##***************************************************************************************************
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price}"

    def __add__(self, other):
        return self.price + other.price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return "\n".join(str(item) for item in self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __contains__(self, product):
        return product in self.items

    def total_price(self):
        return sum(item.price for item in self.items)

# Create some products
p1 = Product("Laptop", 1200)
p2 = Product("Mouse", 25)
p3 = Product("Keyboard", 45)

# Create a shopping cart and add products
cart = ShoppingCart()
cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)

# Print cart items
print("Cart Contents:")
print(cart)

# Dunder methods in action
print("\nNumber of items in cart:", len(cart))      # __len__
print("\nFirst item in cart:", cart[0])             # __getitem__
print("\nIs Mouse in cart?", p2 in cart)            # __contains__
print("\nTotal Price: $", cart.total_price())       # custom method

# Using __add__ in Product
print("\nPrice of Laptop + Mouse:", p1 + p2)        # __add__

