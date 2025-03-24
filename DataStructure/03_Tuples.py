'''
Tuples:
    Tuple is one of the four primary data types in Python. 
    It is a used for storing a ordered collection of objects.
    Tuples are an immutable data type.
'''
## Create the Tuple     
integerTuple = (3, 6, 7, 10, 16, 23)  
print("Tuple with integers: ", integerTuple)                            ##O/p: Tuple with integers:  (3, 6, 7, 10, 16, 23)   

mixedTuple = (6, "Python", 14.3)      
print("Tuple with different data types: ", mixedTuple)                  ##O/p: Tuple with different data types:  (6, 'Python', 14.3)

nestedTuple = ("Python", {4: 5, 6: 2, 8:2}, (5, 3, 5, 6))               ##O/p: A nested tuple:  ('Python', {4: 5, 6: 2, 8: 2}, (5, 3, 5, 6))
print("A nested tuple: ", nestedTuple) 

## Index and Slicing ot Tuples
my_tuple = (10, 20, 30, 40, 50)
'''
+Ve index:            0     1       2       3       4
Tuple                10    20      30      40      50
-Ve index:           -5    -4      -3      -2      -1   
'''
print(my_tuple[0])                                                      # O/p:  10
print(my_tuple[2])                                                      # O/p:  30
print(my_tuple[-1])                                                     # O/p:  50

##Slicing
my_tuple = (10, 20, 30, 40, 50)

print(my_tuple[1:4])                                                    ## O/p: (20, 30, 40)
print(my_tuple[:3])                                                     ## O/p: (10, 20, 30)
print(my_tuple[2:])                                                     ## O/p: (30, 40, 50)
print(my_tuple[::2])                                                    ## O/p: (10, 30, 50)
print(my_tuple[::-1])                                                   ## O/p: (50, 40, 30, 20, 10)

## Access values
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )                                           
print ("tup1[0]: ", tup1[0])                                            ##O/p: tup1[0]:  physics
print ("tup2[1:5]: ", tup2[1:5])                                        ##O/p: tup2[1:5]:  (2, 3, 4, 5)

## Updating Tuples
tup1 = ('physics', 'chemistry', 1997, 2000)
tup1[0]=('Biology')
print ( tup1)  
''' O/p:
Traceback (most recent call last):
  File "d:\Rest Assured_ATT\Python\Programs\DataStructure\tempCodeRunnerFile.py", line 3, in <module>
    tup1[0]=('Biology')
    ~~~~^^^
TypeError: 'tuple' object does not support item assignment
'''

## Deleting a Tuple
tup= (5,69,74,96,0)
del tup
print(tup)
'''o/P:
Traceback (most recent call last):
  File "d:\Rest Assured_ATT\Python\Programs\DataStructure\tempCodeRunnerFile.py", line 4, in <module>
    print(tup)
          ^^^
NameError: name 'tup' is not defined
'''

##***************************************************************************************************
## Tuple Built-In Methods

## 1.index():
a = ["cat", "dog", "tiger"]
print(a.index("dog"))


##***************************************************************************************************

## Tuple Built-In Functions:



##***************************************************************************************************
#USE Cases
## 1. validate login page