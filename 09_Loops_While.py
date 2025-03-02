##Loops:Loops in Python are used to repeat actions efficiently. The main types are For loops (counting through items) and While loops (based on conditions). 
##Life is Loop

##While loop
counter=0
while counter <6:
    counter+=1
    print("Iteration no", format(counter))
print("End of While Loop")

##WAP toprint no between 1 to 20
num=1
while num<=20:
    print(format(num))
    num+=1

#Wap to print the content of a list using while loops
numList=([5,9,3,0])
index=0
while (index<len(numList)):
    print(numList[index])
    index+=1

##While else loop   
counter=1
while counter <6:
    print("Iteration no", format(counter))
    counter+=1
else:
    print("From else Block")
print("End of While Loop")


##While break loop 
var = 10                   
while var > 0:              
   print ('Current variable value :', var)
   var = var -1
   if var == 5:
      break

print ("Good bye!")

##While contiinue loop 
num = 60
print ("Prime factors for: ", num)
d=2
while num > 1:
   if num%d==0:
      print (d)
      num=num/d
      continue
   d=d+1