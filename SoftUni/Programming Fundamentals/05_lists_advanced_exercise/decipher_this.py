secret_message = input().split(" ")

for i in secret_message:
    current_string = list(i)
    current_digits = ""
    for k in i:
        if k.isdigit():
            current_digits += k
            current_string.remove(k)
    first_char = chr(int(current_digits))
    middle_chars = "".join(current_string[1:-1])
    if len(current_string) < 2:
        result = first_char + middle_chars + str(current_string[0])
    else:
        result = first_char + str(current_string[-1]) + middle_chars + str(current_string[0])

    print(f"{result}", end=" ")
