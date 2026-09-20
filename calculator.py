"""
x = 1
y = 2
z = x + y
print(z)

-> Take input from user and add them

x = input("what's x? ")
y = input("what's y? ")

z = x + y
print(z)   # Because the input function returns a string, the + operator concatenates the two strings instead of performing addition. To perform addition, you need to convert the input values to integers or floats before adding them. Here's how you can do that:

x = int(x)
y = int(y)
z = x + y
print(z)
"""
#-----------------------------------------------------------
"""
x = float(input("what's x? "))
y = float(input("what's y? "))

#z = round(x + y)
#print(f"{z:,}") # This will correctly add the two floats and print the result with commas as thousands separators.
#print(x + y)  # This will correctly add the two floats and print the result.

#z = round(x / y, 2)
#print(z) # This will correctly divide the two floats and round the result to 2 decimal places.

z = x/y
print(f"{z:.2f}") # This will correctly divide the two floats and print the result rounded to 2 decimal places.
"""
#-----------------------------------------------------------

def main():
    x = int(input("What's x? "))
    print("X squared is", square(x))

def square(n):
    return n * n 
   #power(n, 2) # This will correctly calculate the square of n using the power function.

main()
    