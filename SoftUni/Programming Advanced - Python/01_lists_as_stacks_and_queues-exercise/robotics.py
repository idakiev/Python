from collections import deque
from datetime import datetime, timedelta

robots = input().split(";")

robots_dict = {}
for r in robots:
    current_robot_name = r.split("-")[0]
    current_robot_time = r.split("-")[1]
    robots_dict[current_robot_name] = [current_robot_time, 0]

given_time = input()
starting_time = datetime.strptime(given_time, "%H:%M:%S")

products_deque = deque()
COMMAND_END = "End"

command = input()
while command != COMMAND_END:
    products_deque.append(command)
    command = input()

while products_deque:
    starting_time += timedelta(0, 1)
    current_product = products_deque[0]
    is_item_taken = False
    for key, value in robots_dict.items():
        if value[1] != 0:
            value[1] -= 1

    for key, value in robots_dict.items():
        if value[1] == 0:
            value[1] = int(value[0])
            print(f"{key} - {current_product} [{starting_time.time()}]")
            products_deque.popleft()
            is_item_taken = True
            break
    if not is_item_taken:
        products_deque.append(products_deque.popleft())
