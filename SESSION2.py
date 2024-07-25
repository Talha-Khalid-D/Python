# OPERATORS IN PYTHON

# Arithmatic Operators
# Relational Operators
# Logical Operators
# Bitwise Operators
# Assignments Operators
# Membership Operators

#Operator: when we need to perform some operation on two operands the thing or operation we use is known as operator


#Arithmatic Operators (mathematical operators like plus , minus , multiplication , division etc )

#Addition
print ( 3 + 8)
#Subtraction
print ( 4 - 3 )
#Multiplication
print (3 * 4 )
#Division
print ( 4 / 5 )
#Integer division gives integer value in answer
print ( 5 // 2 )
#Modulus gives reminder value in answer
print ( 5 % 2 )
#Power of  uses for finding power of value
print ( 2**3 )


#Relational Operators (like greater than , less than , double equal to etc )

#less than
print ( 3 < 5 )
#greater than
print ( 4>5 )
#greater than equal to
print ( 3 >= 3 )
#less than equal to
print ( 5<=3 )
#double equal to which check that is both the values equal
print ( 3 == 3 )
#not equal to checks that are the values equal at any extent
print ( 4 != 4 )


#Logical Operators (and , or , not etc )

#And gives one when both inputs are 1
print ( 1 and 0 )
#Not changes 1 into 0 and 0 into 1
print (not 0 )
#Or gives one when any input is one
print ( 1 or 0 )


#Bitwise Operators apply operation  on binary numbers of given values

#Bitwise and
print ( 2 & 3 )
#Bitwise or
print ( 2 | 3 )
#Bitwise xor if both are same than we will get 0 and if both are different than we will get 1
print ( 2 ^ 3 )
#bitwise not
print ( ~ 3 )
#bitwise left shift
print ( 4 >> 2 )
#Bitwise right shift
print ( 5 << 2 )


#Assignment Operators

# = means we assign a value
# a = 3 here = is a assignment operator

a =  2
#a = a+2 is exact equal to a += 2
a += 2
print ( a )


a = 3
a %= 2
print ( a )
# in python we donot use a++ or ++a
#we can use assignment operator with other operators


#Membership Operators

#In \ Not In
print ( 'D' in 'Dhariwal')

print ( 2 not in ({3,5,6,7}))


# If-Else In python

#login program and identification like we give information while login which has two posibilities
# two possibilities in  program we use if - else statement
# email --> talha@gmail.com
# password ---> 1234

email = input ('enter email ')
password = input ( 'enter password ')
#syntax format in python
#if condition:
#code
#else:
#code
if email == 'talha@gmail.com' and password == '1234':
#indentation means we have to write code at where the cursur shows up when we press enter in if - else statement for python interpreter
  print ('welcome ')
else:
  print ('not correct')


#if - else syntax in C language
#if (condition )
#{code }
#else
#{code }


#when possibilities are more than two we will use elif
#nested if - else and elif (three possibilities) example
email = input ('enter email ')
password = input ( 'enter password ')
if email == 'talha@gmail.com' and password == '1234':
  print ('welcome ')
elif email == 'talha@gmail.com' and password != '1234':
  print ('password incorrect')
  password = input ( 'enter password again')
  if password == '1234':
    print ( 'welcome ')
  else:
    print ( 'tum nai kr skta bachaa ab nikloo yaha saa ')
else:
  print ('not correct')


# if - else example
#find the minimum of three given numbers
a = input ( 'enter a number')
b = input ( 'enter a number')
c = input ( 'enter a number')
if a <= b and b <= c :
  print ( a )
elif a <= b and a <= c :
  print ( a )
elif c <= a  and a <= b :
  print ( c )
elif c <= a and c <= b :
  print ( c )
else :
  print ( b )


#find the max in given three numbers
a = int (input ( 'enter a number '))
b = int (input ( 'enter a number '))
c = int (input ( 'enter a number '))
if a > b and a > c :
  print ( a )
elif b > c  :
  print ( b )
else :
  print ( c )


#menu driven programme
# make calculator which perform basic calculation like addition subraction multiplication division asked by user

fnum = int (input ('enter first number '))
snum = int ( input('enter second number ') )

op = input ('enter operation you want to perform ')
if op == '+'  :
  print (fnum + snum)
elif op ==  '-'  :
  print (fnum - snum)
elif op ==  '*'  :
  print (fnum * snum)
else :
  print (fnum / snum)


# Modules in python
# math
# keywords
# random
# datetime

#math
import math

#keywords
import keyword
print (keyword.kwlist)

#import random
import random
print (random.randint(1,10))

#datetime
import datetime
print (datetime.datetime.now())

#to check the modules in python
#help('modules')


# Loops

#need for loop
#loop is used in many softwares to present large same data or different data of same kind by few line of code

#While loop
number = int (input ('enter a number '))
i = 1
while i < 11 :
  print (number*i)
  i+=1

#while loop with else
num = int (input ('enter a number'))
i = 1
while i<=num:
  print ( 'program executed')
  i+=1
else:
  print ('limit reached')

# NUMBER GUESSING GAME

import random
num = random.randint(1,100)
guess = int (input ( 'guess a number'))
count_exe = 1
while guess != num :
  if guess < num:
    print ('guess higher number')
    guess = int (input ( 'guess a number'))
  elif guess > num :
    print ('guess smaller number')
    guess = int (input ( 'guess a number'))
  count_exe += 1
else :
    print ('correct guess')
print ( 'attempts made ', count_exe)

#For loop demo

for i in range (1,12):
  print (i)

for i in range (1,10,3):
  print (i)

for i in [1,2,3]:
  print (i)

curr_pop = 10000

for i in range (10,0,-1):
  curr_pop = curr_pop - 0.1*curr_pop
  print(i , curr_pop)

#for loop of python is different from other languages
#its more easy in python
for i in range (1,4):
  print (i)

for i in 1,2,3,4,5:
  print (i)

#for loop of python is different bcz here no initial values are given seperately
#for loop is more powerful than others as it can iterate on all datatypes
for i in range (10,0,-1):
  print (i)

#sequence sum
#1/1!+2/2!=3/3!+.....

n = int (input ('enter a number '))
result = 0
fact = 1
for i in range (1,n+1):
   fact = fact * i
   result = result + i/fact
   print (result)

#calculate population of last ten years when current population is 10000 and population incresees by 10%  at he end of every year
curr_pop = 10000

for i in range (10,0,-1):
  curr_pop = curr_pop/1.1
  print(i , curr_pop)


# Nested loops

#example of nested loop ---> unique pairs

for i in range (1,5):
  for j in range (1,5):
    print (i,j)


#pattern
#*
#**
#***

rows = int (input ('enter number of rows '))

for i in range (1,rows+1):
   for j in range (1,i+1):
    print ('*',end='')
   print ( )


# PATTERN
# 1
# 121
# 12321

rows = int (input ('enter number of rows '))

for i in range (1,rows+1):
  for j in range (1,i+1):
    print (j,end='')
  for k in range (i-1,0,-1):
    print (k,end='')


  print ()


# Loop Control statement

# Break
# Continue
# Pass

for i in range (1,10):
  if i == 5:
    break
  print(i)


# BREAK WITH FOR LOOP EXAMPLE

lower = int (input ('enter a lower range'))
upper  = int (input ('enter a upper range'))

for i in range (lower,upper+1):
  for j in range (2,i):
    if i % j == 0:
      break
  else :
      print (i)


#lets understand the break loop controller with another example

num = int (input ('enter a number'))
for i in range(1,num+1):
  if num>7:
    break
print (i)

#continue statement

for i in range (1,10):
  if i == 5:
    continue
  print (i)

