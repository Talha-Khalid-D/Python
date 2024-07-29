# Strings are sequence of characters

# In python specifically, strings are a sequence of unicode characters

# creating strings
# accessing strings
# adding strings
# editing strings
# deleting strings
# operations on strings
# string functions


#how to create strings
s = 'strings'
s = "strings"
#multiline strings
s = ''' strings '''
print (s)
#strings are also used in type conversion
s = str ('strings')
print (s)


# Indexing

#Accessing sub-strings from a string
#Positive Indexing
s  = 'hello world'
print (s[6])
#negative indexing
s = 'hello world'
print (s[-2])

# Slicing , Deleting and Editing Strings

#Slicing
s = 'hello world'
print (s[0:5])

s = 'hello world'
print (s [3:])

s = 'hello world'
print (s [:3])

s = 'hello world'
print (s [6:0:-2])

#Reverse a given string
print(s[::-1])

s = 'hello world'
print(s[-5:])

s = 'hello world'
print (s[-1:-6:-1])

#Edit and delete in strings

s = 'hello world '
s[0] = 'H'

#python strings cannot be changed ie they are immutable

#how to delete a string
s = 'hello world'
del s
print (s)

#the reason for this is that the string is immutable(cannot be changed)
s = 'hello world'
del s[-1:-5:2]
print (s)


# Operations on strings

# arthmetic operations
# Relational operations
# logical operations
# loops on strings
# membership operations

# Arithmetic operations

#addition operation
print ('tal' + 'ha')
print ('lahore' + 'karachi')

#multiplication operation

print ('talha \n' * 5)

print ('*'*39)

#Relational operations

#we compare strings by ascii value means the alphabet which comes later is greater (lexiographically comparison)
#'talha' == 'khalid'

'talha' > 'khalid'

#'talha' != 'talha'

# logical operation

'hello ' and 'world'

#Or gives true when any of them  is true
'hello' or 'world'

#And gives true when both are true
'' and 'world'

#not gives opposites means true into false and false into true
#empty string means false
not ''

for i in 'hello':
  print ( i)

for i in 'delhi':
  print ('pune')

# loops can be used in strings

for i in 'talha':
  print (i)

#Membership operators
#they are case sensitive
'D' not in 'Delhi'

'T' in 'Talha'


# Functions in Python

# Common functions

len ('hello world')

max ('hello world')

min ('hello world')

sorted ('hello world')


# Capitalize/Title/Upper/Lower/Swapcase

s = 'hello world'
s.capitalize()

s = 'hello world'
s.title()

s = 'hello world'
s.upper()

s = 'hello world'
s.lower()

s = 'Hello World'
s.swapcase()


# Count/Find/Index

'my name is talha'.count ('i')

'my name is talha'.find ('a')

#index function is same as find but it gives error when the letter is not present
'my name is talha'.index('c')


# Ends With/Starts With

'my name is talha'.endswith('a')

'my name is talha'.startswith('t')


# Format

name = 'talha'
gender = 'male'
'Hi my name is {} and I am a {}'.format(name,gender)

#Order matters in format function

name = 'talha'
gender = 'male'
'Hi my name is {1} and I am a {0}'.format(name,gender)


# isalnum/isalpha/isdigit/isidentifier

'talha234'.isalnum()

'talha1'.isalpha()

'234'.isdigit()

'3name'.isidentifier()

'_name'.isidentifier()


# split/join

'hi my name is talha'.split()

'hi my name is talha'.split ('is')

"-".join(['hi', 'my', 'name', 'is', 'talha'])


# Replace

'hi my name is talha'.replace('talha','talha khalid')

# strip

'talha                              '.strip()

#strip can be used in data saving when there is extra spaces in data given by user