'''
    Static:
        Doesnot modify class or instace state
        Dosnot access instance or class tstae
        Doesnt deped on class/instance
        It behaves like a plain funntion that belonings to class
        @Status method is used
'''
class MathOperator:
    @staticmethod
    def add(x , y):
        return x + y
    
    @staticmethod
    def sub(x , y):
        return x - y

result_Add= MathOperator.add(5 , 3)
result_Multiply= MathOperator.add(5 , 3)

print(f"Addition: ", result_Add)
print(f"Multiply: ", result_Multiply)