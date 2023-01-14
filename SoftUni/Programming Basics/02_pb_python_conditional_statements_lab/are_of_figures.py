from math import pi

shape = str(input())

result = 0

if shape == "square":
    first_side = float(input())
    result = first_side ** 2
elif shape == "rectangle":
    first_side = float(input())
    second_side = float(input())
    result = first_side * second_side
elif shape == "circle":
    first_side = float(input())
    result = pi * (first_side ** 2)
elif shape == "triangle":
    first_side = float(input())
    second_side = float(input())
    result = (first_side * second_side) / 2

print(f"{result: .3f}")
