# Output In Python 

print('Hello World')
print(5)
print(5.6)
print(5555)
print(5 + 6)
print (True)

# Short-hand for output 

print('salman khan',4,4.5,True)
print('salman khan',4,4.5,True,sep=':')
print('hello')
print ('world')

# To finish the ending next line in print line 

print('hello',end='-')
print ('world')

# Data Types

#integer
print(3)
#Decimal
print(3.4)
#boolean
print(True)
#text\string
print('hello')
#complex
print(5+6j)
#list\array
print([2,3,4])
#tuple
print((1,2,3,4))
#sets
print(({2,3,4,5,6}))
#Dictionary
print({'name':'talha','gender':'male','weight':'50'})
#type
type(4)

# Variables

#static vs dynamic typing
#static vs dynamic binding
#stylish declaration techniques

#In python we don't need to declare variables in start indeed we can create them when we need them
name = 'talha'
print (name)
#another example of variable
a = 4
b = 6
print (a + b)
#dynamic typing is where we don't tell the data type
a = 4
#static typing we need to declare the data-type like in c , c++ , java
#int a = 4
#dynamic binding no fixed data type
a = 5
a = 'talha'
print (a)
#static binding fixed data type
#int a


# Variables creation Commennts

#we use '#' to write comment in code comment is not displayed in output it is for future understanding of code
a = 1
b  = 2
c = 3
print ( a , b , c)

# method of creation more than one 

a,b,c = 1,3,4
print (a , b , c)

# method of assigning value to more than one 
a=b=c=5
print (a , b , c)

# Keywords & Identifiers

#keywords are those words which are fixed means we should not use these words to create variables\functions etc
#there are almost 32 keywords in python interpreters\compliers may give error when we use these words for other than there specified use
#as a programmer we should not use the keywords bcz due to this interpreter may face problem to convert high level code  to low level code

#indentifier we name the variables\funtions\class all of these are identifiers
#there are two specific rules to write identifiers:-
#we can't start with a digit like 2name etc
#we can use special characters _ like first_name etc
#identifiers can not be keywords

# User Input

#static vs dynamic software \\static software means no input \\dynamic software means input from user
input ( 'name ' )

#take input from the users and store them in a variable
first_num = input ('first_num ')
second_num = input ('second_num ')
#add the 2 variables
v = first_num + second_num
#print the result
print ( v )

first_num = input ('first_num ')
second_num = input ('second_num ')
v = int(first_num) + int (second_num)
print (v)
first_num = int (input ('first_num '))
second_num =int ( input ('second_num '))
c = first_num + second_num
print (c)

# Type Convertion

#implicit vs explicit
#implicit in which interpreter automatically understand the type convertion
print (3 + 5.5)
#explicit in which we manually convert type
#str --> int and vice versa
int ('4')
#float --> int and  vice versa
int (3.4)
#complex is not converted

# Literals

#the values given to the variables is literal like in a = 3 , 3 is a literal
a =0b1010 #binary literals
b =100 #decimal literals
c =0o310 #octal literals
d =0x12c #hexadecimal literals

#float literals
e = 3.3
g = 1.5e2
f = 1.5e-4

#complex literals
h = 5.14j

print (a,b,c,d,e,f,g,h,h.imag,h.real)

# All methods of outputing string

string = 'Talha '
strings = " Talha "
char = ' c '
multiline_str = """ this is a multiline string with more than one line code """
unicode = u"\U0001f680\U0001F606\U0001F923"
raw_str = r"raw \n string "
print (string )
print (strings )
print (char )
print (multiline_str)
print (unicode)
print (raw_str)

# Use of boolean with other operators

a = True + 2
b = False + 5
print ( " a: " , a )
print ( " b : " , b )

# None value to some variable 

b = 4
a = None
print ( b )
#we can use none to declare variables when we don't know the value of variables at start or first in python