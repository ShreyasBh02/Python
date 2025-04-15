''''
Exception Handling 
    Handles errors that occur during the execution of a program. 
    Exception handling allows to respond to the error, instead of crashing the running program.

'''

## Exeption Handling Ex
n =10
print( n/0) 
'''
O/p:
    ZeroDivisionError: division by zero
'''
## try, except, else and finally Blocks
try:
    n = 0
    res =100/ n
except ZeroDivisionError:
    print(" You cant divide by 0")
except ValueError:
    print("Enter the valid number")
else:
    print("Result is: ", res)
finally:
    print("Execution completed")

## EX:1 Bank/ ATM Withdrawal System

class InsufficientFundsError(Exception):
    """ Custom exception for the Insufficient Balance."""
    pass

def withdraw_money(balance, amount):
    try:
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number.")

        if amount <= 0:
            raise ValueError("Amount must ne greater than zero.")

        if amount > balance:
            raise InsufficientFundsError("You dont have enough balance.")
        
        balance = balance -amount
        print(f"{amount} withfrawl Sucessful! Remaining balance: {balance:.2f}")
    
    except ValueError as ve:
        print (f"Input Error:  {ve}")

    except InsufficientFundsError as isf:
        print (f"Balance Error:  {isf}")
    
    else: 
        print("Transaction completed successfully.")
    
    finally:
        print("Thank You for using ATM.\n")
    
    return balance


balance = 500.0
withdrawals = [100, 50, -20, 600, "abc", 200]

for amount in withdrawals:
    print(f"Current balance: ${balance:.2f}")
    print(f"Attempting to withdraw: {amount}")
    balance = withdraw_money(balance, amount)

print("Goodbye!")

