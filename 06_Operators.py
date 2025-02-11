## Operators
##***************************************************************************************************
## a. Arithmetic
    # a =5+4          #Addition
    # b=9-4           #Sub
    # c=6*7           #Mul
    # d=9/7           #Div
    # e=5%9           #Mod
    # f=9**3          #Cube
    # g= 5//3         #Floor(Nearst Value)
    # print("The add: ",a)
    # print("The sub: ",b)
    # print("The mul: ",c)
    # print("The div: ",d)
    # print("The mod: ",e)
    # print("The expo: ",f)
    # print("The floor: ",g)

##***************************************************************************************************
## B. Comparison
    # a = 46    # Initializing the value of a    
    # b = 4     # Initializing the value of b    
    
    # print("For a =", a, "and b =", b,"\nCheck the following:") 
    # print('1. Two numbers are equal or not:', a == b)    
    # print('2. Two numbers are not equal or not:', a != b)    
    # print('3. a is less than or equal to b:', a <= b)    
    # print('4. a is greater than or equal to b:', a >= b)    
    # print('5. a is greater b:', a > b)    
    # print('6. a is less than b:', a < b)
##***************************************************************************************************
## C. Logical
    # a = 5
    # print(a > 3 and a < 10)
    # print(a > 3 or a < 4)
    # print(not (a > 3 and a < 10))
##***************************************************************************************************
## D. Assignment
    # a = 21
    # b = 10
    # c = 0
    # print ("a: {} b: {} c : {}".format(a,b,c))
    # c = a + b
    # print ("a: {}  c = a + b: {}".format(a,c))

    # c += a
    # print ("a: {} c += a: {}".format(a,c))

    # c *= a
    # print ("a: {} c *= a: {}".format(a,c))

    # c /= a 
    # print ("a: {} c /= a : {}".format(a,c))

    # c  = 2
    # print ("a: {} b: {} c : {}".format(a,b,c))
    # c %= a
    # print ("a: {} c %= a: {}".format(a,c))

    # c **= a
    # print ("a: {} c **= a: {}".format(a,c))

    # c //= a
    # print ("a: {} c //= a: {}".format(a,c))

##***************************************************************************************************
## E. Membership
    # myList = [12, 22, 28, 35, 42, 49, 54, 65, 92, 103, 245, 874]  
    # x = 31  
    # y = 28  
    
    # print("Given List:", myList)  
    # if (x not in myList):  
    #     print("x =", x,"is NOT present in the given list.")  
    # else:  
    #     print("x =", x,"is present in the given list.")  
    # if (y in myList):  
    #     print("y =", y,"is present in the given list.")  
    # else:  
    #     print("y =", y,"is NOT present in the given list.") 

##***************************************************************************************************
## F. Identity
    # a = [1, 2, 3, 4, 5]
    # b = [1, 2, 3, 4, 5]
    # c = a

    # print(a is c)
    # print(a is b)

    # print(a is not c)
    # print(a is not b)
##***************************************************************************************************
## G. bitwise
a = 2            
b = 1            
print ('a=',a,':',bin(a),'b=',b,':',bin(b))
c = 0
c = a & b;        
print ("result of AND is ", c,':',bin(c))

c = a | b;     
print ("result of OR is ", c,':',bin(c))

c = a ^ b;        
print ("result of EXOR is ", c,':',bin(c))

c = ~a;           
print ("result of COMPLEMENT is ", c,':',bin(c))

c = a << 2;       
print ("result of LEFT SHIFT is ", c,':',bin(c))

c = a >> 2;       
print ("result of RIGHT SHIFT is ", c,':',bin(c))