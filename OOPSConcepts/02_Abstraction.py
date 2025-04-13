'''
## Abstraction:
    Concept of hiding complex implementation
    Hiding unneeded details and exposing the required.

    Syntax: 
     from abc import ABC  
     class ClassName(ABC):  

    EX: We use Amamzon webapplication. Do you see the backend code ?
    Abstraction can be achieved using abstract class >> import ABC
    import ABC collection of multiple functions is a module
'''

##***************************************************************************************************
# Import required modules
from  abc import ABC, abstractmethod

# Create Abstract base class
class Shape(ABC):

    # Create abstract method  
    @abstractmethod
    def calculate_area(self):
        pass

    # Create abstract method  
    @abstractmethod
    def calculate_Perimeter(self):
        pass

    # Create concrete method
    def display_measurements(self):
        print(f"Area: {self.calculate_area()}")
        print(f"Perimeter: {self.calculate_Perimeter()}")

# Create a child class
class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius
    
    def calculate_Perimeter(self):
        return 2 * 3.14 * self.radius

# Create a child class
class Rectangle(Shape):
    def __init__(self, leghth, width):
        self.leghth=leghth
        self.width=width

    def calculate_area(self):
        return self.leghth* self.width
    
    def calculate_Perimeter(self):
        return 2 * (self.leghth + self.width)

# Call methods
circle =Circle(5)
circle.display_measurements()

rectangle=Rectangle(5,2)
rectangle.display_measurements()

















