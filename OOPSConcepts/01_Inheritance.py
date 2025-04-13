'''
## Inheritance:
    Child class inherits data definitions and methods from parent class.
    Syntax: 
        Class BaseClass:
            Body of base class
        Class DerivedClass (BaseClass):
            Body of derived class

'''

##***************************************************************************************************
## Single Level: When a derived class has only one parent class

# parent class
class Parent: 
   def parentMethod(self):
      print ("Calling parent method")

# child class
class Child(Parent): 
   def childMethod(self):
      print ("Calling child method")

# Object/ Instance of child
child_obj=Child()
child_obj.childMethod()         # calling method of child class
child_obj.parentMethod()        # calling method of Parent class

#Object/ Instance of parent
parent_obj=Parent()
parent_obj.parentMethod()
##parent_obj.childMethod() 
'''O/p:
Traceback (most recent call last):
  File "d:\Rest Assured_ATT\Python\Programs\OOPSConcepts\tempCodeRunnerFile.py", line 21, in <module>
    parent_obj.childMethod() 
    ^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'Parent' object has no attribute 'childMethod'
'''
## Moral of the Story:
## Chiild: Child can access the property of both self and Parent Property
## Parent: Whereas Parent can access only self properties but not the child's property.
##***************************************************************************************************
## Types of Python Inheritance
## 1: Single Level Inheritance

class ParentProperty:
    def house(self):
        print("The parent owns a house.")

class ChildProperty(ParentProperty):
    def car(self):
        print("The child owns a car.")

property_instance = ChildProperty()
property_instance.car()
property_instance.house()

##***************************************************************************************************
## METHOD OVERRIDING:
# Re-writing / re defining the methods of parent class in derived/ child class
# method  overriding> child class is very powerfull
# method overiding happend between two class
class Fruit():
    def fruitinfo(self):
        print("This is Fruit Family from fruit")

class Apple(Fruit):
    def appleinfo(self):
        print("This is apple info")
    def fruitinfo(self):
         print("This is apple info from apple")


info=Apple()
info.appleinfo()
info.fruitinfo()

##***************************************************************************************************
## 2: Multi- Level Inheritance
class GrandFather():
    def prop_GrandFather(self):
        print("I'm Your grand father, this is my Property")

class Father(GrandFather):
    def prop_Father(self):
        print("I'm Your Father, I have My Property along with Your GrandFather")


class Son(Father):
    def prop_Son(self):
        print("I'm the Son, I have My Property along with my Father")

## creating Oject of Son
sonProp=Son()
sonProp.prop_Son()
sonProp.prop_Father()
sonProp.prop_GrandFather()

## creating Oject of father
fatherprop=Father()
fatherprop.prop_Father()
fatherprop.prop_GrandFather()


## creating Oject of grandfather
grandfatherprop=GrandFather()
grandfatherprop.prop_GrandFather()


##***************************************************************************************************
## 3: Multiple Level Inheritance
# The Child class thus inherits the attributes and method from all parents. 
# The child can override methods inherited from any parent.

class ParentClass1:
    def method1(self):
        print("method1 of parent  class 1")

class ParentClass2:
    def method2(self):
        print("method2 of parent  class 2")

class ChildClass(ParentClass1, ParentClass2):
    def method(self):
        print ("Method of Child Class")

c1=ChildClass()
c1.method()
c1.method1()
c1.method2()

##***************************************************************************************************
## Diamond Ambiguity Problem: 
# it occurs when a class inherits from 2 or more than  2 class wil be there
# To tackle this pythin uses Method Resilution Order(MRO) algorithm called c3 Linerization
# Meaniing that the class that is inherited first in the derived class, that method will be called
class GrandParentClass:
    def grandmethod1(self):
        print("Method of Grand parent class ")

class ParentClass1(GrandParentClass):
    def Parentmethod(self):
        print("Method of parent class 1")

class ParentClass2(GrandParentClass):
    def Parentmethod(self):
        print("Method of parent class 2")

class ChildClass(ParentClass1,ParentClass2):
    def Childmethod(self):
        print ("Method of Child Class")


c1=ChildClass()
c1.Childmethod()
c1.Parentmethod()


##***************************************************************************************************

## Hierarchical Inheritance:This type of inheritance contains multiple derived classes that are inherited from a single base class
class Manager():
    def managerMethod(self):
        print("Im the Manager")

class Employee1(Manager):
    def employee1(self):
        print("Im Employee 1")
        
class Employee2(Manager):
    def employee2(self):
        print("Im Employee 2")

emp1 = Employee1()  
emp2 = Employee2()
emp1.employee1()
emp1.managerMethod()
emp2.employee2()
emp2.managerMethod()

##***************************************************************************************************
## Hybrid Inheritance
# Combination of two or more types of inheritance is called as Hybrid Inheritance. 
# For instance, it could be a mix of single and multiple inheritance.

# parent class
class CEO: 
   def ceoMethod(self):
      print ("I am the CEO")
      
class Manager(CEO): 
   def managerMethod(self):
      print ("I am the Manager")

class Employee1(Manager): 
   def employee1Method(self):
      print ("I am Employee one")
      
class Employee2(Manager, CEO): 
   def employee2Method(self):
      print ("I am Employee two")      

# creating instances 
emp = Employee2()
# method calls
emp.managerMethod() 
emp.ceoMethod()
emp.employee2Method()

##***************************************************************************************************
