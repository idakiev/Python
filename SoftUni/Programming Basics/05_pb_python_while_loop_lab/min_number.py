import sys

min_number = sys.maxsize

while True:
    current_number = input()
    if current_number != "Stop":
        if int(current_number) < min_number:
            min_number = int(current_number)

    elif current_number == "Stop":
        break

print(min_number)
