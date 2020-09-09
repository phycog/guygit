'''
BASIC OPERATIONS

Traverse − print all the array elements one by one.

Insertion − Adds an element at the given index.

Deletion − Deletes an element at the given index.

Search − Searches an element using the given index or by the value.

Update − Updates an element at the given index.

'''
from array import *

array1 = array('i', [10,20,30,40,50])

array1.insert(1,60)

for x in array1:
 print(x)

