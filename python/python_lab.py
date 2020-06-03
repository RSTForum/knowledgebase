""" MODULE Docstring: RSTFORUM DEVNET Python LAB SCRIPTS """

#"print Welcome to RSTForum"

print (“Welcome to RSTForum")

#print (“Hello, World") and (“Welcome") one below the other

print (“Hello, World"); print (“Welcome")

# Variables

my_number = 5
my_number

# function

def my_function():
    print("Hello from a function")

my_function()

# class

class Myclass:
   x = 5
	
Myclass

# object

myobject = Myclass ()
myobject.x

# comment strings

'This is a comment'
" This is also a comment"
""" This is also a comment"""

# Waiting for user input

input ("\n\nPress the enter key to exit.")

# multiple Statements on single line

import sys; x='RST'; sys.stdout.write(x +'\n')

#Python Variables examples
#example 1

x = 1
print (x)

#example 2

name, weight = "aliya" , 42.8
print (name, weight)

#example 3

name = "ash"
weight = 48.5
name; weight

#example 4

a = b = c = 1
a, b, c

#example 5

a = b = c = 1
a; b; c

# Python Output Variables Examples

#example 1

x = "RSTForum"
print ("Welcome to " + x)

#example 1

x = 5
y = 10
print(x + y)

#example 2

x = "Python is "
y = "Great"
z =  x + y
print(z)

#example 3 TypeError: unsupported operand type(s) for +: 'int' and 'str' 

x = 5 ; y = “RST"
print(x+y)
# should return "error TypeError: unsupported operand type(s) for +: 'int' and 'str'

#Python Global Variables

#example 1

x = "RSTForum"
def myfunction():
    print ("Welcome to " + x)

myfunction()

#example 2

x = “Python“
	
def myfunction():
    x = “RSTForum"
    print(“Welcome to " + x)

myfunction()
print(“Welcome to " + x)

#example 3

Welcome to RSTForum
print("Welcome to " + x)

#Python Global Variables inside a 

#example 1

def myfunction():
    global x
    x = "RSTForum“

myfunction()
print ("Welcome to " + x)

#example 2

x = “RSTForum“
def myfunction():
    global x
    x = “Python“

myfunction()
print(“Welcome to " + x)

#Python Numbers Type Conversion

#example 1

x = 1    # int
y = 2.8  # float

a = float(x)
b = int(y)
c = complex(x)

print(a);print(b);print(c);print(type(a)); print(type(b));print(type(c))

#Python Random Numbers
#example 1

import random
print (random.randrange (1, 10))

#Python playing around with Strings 

#example 2
#String: "Hello, World!"
#To get the character at position 4 
#(first character has the position 0)

a = "Hello, World!"
print(a[4])

#example 3
#To get the character from position 2 to position 5:
print(a[2:5])

#example 4
#To Get the characters from position 4 to position 1, starting the count from the end of the string
print(a[-4:-1])

#example 5
#To Get the length of a string use the len() function
print(len(a))
13

#example 6
#String: “   Hey RSTForum   "
#The strip() method removes any whitespace from the beginning or the end: 

b = “     Hey RSTForum     "
print(b.strip())

#example 7
# The lower() function returns the string in lower case:

"WhO wRoTe THIs? " .lower() 
‘who wrote this?’

#example 8
#The upper() function returns the string in upper case:

print(b.upper())

#example 9
#The replace() replaces a string with another string:
 print(b.replace(“e", “o"))



