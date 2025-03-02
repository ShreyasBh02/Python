'''
##List: List is one of the built-in data types in Python. 
    * A Python list is a sequence of comma separated items, enclosed in square brackets [ ]. 
    * List can contain duplicate items.
    * List in Python are Mutable. Hence, we can modify, replace or delete the items.
    * List are ordered. It maintain the order of elements based on how they are added.
    * Accessing items in List can be done directly using their position (index), starting from 0.
'''

## Create a List
# 1. Using [] brackets
a = [1, 2, 3, 4, 5]
b = ['apple', 'banana', 'cherry']
c = [1, 'hello', 3.14, True]

print(a)
print(b)
print(c)

#2. Using list() Constructor
a = list((1, 2, 3, 'apple', 4.5))  
print(a)

##***************************************************************************************************
## List Indexing 
list =[1,2,3,4,5,6]
'''
+Ve index:          0   1    2   3   4   5 
list                1   2    3   4   5   6
-Ve index:         -6   -5  -4  -3  -2  -1   
'''
## Accessing the List
print(list[2:5])                            ## O/p: [3, 4, 5]         
print(list[5])                              ## O/p: 6
print(list[-1])                             ## O/p: 6
print(list[3:])                             ## O/p: [4, 5, 6] 
print(list[:-1])                            ## O/p: [1, 2, 3, 4, 5]
print(list[-3:-1])                          ## O/p: [4, 5] 

##***************************************************************************************************

## Update the List
fruits=["apple", "Mango","Banana", "Orange"]

print(fruits)                       # O/p: ['apple', 'Mango', 'Banana', 'Orange']
# append(): Adds an element at the end of the list.
append_Fruits=fruits.append("Grapes")
print(fruits)                       # O/p: ['apple', 'Mango', 'Banana', 'Orange', 'Grapes']

# extend(): Adds multiple elements to the end of the list.
fruits.insert(1, "Gava")  
fruits.insert(4, "Pineapple")
fruits.insert(6, "Strawberries")
print(fruits)                       # O/p: ['apple', 'Gava', 'Mango', 'Banana', 'Pineapple', 'Orange', 'Strawberries', 'Grapes']

# insert(): Adds an element at a specific position.
fruits.extend(["Peaches", "Blueberries"])
print(fruits)                       #O/p: ['apple', 'Gava', 'Mango', 'Banana', 'Pineapple', 'Orange', 'Strawberries', 'Grapes', 'Peaches', 'Blueberries']

##***************************************************************************************************
## Remove the element
shopping_Item=["Jeans", "T-shirt", "Car", "Laptop", "Home", "Mobile"]
print(shopping_Item)                   # O/p: ['Jeans', 'T-shirt', 'Car', 'Laptop', 'Home', 'Mobile']

# remove(): Removes the first occurrence of an element.
shopping_Item.remove("Car")
print(shopping_Item)                   # O/p: ['Jeans', 'T-shirt', 'Laptop', 'Home', 'Mobile']

#pop(): Removes the element at a specific index or the last element if no index is specified.
shopping_Item.pop(3)
print(shopping_Item)                   # O/p: ['Jeans', 'T-shirt', 'Laptop', 'Mobile']

# del statement: Deletes an element at a specified index
del shopping_Item[1]
print(shopping_Item)                   # O/p: ['Jeans', 'Laptop', 'Mobile']

# clear statement: clear an element from list wont clear the variable
shopping_Item.clear()
print(shopping_Item)                   # O/p: []


##***************************************************************************************************
## List is mutable
'''
Lists are mutable, which means you can change their content without changing their identity. 
This mutability allows you to modify lists by adding, removing, or changing elements directly.
'''
# 1. Creating a List
my_list = [10, 20, 30, 40, 50]

# 2. Changing an Element in the List (Mutable Operation)
print("Original List:", my_list)
my_list[1] = 100
print("After Changing Element at Index 1:", my_list)

# 3. Adding Elements to the List
my_list.append(60)  
print("After Appending 60:", my_list)

# Adding an element at the beginning of the list using insert()
my_list.insert(0, 5)  
print("After Inserting 5 at Index 0:", my_list)

# 4. Removing Elements from the List
my_list.remove(100)  
print("After Removing 100:", my_list)

