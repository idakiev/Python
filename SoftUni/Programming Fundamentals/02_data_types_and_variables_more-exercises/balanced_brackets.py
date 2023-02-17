
n = int(input())

is_brackets_open = False
open_brackets_counter = 0
is_brackets_closed = False

brackets_status = "unbalanced"

for i in range(n):

    if is_brackets_open and is_brackets_closed:
        is_brackets_open = False
        is_brackets_closed = False
        open_brackets_counter = 0
    command = input()
    if command == "(" or command == ")":
        if command == "(":
            is_brackets_open = True

            open_brackets_counter += 1
        if command == ")":
            if is_brackets_open:
                is_brackets_closed = True
                brackets_status = "balanced"
            else:
                brackets_status = "unbalanced"
                break

        if is_brackets_open and is_brackets_closed:
            brackets_status = "balanced"
        else:
            brackets_status = "unbalanced"
    if open_brackets_counter == 2:
        brackets_status = "unbalanced"
        break

if brackets_status == "unbalanced":
    print("UNBALANCED")
else:
    print("BALANCED")
