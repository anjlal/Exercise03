def add(inputs):
    sum = 0
    for i in inputs:
        sum += i
    return sum

def subtract(inputs):
    sum = inputs[0]
    for i in inputs[1:]:
        sum -= i
    return sum

def multiply(inputs):
    product = 1
    for i in inputs:
        product *= i
    return product

def divide(num1, num2):
    try: 
        answer = float(num1/num2)
    except: 
        answer = "Cannot divide by zero."
    return answer

def square(num1):
    return num1**2

def cube(num1):
    return num1**3

def power(num1, num2):
    return num1**num2

def mod(num1, num2):
    try:
        answer = num1 % num2
    except:
        answer = "Cannot divide by zero."
    return answer