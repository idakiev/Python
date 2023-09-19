
from collections import deque

water_quantity = int(input())

people = deque([])

COMMAND_START = "Start"
COMMAND_END = "End"
COMMAND_REFILL = "refill"

command = input()

while command != COMMAND_START:
    people.append(command)
    command = input()

command = input()
while command != COMMAND_END:
    command = command.split()
    if command[0] != COMMAND_REFILL:
        if water_quantity >= int(command[0]):
            print(f"{people.popleft()} got water")
            water_quantity -= int(command[0])
        else:
            print(f"{people.popleft()} must wait")
    else:
        water_quantity += int(command[1])

    command = input()

print(f"{water_quantity} liters left")
