import random

## Practical Questions
## STRING

## 1. WAP to create a string with your name and print it
userName="Shreyas Bhagat"
print(userName)                                                                                                 
##O/P: Shreyas Bhagat

## 2. WAP to find the length of the string "Hello World"
str="Hello World"
## using len()
print("The lenght of '", str, "' is:", len(str))

## using the for loop
letter_count=0
for char in str:
    letter_count += 1
print("The length of '", str, "' using for loop is:", letter_count)        
'''O/p:
The lenght of ' Hello World ' is: 11
The length of ' Hello World ' using for loop is: 11
'''

## 3. WAP to slice the first 3 characters from the string "Python Programming"
string ="Python Programming"
sliceString=string[0:3]
print ("The string after 3 character sliced is: ",sliceString)                                                   
## O/p: The string after 3 character sliced is:  Pyt

## 4. WAP to convert the string "hello" to uppercase
text="hello"
uppercaseStr=text.upper()
print("Uppercase string is: ",uppercaseStr)

## 5. WAP to replace the word "apple" with "orange" in the string "I like apple"
string = "I like apple"
## using replace() method
print("The string before replace:", string)
print("The string after using replace() method:", string.replace("apple", "orange"))

## Using split() and join() methods
words=string.split()
words=[word if word !="apple" else "orange" for word in words]
replaced_string = " ".join(words)
print("The string after replacement:", replaced_string)

##***************************************************************************************************
## LIST
## 6. WAP to create a list with numbers 1 to 5 and print it
number=[1,2,3,4,5]
print(number)

## 7. WAP to append the number 10 to the list [1, 2, 3, 4]
num=[1, 2, 3, 4]
print("The List before append:", num)
num.append(10)
print("The List after using append() method:", num)

## 8. WAP to remove the number 3 from the list [1, 2, 3, 4, 5]
num=[1, 2, 3, 4, 5]
print("The List before remove():", num)

## using remove() method
num.remove(3)
print("The List after using remove() method:", num)

## 9. WAP to access the second element in the list ['a', 'b', 'c', 'd']
list=['a', 'b', 'c', 'd']
## using pop() method
list.pop(1)
print("The List after using pop() method:", list)

## 10. WAP to reverse the list [10, 20, 30, 40, 50].
num = [10, 20, 30, 40, 50]
## Using reverse() method
num.reverse()
print("Reversed list using reverse() method:", num)

## Using Slicing
num = [10, 20, 30, 40, 50]
reversed_num = num[::-1]
print("Reversed list using slicing:", reversed_num)

##***************************************************************************************************
## TUPLE
## 11. WAP to create a tuple with the elements 100, 200, 300 and print it.
tupleEle= (100,200,300)
print("The tuple with element:", tupleEle)

## 12. WAP to access the second-to-last element of the tuple ('red', 'green', 'blue', 'yellow').
element=('red', 'green', 'blue', 'yellow')
second_last=element[-2]
print("The second-to-last element is:",second_last)

## 13. WAP to find the minimum number in the tuple (10, 20, 5, 15).
numTuple=(10, 20, 5, 15)
##using min() method
minNum = min(numTuple)
print("The minimum number in the tuple is Using min():", minNum)

## Using for loop
min_Num=numTuple[0]
for num in numTuple:
    if num < min_Num:
        min_Num=num

print("The minimum number in the tuple is:", minNum)


## 14. WAP to find the index of the element "cat" in the tuple ('dog', 'cat', 'rabbit').
animal=('dog', 'cat', 'rabbit')
index_of_cat = animal.index('cat')
print("The index of 'cat' is:", index_of_cat)

## 15. WAP to create a tuple containing three different fruits and check if "kiwi" is in it.
fruits = ("Apple", "Orange", "Banana", "Grapes")
if "kiwi" in fruits:
    print("Kiwi is in the tuple.")
else:
    print("Kiwi is not in the tuple.")

##***************************************************************************************************
## SET
## 16.WAP to create a set with the elements 'a', 'b', 'c' and print it.
ele={'a', 'b', 'c'}
print("The set with elements:", ele)

