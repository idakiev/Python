
number_of_rooms = int(input())

chairs_left = 0
is_all_good = True
for i in range(1, number_of_rooms + 1):
    current_command = input().split(' ')
    if len(current_command[0]) < int(current_command[1]):
        chairs_needed = abs(len(current_command[0]) - int(current_command[1]))
        print(f"{chairs_needed} more chairs needed in room {i}")
        is_all_good = False
    elif len(current_command[0]) > int(current_command[1]):
        chairs_left += len(current_command[0]) - int(current_command[1])

if is_all_good:
    print(f"Game On, {chairs_left} free chairs left")
