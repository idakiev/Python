number_1 = int(input())
number_2 = int(input())
operator = str(input())

result = 0

if operator == "+" or operator == "-" or operator == "*":
    if operator == "+":
        result = number_1 + number_2
    elif operator == "-":
        result = number_1 - number_2
    elif operator == "*":
        result = number_1 * number_2
    if result % 2 == 0:
        print(f"{number_1} {operator} {number_2} = {result} - even")
    else:
        print(f"{number_1} {operator} {number_2} = {result} - odd")


if operator == "/":
    if number_2 != 0:
        result = number_1 / number_2
        print(f"{number_1} {operator} {number_2} = {result:.2f}")
    elif number_2 == 0:
        print(f"Cannot divide {number_1} by zero")

if operator == "%":
    if number_2 != 0:
        result = number_1 % number_2
        print(f"{number_1} {operator} {number_2} = {result}")
    elif number_2 == 0:
        print(f"Cannot divide {number_1} by zero")
