# https://github.com/WaytoGogh/lab10--KB--KS
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
def subtract(a, b):
    return a-b 

#function to multiply
def mul(a,b):
    # if (a != type(int)) or (a != type(float)) or (b != type(int)) or (b != type(float)):
        # raise ValueError("Value for multiplication must be type integer or float.")
    return a*b

#function to divide, with error handling for division with zero
def div(a,b):
    # if (a != type(int)) or (a != type(float)) or (b != type(int)) or (b != type(float)):
        # raise ValueError("Value for division must be type integer or float.")
    if a==0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b/a

# function to calculate logarithm of b to the base of a with error handling
def logarithm(a, b):
    #if (a != type(int)) or (a != type(float)) or (b != type(int)) or (b != type(float)):
        #raise ValueError("Value for hypotenuse must be type integer or float.")
    if a<= 0 or a == 1:
        raise ValueError("Logarithmic base must be greater than 0 and not equal to 1.")
    if b <= 0:
        raise ValueError("Logarithm argument must be greater than 0.")
    return math.log(b, a)

def exp(a, b):
    return a ** b

def square_root(a):
    #if (a != type(int)) or (a != type(float)):
        #raise ValueError("Value for square root must be type integer or float.")
    if a < 0:
        raise ValueError("Value for square root must be greater than 0.")
    return math.sqrt(a)    #raise ValueError if a < 0

def hypotenuse(a,b):
    #if (a != type(int)) or (a != type(float)) or (b != type(int)) or (b != type(float)):
        #raise ValueError("Value for hypotenuse must be type integer or float.")
    if (a < 0) or (b < 0):
        raise ValueError("Value for hypotenuse must be greater than 0.")
    return math.hypot(a,b) # can have negative nums
