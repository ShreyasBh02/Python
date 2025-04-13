'''
    Class:
        Bpund to the class (and not to a particular instance of the class), 
        and Attributes associates to a class across all the instances
        @classmethod decorater
        instead of self, cls as first Parameter
    
'''
class Student:
    ## constructor>> Constructing class with initialisation of variable/data
    def __init__(self, name):
        self.name=name

obj =Student("Alice")
print(obj.name)


class Student:
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def student_details(cls, name):
        return cls(name)


stu=Student.student_details("Ricky Pointing")
print(stu.name)

##***************************************************************************************************
class Circle:
    pi=3.141

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_Diameter(cls, diameter):
        radius=diameter/2
        return cls(radius)
    
    @classmethod
    def get_pi(cls):
        return cls.pi

# Creating an instance using the class method
circle1 = Circle.from_Diameter(10)
print(f"Circle with radius: {circle1.radius}")  

# Accessing class variable using class method
print(f"Value of pi: {Circle.get_pi()}")  