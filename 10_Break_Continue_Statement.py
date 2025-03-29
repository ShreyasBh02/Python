## Break Statement: Python break statement is used to terminate the current loop and resumes execution at the next statement

## Break statement with For Loop
for letter in "Python":
    if letter == "t":
        break
    print("current letter: ", letter)
    


## Break statement with While loop
var=10
while var>0 :
    print( "current no is: ", var)
    var =var-1
    if var ==5:
        break
print("Good Bye!")
 
## Continue Statement: Python continue keyword is used to skip the remaining statements of the current loop and go to the next iteration.
for i in range(0,5):
    if i== 3:
        print("I'm with continue statement", i)
        continue
    print(i)