# Tuples

# A tuple in Python is similar to a list. The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list.

# In short, a tuple is an immutable list. A tuple can not be changed in any way once it is created.

# Characterstics

# Ordered
# Unchangeble
# Allows duplicate
# Plan of attack
# Creating a Tuple
# Accessing items
# Editing items
# Adding items
# Deleting items
# Operations on Tuples
# Tuple Functions


# Creating Tuples

#empty tuple
t = ()
print ( t)

#single item tuple
t = (1,)
print(t)

#tuple homogeneous
t = (2,3,4)
print(t)

#tuple heterogeneous
t = (2,'hello',True)
print(t)

#tuple within a tuple
t = (2,3,4,(4,5))
print(t)

#3D tuple
t =(((3,4,5),(3,4,5)),((3,4,5),(3,4,5)))
print(t)

#type conversion creation of tuple
t = tuple('hello')
print(t)


# Accessing Items

# Indexing
# Slicing

t = (2,3,4,5)
print(t)
print(t[0])

#Index accessing of tuple is same as list and strings

#slicing means fetching multiple items at the same time
t = (2,3,4,5)
print(t[0:4])

t = (2,3,4,5)
print (t[0:2])

t = (2,3,4,5)
print (t[::-1])

t = (2,3,4,(4,5))
print(t[-1][0])

#slicing is also same as in lists and strings

#Editing a tupple
#tupple cannot be eddited as it is not mutable
t = (2,3,4,(4,5))
t[0]=100
print (t[0])

#adding items to a tupple is not possible as it is immutable

#deleting items
# we can del a complete tupple but we can not delete a portion of it

# Opperations On tupples

#addition and multiplication
t = (2,3,4)
ta = (2,3,4,5)
print (t + ta)

print (t*4)
#membership
print(5 in ta)
#Iteration
for i in t:
  print(i)


# Tupple Functions

# len/max/min/sum/sorted
ta = (6,2,3,4,5)
print (len(ta))
print(min(ta))
print(sum(ta))
print(max(ta))
print(sorted(ta))
print(sorted(ta,reverse=True))

#count
ta = (2,3,4,5)
ta.count(5)

ta = (2,3,4,5)
ta.index(4)

#index function of tupple is same as of list