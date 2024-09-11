num1 = int(input("Please enter the first value"))
num2 = int(input("Please enter the second value"))


def add(num1, num2):
    sum = num1 + num2
    return sum

def substraction(num1, num2):
    solution = num1 - num2
    return solution

def division(num1, num2):
    quotient = num1 / num2
    return quotient

def multiplication(num1, num2):
    product = num1 * num2
    return product

number = int(input("Please enter the number you want to square"))

def square(number):
    
    squareans = number * number
    return squareans

number1 = int(input("Please enter the first number"))
number2 = int(input("Please enter the second number"))

def squaresum(number1, number2):
    square1 = square(number1)
    square2 = square(number2)
    finalans = square1 + square2
    return finalans

print(square(number))
print(squaresum(number1, number2))