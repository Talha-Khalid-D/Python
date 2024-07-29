# Lists


# What are lists?
# lists Vs Arrays
# Characteristics of a list
# How to create a list
# Access items from a list
# Editing items in a list
# Deleting items from a list
# Operations on lists
# Functions on lists


# What are lists

# list is a data type where you can store multiple items under 1 name. More technically , lists act like dynamic arrays which means you can add more items on the fly.
# L = [ 2 , 'jessa', 35.75 , [20,45,56] ] Why lists are required in programming?


# Lists Vs Arrays

# dynamic size vs fixed
# convenience -> heterogeneous
# speed of execution
# memory


a = 2
print ( id (2))


L = [1,2,3]

print(id(L))
print(id(L[0]))
print(id(L[1]))
print(id(L[2]))
print(id(1))
print(id(2))
print(id(3))


# How lists are stored in memory

# by referential array
# item reference \ pointer


# Characteristics of a list

# Ordered
# Changeble/Mutable
# Heterogeneous
# can have duplicates
# are dynamic
# can be nested
# items can be accessed
# can contain any kind of objects in python


L = [1,2,3]
L1 = [3,2,1]

L == L1


#lists of python can be changed


#python lists can be nested
l = [2,3,[3.4,4]]
print (l)


# Creating a List

#Empty
print([])
#1D
print([2,3,4,5])
#2D
print([2,3,4,[4,5]])
#3D
print([[[3,2],[1,2]],[[4,5],[3,4]]])
#heterogeneous
print ([1,3.4,2.3j,'hello'])
#Using Type conversion
print(list('talha'))


# Accessing items from a list

#Indexing
l = [2,3,4]
print (l[0])


#Positive Indexing
l = [2,3,5]
print(l[0])

#Negative Indexing
l = [2,3,4]
print(l[-1])

#Indexing for 2D list
l = [1,3,4,[3,4]]

#positive Indexing
print (l[3][0])

#Negative Indexing
print (l[-1][-1])

#Indexing for 3D list
l = [[[2,3],[4,5]],[[5,6],[2,3]]]

#Positive Indexing
print (l[0][1][0])

#Negative Indexing
print (l[-1][-2][-1])

#Slicing
l = [2,3,4,5,6,1]
print (l[0:3])

l = [2,4,5,6,7,7,8,9]
print (l[-4:-1])
print(l[-3:])

l = [2,4,5,6,7,7,8,9]
print(l[0:5:2])

l = [2,4,5,6,7,7,8,9]
print (l[0::2])
print(l[0:5:1])

l = [2,4,5,6,7,7,8,9]
print (l[-5:-2:2])

l = [2,4,5,6,7,7,8,9]
#to reverse a list
print (l[::-1])


# Adding items to a list

#Append will add a single item at the end of the list
l = [2,4,5,6,7,7,8,9]
l.append(3)
print (l)

#we can also add a list as an item in list by append func.
l = [2,4,5,6,7,7,8,9]
l.append([2,3,4])
print(l)

#extend can add more than one item at the last of the list
l = [2,4,5,6,7,7,8,9]
l.extend([3,4,5])
print(l)

#Extend will try to add multiple items while append will try to add a single item in a list
l = [2,3,4,5]
l.extend('talha')
print (l)

#Insert can be used to add item in a list at our desired position
l = [3,4,5,6,7]
l.insert(3,1)
print(l)

l = [3,4,5,6,7]
l.insert(0,1)
print(l)


# Editing items in a list

#Lists are mutable so we can edit lists

l = [3,4,5,6]
#Editing with indexing
l [-1] = 600

#Editing with slicing
l [1:3] = [400,500]

print(l)


# Deleting items from a list

#del
l = [2,3,4,5]
print (l)
#complete list deletion
#del l

#indexing deletion of item
del l [-1]

#Slicing deletion of item
del l [1:2]
print(l)


#remove
l = [2,3,4,5]
l.remove(5)
print (l)

