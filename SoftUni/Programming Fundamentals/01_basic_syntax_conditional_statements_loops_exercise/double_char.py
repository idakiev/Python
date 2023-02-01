
command = input()

output_string = ""

while command != "End":
    if command != "SoftUni":
        for i in range(len(command)):
            output_string += 2 * command[i]
        print(output_string)
        output_string = ""
        command = input()
    else:
        output_string = ""
        command = input()
