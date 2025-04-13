'''
## Encapsulation:
    Means hiding something
    Bundling of data and methoods of class

## Access Modifier:
    Public, Protected, Private
    Access specifiers in Python have an important role to play in securing data from unauthorized access and in preventing it from being exploited.

'''
##***************************************************************************************************
## Public (name): The members of the public access modifier can be accessed anywhere.
class employee:
    def __init__(self, name="Sachin", age=10):
        self.name=name
        self.age=age

    def getEmpDetails(self):
        print("Name:", self.name, "Age:", self.age)


emp1=employee()
emp1.getEmpDetails()
emp2=employee("Rohit", 45)
emp2.getEmpDetails()

##***************************************************************************************************
## Protected (_name): The members of the protected access modifier should be accessed only within the class and its subclasses.

class Employee:
    def __init__(self):
        self._id = 7

class HR(Employee):
    def __init__(self, name):
        self.name=name
        Employee.__init__(self)
    
    def getDetails(self):
        print("Name: ", self.name, "ID:", self._id)

hr=HR("MSD")
hr.getDetails()
print(hr.name)
print(hr._id)

##***************************************************************************************************
## Private (__name): The members of the private access modifier can be accessed only within the class (using name mangling).

class employee:
    def __init__(self, name, age):
        self.name=name
        self.__age=age

    def getEmpDetails(self):
        print("Name:", self.name, "Age:", self.__age)

emp1=employee("Sachin",10)
emp1.getEmpDetails()
print(emp1.__age)
'''Traceback (most recent call last):
  File "d:\Rest Assured_ATT\Python\Programs\OOPSConcepts\tempCodeRunnerFile.py", line 13, in <module>
    print(emp1.__age)
          ^^^^^^^^^^
AttributeError: 'employee' object has no attribute '__age'
'''
## Method as Private:
class Student:
    def __init__(self, name, no):
        self.name = name
        self.__no= no

    def show(self):
        print("Name: ", self.name, "Degree: ",self.__no)

    def __private_method(self):
        print("This Method is private method") 

stu = Student("Virat", 18)
stu.show()
stu.__private_method()
'''
Traceback (most recent call last):
  File "d:\Rest Assured_ATT\Python\Programs\OOPSConcepts\tempCodeRunnerFile.py", line 15, in <module>
    stu.__private_method()
    ^^^^^^^^^^^^^^^^^^^^
AttributeError: 'Student' object has no attribute '__private_method'
'''
## Access private method
class Student:
    def __init__(self, name, no):
        self.name = name
        self.__no= no

    def show(self):
        print("Name: ", self.name, "Degree: ",self.__no)

    def __private_method(self):
        print("This Method is private method") 
    
    def access_privatemethod(self):
        self.__private_method()

stu = Student("Virat", 18)
stu.show()
stu.access_privatemethod()

##***************************************************************************************************

## Getters and Setters

class person:
    def __init__(self, name):
        self.__name=name

    ## Getter
    def get_Name(self):
        return self.__name
    
    ## Setter
    def set_Name(self, name):
        if len(name)>0:
            self.__name=name
        else:
            print("Name can't be empty.")

p=person("Dravid")
print(p.get_Name())

p.set_Name("Bob")
print(p.get_Name()) 



