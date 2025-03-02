##  Q1.Wap to print right triangle with '*'
"""O/P:
    *
    **
    ***
    ****
    *****
"""
##using while loop
row =1
while row<=5:
    col=1
    while col<=row:
        print('*' ,end ="")
        col = col+1
    print()
    row=row+1


print()
##using For loop
for i in range(5):
    for j in range(i+1):
        print('*' ,end ="")
    print()

##  Q2.Wap to print Down right triangle with '*'
"""O/P:
    *****
    ****
    ***
    **
    *
"""
row =5
for i in range(row, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

##  Q3.Wap to print Up left triangle with '*'
"""O/P:
        *
       **
      ***
     ****
    ***** 
"""
row=5
for i in range(1,row+1):
    for j in range(row-i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()


##  Q4.Wap to print Down left triangle with '*'
"""O/P:
*****
 ****
  ***
   **
    * 
"""
row=5
for i in range(row):
    for j in range(i):
        print(" ", end="")
    for  k in range (row -i):
        print ("*", end="")
    print()

## Q5. WAP to print multiplication table of a given number using for loop.
num=9
for i in range(1, 11):
    print(f"{num} X {i} = {num*i}")

## Q6. WAP to greet all the person names stored in a list ‘l’ and which starts with S.
nameList = ["Harry", "Soham", "Sachin", "Rahul"]
for name in nameList:
    if name.startswith("S"):
        print("Hello",name, "!")

## Q7. WAP to find whether a given number is even or odd.
num=(56, 97, 564, 12)
for i in num:
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")


## Q8.WAP to find the sum of first n natural numbers using while loop
num=5
sum=0
i=1
while i <= num:
    sum=sum+i
    i=i+1
print(sum)

## Q9. WAP to calculate the factorial
num=5
fact=1
for i in range(1,num+1):
    fact*=i
print(fact)


## Q10. WAP to print for row=4
'''
    *
   ***
  *****
*********
'''
row =4
for i in range(1, row+1):
    for j in range(row -i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print()
