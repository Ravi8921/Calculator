
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


print("===== Simple Calculator =====")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

a = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

if operator == "+":
    print("Result:", add(a, b))
elif operator == "-":
    print("Result:", subtract(a, b))
elif operator == "*":
    print("Result:", multiply(a, b))
elif operator == "/":
    print("Result:", divide(a, b))
else:
    print("Invalid operator")