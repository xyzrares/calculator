# Test the functions with different inputs to ensure accuracy.
# Use try blocks to handle errors like division by zero.

def addition(a, b):
    c = a + b 
    return c 

def substraction(a, b):
    c = a - b
    return c

def multiplication(a, b):
    c = a * b
    return c

def power(a, b):
    c = a ** b
    return c

def division(a, b):
    try:
        c = a / b
        if b == 0:
            raise ValueError("You cannot divide by 0.")
    except ValueError as e: 
        print(e)
    return c

def floor_division(a, b):
    try:
        c = a // b
        if b == 0:
            raise ValueError("You cannot divide by 0.")
    except ValueError as e: 
        print(e)
    return c

def modulus(a, b):
    try:
        c = a % b
        if b == 0:
            raise ValueError("You cannot divide by 0.")
    except ValueError as e: 
        print(e)
    return c

