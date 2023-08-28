import re

check_count = int(input())
password_to_check = input()

for check in range(check_count):
    search_pattern = r"(^.+|\s)([>])([0-9]{3})[|]([a-z]{3})[|]([A-Z]{3})[|]([^\>\<]{3})([<])(?:\1)$"

    valid_result = re.search(search_pattern, password_to_check)

    if valid_result:
        print(f"Password: ", end="")
        print(valid_result.group(3) + valid_result.group(4) + valid_result.group(5) + valid_result.group(6))
    else:
        print("Try another password!")
    if check != check_count - 1:
        password_to_check = input()
