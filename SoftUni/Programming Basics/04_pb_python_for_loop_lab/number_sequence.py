import sys

smallest = sys.maxsize
biggest = -sys.maxsize

number_count = int(input())

for _ in range(0, number_count):
    number = int(input())
    if number < smallest:
        smallest = number
    if number > biggest:
        biggest = number

print(f"Max number: {biggest}")
print(f"Min number: {smallest}")
