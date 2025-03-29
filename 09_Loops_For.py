##Loops:Loops in Python are used to repeat actions efficiently. The main types are For loops (counting through items) and While loops (based on conditions). 
##Life is Loop

##For loop: provides the ability to loop over the items of any sequence

##For Loop 
numbers = (34,54,67,21,7)
total = 0
for num in numbers:
   total += num
print ("Total =", total)


elementList=('a', "Python", 35,True, 0,-9)
for i in elementList:
   print(i)


##For loop with List, Tuple, String and Dictionary
nameList= ["Ronaldo", "Messi", "Mabape", "Ramos"]
for name in nameList:
   print(name)
print()

nameTuple=("Dhoni","Pointing","Sachin","Breet Lee","Dravid")
for name in nameTuple:
   print(name)
print()

nameString="Cristiano Ronaldo"
for name in nameString:
   print(name)
print()

nameDict=dict ({'a':0,'b':945, 'c':46})
for name in nameDict:
   print(name,    nameDict[name])
print()


##For loop with else
nameList= ["Ronaldo", "Messi", "Mabape", "Ramos"]
for name in nameList:
   print(name)
else:
   print("Inside the else Block")
print()
















##Q1. WAP to print namne without Owels
name="John Doe"
for char in name:
   if char not in 'aeiou':
      print(char, end='')
   

##For loop with Range
##range(stop)
for i in range(10):
   print(i, end=' ')
print()

##range(start, stop)
for i in range(3,10):
   print(i, end=' ')
print()

##range(start, stop, step)
for i in range(1,10,3):
   print(i, end=' ')
print()