## 17. WAP to clear all elements from the set {1, 2, 3, 4, 5}.
numSet={1, 2, 3, 4, 5}
print("The set before Clear all elements:", numSet)
numSet.clear()
print("The set after clearing all elements:", numSet)

## 18. WAP to remove the element 4 from the set {1,2,3,4}
numSet={1, 2, 3, 4}
numSet.remove(4)
print("The set after removing element 4:", numSet)

## 19. WAP to find the union of two sets {1, 2, 3} and {3, 4, 5}.
numSet1={1, 2, 3}
numSet2={3, 4, 5}
## using Union() Method
union_Set=numSet1.union(numSet2)
print("The union of set using Union() Method is: ",union_Set)

## Using | operator
print("The union of set using | operator is: ",numSet1|numSet2)

## 20. WAP to find the intersection of two sets {1, 2, 3} and {2, 3, 4}.
numSet1= {1, 2, 3}
numSet2= {2, 3, 4}
## using intersection() Method
intersection_Set=numSet1.intersection(numSet2)
print("The intersection of set using intersection() Method is: ",intersection_Set)

## Using $ operator
print("The intersection of set using & operator is: ",numSet1 & numSet2)

##***************************************************************************************************
## DICTIONARY
## 21. WAP to create a dictionary with the keys "name", "age", and "city", and print it.
userData={
    "name": "Jhon Doe",
    "age" :30,
    "city": "New York"
}

for key, value in userData.items():
    print(f"Key: {key} Value: {value}")

## 22. WAP to add a new key-value pair "country": "USA" to the dictionary {'name': 'John', 'age': 25}
userData={
    "name": "Jhon",
    "age" :25
}
print("Dictionary Before:")
for key in userData:
   print(key, "= ",userData[key])

userData["country"] = "USA"
print("\nDictionary After:")
for key in userData:
    print(key, "=", userData[key])


## 23. WAP to access the value associated with the key "name" in the dictionary {'name': 'Alice', 'age': 30}
userData={'name': 'Alice', 'age': 30}
print(f"The value of key name is {userData['name']}")

## 24. WAP to remove the key "age" from the dictionary {'name': 'Bob', 'age': 22, 'city': 'New York'}.
userData={'name': 'Bob', 'age': 22, 'city': 'New York'}
print("Dictionary Before removing the age:")
for key in userData:
   print(key, "= ",userData[key])

userData.pop('age')
print("\nDictionary After removing the age:")
for key in userData:
    print(key, "=", userData[key])

## 25. WAP to check if the key "city" exists in the dictionary {'name': 'Alice', 'city': 'Paris'}.
userData= {'name': 'Alice', 'city': 'Paris'}
if 'city' in userData:
    print("The key 'city' exists in the dictionary.")
    print(f"The value of 'city' is: {userData['city']}")
else:
    print("The key 'city' does not exist in the dictionary.")


##***************************************************************************************************

## 26. WAP to create a list, a tuple, and dictionary abd print them all.
dataList=[1, 'hello', 3.14, True]
dataTuple=('physics', 'chemistry', 1997, 2000)
dataDictionary={10:"Ten",20:"Twenty",30:"Thirty",40:"Forty"}

print("List:", dataList)
print("Tuple:", dataTuple)
print("Dictionary:", dataDictionary)

## 27. WAP to create a list of 5 random numbers between 1 and 100, sort it in ascending order, and print the result.(replaced)
import random as randoms
random_numbers = []
random_numbers = [randoms.randint(1, 100) for _ in range(5)]

random_numbers.sort()

print("Sorted list of random numbers:", random_numbers)

## 28. WAP to create a list with strings and print the element at the third index.
userName = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
print("The element at index 3 is:", userName[3])

## 29. WAP to combine two dictionaries into one and print the result.
userData_1={"name": "Alice", "age": 21, "major": "Computer Science"}
userData_2={"name": "Jhon", "age": 30, "major": "Masters in CS"}

combinedData = userData_1.copy() 
combinedData.update(userData_2)
print("Combined Dictionary using update():", combinedData)

## 30. WAP to convert a list of strings into a set.
stringList = ['apple', 'banana', 'cherry', 'apple', 'banana']
stringSet = set(stringList)
print("Set of strings:", stringSet)











