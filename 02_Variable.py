## Variable
    # a= 20
    # print(a)
    # print(type(a))
    # print(id(a))

    # b= 5.64
    # print(b)
    # print(type(b))
    # print(id(b))

    # c="Shreyas"
    # print(c)
    # print(type(c))
    # print(id(c))

    # d= False
    # print(d)
    # print(type(d))

##local Variable
    # def add():
    #     a=20;
    #     b=2;
    #     c=a+b;
    #     print(c);

    # add()
    # print(a)

##Global Variable
x=99
def mainFunction():
    global x
    print(x)

mainFunction() 
print(x)
