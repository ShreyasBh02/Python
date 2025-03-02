## 1. Sum and Multiplication Items in List
num=[56.9,87,3,45,0.9,56]
sum=0
mul=1
for i in num:
    sum+=i
    mul=mul*i
print("The sum of the list is:",sum)
print("The Mul of the list is:",mul)

## 2.  Get Largest and Smallest Number in List
num=[56.9,87,3,45,0.9,56]
largest_num=num[0]
smallest_num=num[0]
for no in num:
    if no >largest_num:
        largest_num=no
    if no < smallest_num:
        smallest_num=no
print("The largest number is:", largest_num)
print("The smallest number is:", smallest_num)

## 3.  Remove Duplicates from List
num_List= [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
unique_List = []
for num in num_List:
    if num not in unique_List:
        unique_List.append(num)

print(unique_List)


##4. WAP to store seven fruits in a list entered by the user.
fruits = []
for i in range(7):
    fruit = input("Enter the name of fruit {}: ".format(i+1))
    fruits.append(fruit)
print("The list of fruits is:", fruits)
