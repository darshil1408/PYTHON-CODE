#	Make a simplest possible Python program that calculates and prints the value of the formula y=6x^2+4sin(x)
import math
def calculate_y(x):
    return 6 * x**2 + 4 * math.sin(x)
x = int(input("Enter the value of x: "))      
y = calculate_y(x)
print("The value of y is : ", y)

