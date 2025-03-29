'''
Set:
    A Python set is the collection of the unordered items. 
    Each element in the set must be unique, immutable, and the sets remove the duplicate elements. 
    Sets are mutable which means we can modify it after its creation.
'''

## Create a Set
## using {}
Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}    
print(Days)                                                                               
## O/p: {'Wednesday', 'Thursday', 'Friday', 'Sunday', 'Saturday', 'Tuesday', 'Monday'}

## using set() method
set1=set([1,2,3, "Python", 20.5, 14])
print(set1, "\n",type(set1))
for set in set1:
    print(set)
## O/p: 
# {1, 2, 3, 14, 'Python', 20.5} 
#  <class 'set'>
# 1
# 2
# 3
# 14
# Python
# 20.5
## 

## set is Unique: duplicates will be automatically removed 
bucketList= {"Laptop","iPhone","iPhone","Car","iPhone","House","Laptop"}
print(bucketList)                                                                           
## O/p: {'House', 'Car', 'iPhone', 'Laptop'}

##***************************************************************************************************
## Updating Set
## 1. Using add() methods:
add={1,9,3,4,0}
add.add(5.64)
print(add)                                                                                  ## O/p: {0, 1, 3, 4, 5.64, 9}

## 2. Using update() methods:
setUpdate={1,9,3,4,0}
setUpdate.update([64])
print(setUpdate)                                                                            ## O/p: {0, 1, 64, 3, 4, 9}

##***************************************************************************************************
## Accessing Elements: Set Dont have index i.e. we cant do slicing
eleSet={90,4,6,9,40} 

for i in eleSet:
    print(i)
'''O/p:
6
40
9
90
'''
print(eleSet[3])
'''
    Traceback (most recent call last):
    File "d:\Rest Assured_ATT\Python\Programs\DataStructure\tempCodeRunnerFile.py", line 3, in <module>
        print(eleSet[3])
            ~~~~~~^^^
    TypeError: 'set' object is not subscriptable
'''


##***************************************************************************************************
## Remove Elements

## Using remove() Method: remove() method removes a specified element from the set. 
#                         If the element is not present in the set, it raises a KeyError
months={"January","February", "March", "April", "May", "June"}
months.remove("May")
print(months)                                                                               ## O/p: {'February', 'March', 'April', 'June', 'January'}
months.remove("Sept")
print(months)                     
''' O/p
Traceback (most recent call last):
  File "d:\Rest Assured_ATT\Python\Programs\DataStructure\tempCodeRunnerFile.py", line 4, in <module>
    months.remove("Sept")
KeyError: 'Sept'
'''


## Using discard() Method:  discard() method also removes a specified element from the set. 
#                          Unlike remove(), if the element is not found, it does not raise an error.
months={"Jully","February", "March", "April", "May", "June"}
months.discard("Jully")
print(months)                                                                               ## O/p: {'May', 'February', 'June', 'April', 'March'}
months.discard("Nov")
print(months)                                                                               ## O/p: {'May', 'February', 'June', 'April', 'March'}



## Using pop() Method :removes and returns an any random element from the set. 
Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}   
Days.pop() 
print(Days)                                                                        
'''O/p:
Iteration 1: {'Monday', 'Friday', 'Wednesday', 'Thursday', 'Saturday', 'Sunday'}
Iteration 2: {'Sunday', 'Tuesday', 'Saturday', 'Friday', 'Thursday', 'Wednesday'}
'''
## Using clear() Method: removes all elements from the set, leaving it empty.
set1 = {1, 2, 3, 4, 5}
set1.clear()
print(set1)  

##***************************************************************************************************
##  Set Operations

## 1. Union: It combine elements from both sets using the union() function or the | operator.
## Using union() methods:
sisBucketList={"Nailpaint","Tshirts","Makeup","Jeans","Lahenga"}
broBucketList={"Games","Fun","Tshirts","Jeans"}
print(sisBucketList.union(broBucketList))                                                                            
 ##O/p: {'Makeup', 'Jeans', 'Tshirts', 'Nailpaint', 'Fun', 'Lahenga', 'Games'}

## using union | operator
sisBucketList={"Nailpaint","Tshirts","Makeup","Jeans","Lahenga"}
broBucketList={"Games","Fun","Tshirts","Jeans"}
print(sisBucketList| broBucketList)                                                                                   
##O/p: {'Lahenga', 'Makeup', 'Jeans', 'Tshirts', 'Fun', 'Games', 'Nailpaint'}


## 2. Intersection − It is used to get common elements using the intersection() function or the & operator.
##  Using & operator
sisBucketList={"Nailpaint","Tshirts","Makeup","Jeans","Lahenga"}
broBucketList={"Games","Fun","Tshirts","Jeans"}
print(sisBucketList & broBucketList)                                                                                   
##O/p: {'Jeans', 'Tshirts'}

##  Using intersection() method
sisBucketList={"Nailpaint","Tshirts","Makeup","Jeans","Lahenga"}
broBucketList={"Games","Fun","Tshirts","Jeans"}
print(sisBucketList.intersection(broBucketList))                                                                       
##O/p: {'Jeans', 'Tshirts'}

## 3. Difference − It is used to get elements that are in one set but not the other using the difference() function or the - operator.
## Using subtraction ( - ) operator
sisBucketList={"Nailpaint","Tshirts","Makeup","Jeans","Lahenga"}
broBucketList={"Games","Fun","Tshirts","Jeans"}
print(sisBucketList - broBucketList)                                                                                   
##O/p: {'Lahenga', 'Nailpaint', 'Makeup'}

##  Using difference() method
sisBucketList={"Nailpaint","Tshirts","Makeup","Jeans","Lahenga"}
broBucketList={"Games","Fun","Tshirts","Jeans"}
print(sisBucketList.difference(broBucketList))                                                                          
##O/p: {'Lahenga', 'Nailpaint', 'Makeup'}
  
## 4. Symmetric Difference − It is used to get elements that are in either of the sets but not in both using the symmetric_difference() method or the ^ operator.
## Using ^ operator
sisBucketList={"Nailpaint","Tshirts","Makeup","Jeans","Lahenga"}
broBucketList={"Games","Fun","Tshirts","Jeans"}
print(sisBucketList^ broBucketList)                                                                                   
##O/p: {'Fun', 'Games', 'Makeup', 'Nailpaint', 'Lahenga'}

##  Using  symmetric_difference() method
sisBucketList={"Nailpaint","Tshirts","Makeup","Jeans","Lahenga"}
broBucketList={"Games","Fun","Tshirts","Jeans"}
print(sisBucketList.symmetric_difference(broBucketList))                                                              
##O/p: {'Fun', 'Games', 'Makeup', 'Nailpaint', 'Lahenga'}
 



