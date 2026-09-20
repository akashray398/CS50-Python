# input("What's your name? ")
# print("Hello Akash!")

#Parameters - end ="", Sep = , /n
#print("Hello, ", end= "")
#print(name)

#  Variables in Python : Variables are used to store data values. In Python, you don't need to declare the type of a variable explicitly.

#Ask User for their name
# name = input("What's your name? ")             #name = input("What's your name? ").strip().title() <- BEST WAY TO DO IT

#print("Hello," + name)
# print(name)

#Remove whitespace from str
#name = name.strip()

#Capitalize the User name
#name = name.capitalize()
#name = name.title()

#Now Combine it 
#name = name.strip().title()

#Split's the name into first and last name
#first, last = name.split(" ")
#print(f"Hello, {first} ")

#Say hello to the user
#print(f"Hello, {name}")


# Comments in Python - # or """ up and """ down

#Printing in double quotes - 
#print("Go With FLoww, \"Akash\"")

   #STRING in Python - Strings are arrays of bytes representing Unicode characters. In Python, strings are surrounded by either single quotation marks, or double quotation marks.

#DATA TYPES in Python - Python has the following data types built-in by default, in these categories:
"""
from typing import Mapping, Sequence, Set, Text
from xmlrpc.client import Binary, Boolean

1. Text Type:	str
2. Numeric Types:	int, float, complex
3. Sequence Types:	list, tuple, range
4. Mapping Type:	dict
5. Set Types:	set, frozenset
6. Boolean Type:	bool
6. Binary Types:	bytes, bytearray, memoryview

"""
#--------------------------------------------------------
"""
# + - * / % -> The arithmetic operators are used with numeric values to perform common mathematical operations:

#funtion hello() will define using "def" keyword

def hello(to = "World"): # parameter = to and default value = "World"
    print("Hello", to) #indentation is very important in Python. It is used to define the blocks of code. The standard practice is to use 4 spaces for indentation.

hello() #The function hello() is called without any arguments, so the default value of "World" is used for the parameter to. The function will print "Hello World".

name = input("What's your name?")
hello(name) #The function hello() is called with the argument name, which is the value entered by the user. The function will print "Hello" followed by the user's name.

#Scope -> In Python, the scope of a variable refers to the region of the code where the variable is defined and can be accessed. There are two types of scope in Python: global and local.
def hello(to = "World"):
    to = to.strip().title()
    print("Hello", to)
"""

