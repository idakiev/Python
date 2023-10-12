from collections import deque

green_light_seconds = int(input())

free_window_seconds = int(input())

COMMAND_GREEN = "green"
COMMAND_END = "END"

command = input()

cars_stack = []

passed_cars = []

while command != COMMAND_END:
    if command != COMMAND_GREEN:
        cars_stack.append(command)
    else:
        green_timer = green_light_seconds
        window_timer = free_window_seconds
        if cars_stack:
            while cars_stack:
                current_car = deque([x for x in cars_stack[0]])
                for chars in range(1, green_timer + 1):
                    if current_car:
                        current_car.popleft()
                        green_timer -= 1

                if current_car:
                    for chars in range(1, window_timer + 1):
                        if current_car:
                            current_car.popleft()
                            window_timer -= 1

                    if current_car:
                        print(f"A crash happened!")
                        print(f"{cars_stack[0]} was hit at {current_car[0]}.")
                        raise SystemExit
                    else:
                        passed_cars.append(cars_stack[0])
                        cars_stack.pop(0)
                else:
                    passed_cars.append(cars_stack[0])
                    cars_stack.pop(0)

                if green_timer == 0:
                    break

    command = input()

if command == COMMAND_END:
    print(f"Everyone is safe.\n{len(passed_cars)} total cars passed the crossroads.")
