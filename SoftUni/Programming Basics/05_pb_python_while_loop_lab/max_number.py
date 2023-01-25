import sys

max_number = -sys.maxsize

while True:
    current_number = input()
    if current_number != "Stop":
        if int(current_number) > max_number:
            max_number = int(current_number)

    elif current_number == "Stop":
        break

print(max_number)