# Removing an element at a specific index (index 3 in this case)
removed_item = my_list.pop(3) 
print("After Popping Element at Index 3:", my_list)
print("Removed Item:", removed_item)

# 5. Changing the Length of the List
my_list.append(70)  
my_list.append(80)
print("After Appending 70 and 80:", my_list)

# 6. Modifying Elements In-Place
for i in range(len(my_list)):
    my_list[i] *= 2 
print("After Doubling Each Element:", my_list)

# 7. Final List Operations
print("Final List after all operations:", my_list)
''' O/P
Original List: [10, 20, 30, 40, 50]
After Changing Element at Index 1: [10, 100, 30, 40, 50]
After Appending 60: [10, 100, 30, 40, 50, 60]
After Inserting 5 at Index 0: [5, 10, 100, 30, 40, 50, 60]
After Removing 100: [5, 10, 30, 40, 50, 60]
After Popping Element at Index 3: [5, 10, 30, 50, 60]
Removed Item: 40
After Appending 70 and 80: [5, 10, 30, 50, 60, 70, 80]
After Doubling Each Element: [10, 20, 60, 100, 120, 140, 160]
Final List after all operations: [10, 20, 60, 100, 120, 140, 160]

'''
##***************************************************************************************************
## Deep copy and Shallow copy
##Shallow copy: Modifications to mutable elements inside the copy will affect the original object.
original_list = [1, 2, [3, 4]]
print("Original list:", original_list)                              # Output: Original list: [1, 2, [3, 4]
shallow_copied_list = original_list
shallow_copied_list[2][0] = 99
print("Shallow copied list:", shallow_copied_list)                  # Output: Shallow copied list: [1, 2, [99, 4]]
print("Original list:", original_list)                              # Output: Original list: [1, 2, [99, 4]]

## Deep Copy:Modifications to the deep copy or any of its inner objects do not affect the original object.
import copy
original_list = [1, 2, [3, 4]]
print("Original List:", original_list)                                  # Output: [1, 2, [3, 4]]
deep_copy_list = copy.deepcopy(original_list)
deep_copy_list[2][0] = 99

print("Original List:", original_list)                                  # Output: [1, 2, [3, 4]]
print("Deep Copy List:", deep_copy_list)                                # Output: [1, 2, [99, 4]]

##***************************************************************************************************
## List Comprehension
prices =[10,6,78,36.5]
doubled_Price=[]
for i in prices:
    doubled_Price.append(i*2)
print(doubled_Price)                                            # O/p: [20, 12, 156, 73.0]

## above code can be written as below
print([price* 2 for price in prices])                           # O/p: [20, 12, 156, 73.0]
                               


##***************************************************************************************************
## Built-in Functions 
## 1. len(list): Gives the total length of the list.
list_1=[1,6.5,0,9,"XYZ"]
list_2=[5,4,4.8,9,"ABC"]
if len(list_1)==len(list_2):
    print("Equal length of List")
else:
    print("Unequal length of List")
'''
O/p: Equal length of List
'''

## 2. max(list): Returns item from the list with max value.
## 3. min(list): Returns item from the list with min value.
list1 = [103, 675, 321, 782, 200]  
print("Max no is:",max(list1))  
print("Min no is:",min(list1))  
'''
O/p:
Max no is: 782
Min no is: 103
'''

## 4. list(seq): Converts a tuple into list.
aTuple = (123, 'xyz', 'zara', 'abc')
aList = list(aTuple)
print("List elements : ", aList)
'''
O/p:
List elements :  [123, 'xyz', 'zara', 'abc']
'''



##***************************************************************************************************
#USE Cases
## 1. Tracking Student Grades
grades = [85, 92, 78, 88, 94]
average_grade = sum(grades) / len(grades)
highest_grade = max(grades)
lowest_grade = min(grades)

print(f"Average Grade: {average_grade}")
print(f"Highest Grade: {highest_grade}")
print(f"Lowest Grade: {lowest_grade}")
'''
O/p:
Average Grade: 87.4
Highest Grade: 94
Lowest Grade: 78
'''

## 2. Compare the list and find the common element
list1 = [1,2,3,4,5,6]    
list2 = [7,8,9,2,10]   
for x in list1:
   for y in list2:
        if x== y:
            print("The common element is: ", x)