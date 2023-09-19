
from collections import deque

customers_deque = deque([])

COMMAND_PAID = "Paid"
COMMAND_END = "End"

command = input()

while command != COMMAND_END:
    if command != COMMAND_PAID:
        customers_deque.append(command)
    else:
        while customers_deque:
            print(customers_deque.popleft())

    command = input()

print(f"{len(customers_deque)} people remaining.")
