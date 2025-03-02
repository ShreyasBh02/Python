## Condition Control: I will play cicket when the weather is sunny.
## Loop: I will keep checking out Dishe untill all the dishes are over in a buffet.
## Break: I will check out all the dishes untill I  get sweets

##Conditional Statement:Helps to code decision based on some Pre-condions
##If statement

validAge=19
if validAge>18:print("Eligiable for Driving License.")
invalidAge=10
if invalidAge>18:print("Not Eligiable for Driving License.")

number=42
if (number%2)==0:
    print("Number is Even")

##If else statement
#If yor'r age is less than 12, then you can travel free
childAge=28
if(childAge<=12):
    print("You can travel Free")
else:
    print("You need to pay")

#If student's marks is greater than 10 he is "Pass" otherwise he is "Fail"
studentMarks=10
if(studentMarks>=10):
    print("Pass!")
else:
    print("Fail!!!")


##elif statement
marks=65
if(marks>=90):
    print("Grade A")
elif(80<=marks<89):
    print("Grade B")
elif(70<=marks<79):
    print("Grade C")
elif(50<=marks<69):
    print("Grade D")
elif(30<=marks<49):
    print("Grade E")
else:
    print("Grade F")
    

age=26
if (age<=12):
    print("You are Child")
elif(age<=19):
    print("You are Tenager")
else:
    print("You are Adult")

num=9800
if(num<=10):
    print("Number is less than 10")
elif(num<=100):
    print("Number is less than 100")
elif(num<=1000):
    print("Number is less than 1000")
else:
    print("Number is gretaer than 1000")

##Nested If Statement

x=10
y=20
if(x>5):
    if(y>5):
        print("Both x and y greater than 5")
    else:
        print("X is greater than 5 but Y is less than 5")
else:
    print("Both x is less than 5")