#pop can delete a particular item at particular position by providing index
l = [2,3,4,5]
l.pop(0)
print(l)

#pop can be used to delete the last item by not giving index number
l = [2,3,4,5]
l.pop()
print (l)

#Clear can be used to clear all the items of a list
l = [2,3,4]
l.clear()
print(l)


# Operations On lists

# Arithmetic
# loops
# Membership


#Arithmetic (Addition,Multiplication)

#Concatenation / Merge
l = [2,3,4]
L = [1]
print (l + L)

#Multiplication
l = [2,3,4]
print(l*3)

#Membership
l = [2,3,4,5]
L = [1,2,3,4,[5,6]]
print(3 not in l)
print(5 in L)

#loops
l = [3,4,5,6,7]
L = [1,2,5,[6,7]]
for i in L:
  print(i)

l = [[[2,3],[4,5]],[[3,4],[5,6]]]
for i in l:
  print(i)


# List Functions  

#len/min/max/sorted
l = [2,3,4,5]
print (len(l))
print(min(l))
print(max(l))
#for desending order sorting
print(sorted(l,reverse=True))
#for ascending order sorting
print(sorted(l))

#count
l = [2,3,4,5,3,4,2,5,6]
l.count(3)
l.count(6)

#index
l = [2,3,5,4,6,2]
l.index(5)
#when item is present multiple times it will give its first occurence like l.index (2) will give 0 in answer
#l.index(7) gives error when item is not present in the list

#reverse
l = [2,3,4,5,6,7]
#the reverse function will permenantly change the list
l.reverse()
print (l)

#sort (vs sorted)
#sort also permanently change the list
l = [2,3,4,5,0]
print (l)
print(sorted(l))
print(l)
l.sort()
print(l)

#copy --> shallow copy means in memory at the new address the same copy is created
l = [2,3,4,5]
print(id(l))
L = l.copy()
print(L)
print (id(L))


# List Comprehension

# list comprehension provides a concise way of creating lists

# newlist = [expression for item in iterable if condition == True]

# Advantages of list comprehension

# more time-efficient and space efficient than loops
# require fewer lines of codes
# transforms iterative statement into formula


#add 1 to 10 number to a list
l = []
for i in range(1,11):
  l.append(i)
print(l)

#by list comprehension
l =[i for i in range (1,11)]
print (l)

#scalar multiplication on a vector
s = [2,3,4]
v = -3
x=[]
for i in s:
  x.append(i*v)
print (x)

#by list comprehension
s = [2,3,4]
v = -3
l = [v*i for i in s]
print (l)

#add squares
l =[1,2,3,4,5]
l = [n*n for n in l]
print (l)

#print all numbersin the range 1 to 50 which are divisible by 5
l = [n for n in range(1,50) if n%5 == 0]
print(l)

#find languages which starts with letter p
languages = ['java','python','javascript','php','html']
language = [lan for lan in languages if lan.startswith('p')]
print(language)

#cartessian products -> list comprehension on two lists
la = [2,3,4]
ls = [1,2,3,4]
l =[i*j for i in la for j in ls]
print(l)

#Two Ways to traverse a list
#Item wise
l = [1,3,4]
for i in l:
  print (i)

#Indexwise
l=[2,3,4,5]
for i in range (0,len(l)):
  print(i)

#Indexwise
l=[2,3,4,5]
for i in range (0,len(l)):
  print(l[i])


# Zip

# The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together.

# If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.

l =[1,2,3,4]
la =[-1,-2,-3,-4]
list(zip(l,la))

#print(ls)

ld=[i+j for i,j in zip (l,la)]
print(ld)


# Disadvantages of python lists

# Slow
# Risky usage
# eats up more memory


#python lists are so fexible that we can store objects in lists even builtin functions can be stored
#like
l = [1,2,print,type,input]
print(l)

#risky usage example of python
a = [1,2,3,4]
b =a
a.append(5)
print(b)

a = [1,2,3,4]
b =a.copy()
a.append(5)
print(b)