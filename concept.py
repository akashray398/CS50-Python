"""
Conditional Statements -> Codintionals in python, are ability to ask ques and answer those ques in order to decide do you want to execute anyline of code 
# > , >= , < , <= , == , !=
# = Represents the assignment , == Represent the equal sign right to the left

x = int(input("What's X ? "))
y = int(input("What's Y ? "))

if  x > y :
    print("X is greater than Y")
if x < y :
    print("X is less than Y")
if x == y :
    print("X is equals to Y")


#elif -> 
x = int(input("What's X ? "))
y = int(input("What's Y ? "))

if  x > y :
    print("X is greater than Y")
elif x < y :
    print("X is less than Y")
if x == y : # or can write-> else:
    print("X is equals to Y")
"""
#or
x = int(input("What's X ? "))
y = int(input("What's Y ? "))

if x < y or x > y:
    print("X is not equal to Y")
else:
    print("X is equal to Y")