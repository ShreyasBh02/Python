#TypeCasting
#Implicit Casting
a=5
b=9.4
print("The type of no are: a: ",type(a), " b: ", type(b))
result =a+b
print("The result of casting is: ", result)
print("The type of result is: ",type(result))
print("")
#***************************************************************************************************
# Explicit Casting
a= "10"
b= 6
print("Before Casting: The type of no are: a: ",type(a), " b: ", type(b))
a=int(a)
print("After Casting: The type of no are: a: ",type(a), " b: ", type(b))
result =a+b
print("The result of casting is: ", result)
print("The type of result is: ",type(result))
print("")
#Data Loss in Explicit Casting
x=4.56
print("Before Casting:" ) 
print("The type of no is: x: ",type(x), " And value of x is: ",x)
a=int(x)
print("After Casting: ")
print("")
#***************************************************************************************************
# Functions
#A. int() function
a= 5            #int 
b =5.64         #float
c="45"          #string
d=True          #bool
print("Casting using int func: ",int(a), type(a))
print("Casting using int func: ",int(b), type(b))
print("Casting using int func: ",int(c), type(c))
print("Casting using int func: ",int(d), type(d))
print("")

#***************************************************************************************************
#B. float() function
w=5.61                  #float
x=6                     #int
y="97.01"               #str
z=False                 #bool 
print("Casting using float func: ",float(w), type(w))
print("Casting using float func: ",float(x), type(x))
print("Casting using float func: ",float(y), type(y))
print("Casting using float func: ",float(z), type(z))
print("")

#***************************************************************************************************
# C. str() function
p=5.61                  #float
q=6                     #int
r="97.01"               #str
s=False                 #bool 

print("Casting using str() function: ", str(p), "Type:", type(str(p)))
print("Casting using str() function: ", str(q), "Type:", type(str(q)))
print("Casting using str() function: ", str(r), "Type:", type(str(r)))
print("Casting using str() function: ", str(s), "Type:", type(str(s)))
print("")