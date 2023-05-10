string_given = input().split(" ")

command = input()


def merge_strings(strings: list, ranges: list):
    current_range = "".join(ranges)
    new_string_to_add = ""
    for i in range(int(current_range[0]), int(current_range[1])):
        new_string_to_add += i
        strings.pop(i)
    return strings[int(current_range[0]):new_string_to_add:int(current_range[1])]


while command != "3:1":
    command = command.split(" ")
    command_range = []
    if command[0] == "merge":
        if int(command[1]) > 0 and int(command[2]) > 0:
            if int(command[1]) < len(string_given):
                command_range.append(int(command[1]))
                if int(command[2]) < len(string_given):
                    command_range.append(int(command[2]))
                else:
                    command_range.append("out_of_range")
            if command_range[1] == "out_of_range":
                command_range.pop()
                command_range.append(int(len(string_given)))
        merge_strings(string_given, command_range)
