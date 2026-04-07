# import array 
# import array as arr #aliasing
from array import *

# val = arr.array('i', [1,2,3,4,5,6])
val = array('i', [1,2,3,4,5,6,7,8,9])
# val = array('i', [1,2,3,4,5,6,7,8,9.5])  #error  
# val = array('d', [1,2,3,4,5,6,7,8,9.5])
# val = array('u', ['a','b','c','d'])
# print(val)

#to know the type code
print(val.typecode)

for i in range(0,6):
    # print(val[i])
    print(val[i], end = " ")

print('\n')

for i in range(0,len(val)):
    # print(val[i])
    print(val[i], end = "-")

print('\n')

for x in val:
    # print(val[i])
    print(x, end = ",")


# reverse array method

val.reverse()
for i in range(0,len(val)):
    # print(val[i])
    print(val[i], end = "-")


#Insertion
val.insert(1,50)
val.append(100)   #add in last
val[2] = 200      #overwrite

print('\n')

#Copying array
copyarray = array (val.typecode,(x*2 for x in val))

for i in range (0, len(copyarray)):
    print(copyarray[i], end= " ")

#Deletion

copyarray.pop(3)
copyarray.pop()
copyarray.remove(12)


#slicing

a = val [2:6]
a = val [2:-3]
a = val [::-1] #reverse an array

#Searching
arr = array ('i', [0,1,2,3,4,5,6])
i = arr.index(4)
print(i)

#input from user

arr = array ('i',[])

n = int(input('Enter how many element you want to insert : '))

for i in range(0,n):
    arr.append(int(input("Enter element : ")))

for x in arr:
    print(x,end=" ")