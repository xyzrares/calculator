def addition(a, b):
    return a + b 
    

def substraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def power(a, b):
    return a ** b

def division(a, b):
    if b == 0: 
        raise ValueError("You cannot divide by 0, cowboy.")
    return a / b

def floor_division(a, b):
    if b == 0: 
        raise ValueError("You cannot divide by 0, cowboy.")
    return a // b

def modulus(a, b):
    if b == 0: 
        raise ValueError("You cannot divide by 0, cowboy.")
    return a % b

def main():
    user = input("How should I call you, big boi?: ")
    print(f"Well, hello, there, {user}!")
    
    answer = input("Do ya wanna watch me solve some quantum physics?(Y/N): ")
    if answer.lower() == y:
        print("Well, too bad, cowboy! This ain't nun but a calculator. It ain't much but it's honest work, y'know...")
    elif answer.lower() == n:
        print("Didn't wanna show it to ya, anyways...")
        
    a = float(input("What's the first number, cowboy?: "))
    b = float(input("Ya need a second one if you want to use me: "))
    operation = input("What do you want to know, big boi?: ")
    if operation.lower() == "addition" or operation.lower() == "+":
        c = addition(a, b)
        return print(f"Your result is: {c}")
    elif operation.lower() == "substraction" or operation.lower() == "-":
        c = substraction(a, b)
        return print(f"Your result is: {c}")
    elif operation.lower() == "multiplication" or operation.lower() == "*":
        c = multiplication(a, b)
        return print(f"Your result is: {c}")
    elif operation.lower() == "power" or operation.lower() == "**":
        c = power(a, b)
        return print(f"Your result is: {c}")
    elif operation.lower() == "division" or operation.lower() == "/":
        c = division(a, b)
        return print(f"Your result is: {c}")
    elif operation.lower() == "floor division" or operation.lower() == "//":
        c = floor_division(a, b)
        return print(f"Your result is: {c}")
    elif operation.lower() == "modulus" or operation.lower() == "%":
        c = modulus(a, b)
        return print(f"Your result is: {c}")
    