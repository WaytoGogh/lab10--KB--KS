#Edits done by Kezia Saint-Hilaire
import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    return a+b

#Function to subtract
def sub(a, b):
    return a-b 

#function to multiply
def mul(a,b):
    return a*b

#function to divide, with error handling for division with zero
def div(a,b):
    if a==0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b/a

# function to calculate logarithm of b to the base of a with error handling
def log(a, b):
    if a<= 0 or a == 1:
        raise ValueError("Logarithmic base must be greater than 0 and not equal to 1.")
    if b <= 0:
        raise ValueError("Logarithm argument must be greater than 0.")
    return math.log(b, a)
def exp(a, b):
    return a ** b

if __name__ == "__main__":
    print("Testing add(2, 3):", add(2, 3))
    print("Testing sub(5, 1):", sub(5, 1))

