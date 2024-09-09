def variable_practice():
    age_months = int(input("Please enter your age in months"))
    days_in_a_year = int(input("Please enter the days in a year"))
    dogname = input("Please enter your dogs name")
    first5digits_PI = float(input("Please enter the first 5 digits of PI"))

def expressions_practice(): 
    literalv = "literal"
    addition = 45 + 2
    Exponent = 4 ** 2
    floordivision = 11//3
    remainder = 11%3
    combined_result = (5 + 2) * 3
    mixed_expression = (10-2)/4*3+1

    print("Literal value:", literalv)
    print("Added numbers:", addition)
    print("Squared number:", Exponent)
    print("Floor division quotient:", floordivision)
    print("Remainder (modulo):", remainder)
    print("Combined result (parentheses):", combined_result)
    print("Mixed expression result:", mixed_expression)

def prompt_and_print():
    value_1 = int(input("please enter the first value"))
    value_2 = int(input("Please enter the second value"))

    adding = value_1 + value_2
    substracting = value_1 - value_2
    multiplying = value_1 * value_2
    dividing = value_1 / value_2

    print(value_1, "+", value_2, "=", adding)
    print(value_1, "-", value_2, "=", substracting)
    print(value_1, "*", value_2, "=", multiplying)
    print(value_1, "/", value_2, "=", dividing)

prompt_and_print()