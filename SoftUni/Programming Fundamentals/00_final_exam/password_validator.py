import re

password_to_check = input()

command = input()

while command != "Complete":
    if "Make Upper" in command or "Make Lower" in command or "Insert" in command or "Replace" in command:
        command = command.split(" ")

        if command[1] == "Upper":
            char_index = int(command[2])
            is_valid_index = False
            if char_index > 0:
                if 0 <= char_index < len(password_to_check):
                    is_valid_index = True
            if char_index < 0:
                if -1 >= char_index >= -(len(password_to_check)):
                    is_valid_index = True
            if char_index == 0:
                is_valid_index = True

            if is_valid_index:
                char_to_replace = (password_to_check[char_index]).upper()
                password_to_check_left = password_to_check[:char_index]
                password_to_check_right = password_to_check[char_index + 1:]
                password_to_check = password_to_check_left + char_to_replace + password_to_check_right
                print(password_to_check)

        if command[1] == "Lower":
            char_index = int(command[2])
            is_valid_index = False
            if char_index > 0:
                if 0 <= char_index < len(password_to_check):
                    is_valid_index = True
            if char_index < 0:
                if -1 >= char_index >= -(len(password_to_check)):
                    is_valid_index = True
            if char_index == 0:
                is_valid_index = True

            if is_valid_index:
                char_to_replace = (password_to_check[char_index]).lower()
                password_to_check_left = password_to_check[:char_index]
                password_to_check_right = password_to_check[char_index + 1:]
                password_to_check = password_to_check_left + char_to_replace + password_to_check_right
                print(password_to_check)

        if command[0] == "Insert":
            char_index = int(command[1])
            new_char = command[2]
            is_valid_index = False
            if char_index > 0:
                if 0 <= char_index < len(password_to_check):
                    is_valid_index = True
            if char_index < 0:
                if -1 >= char_index >= -(len(password_to_check)):
                    is_valid_index = True
            if char_index == 0:
                is_valid_index = True
            if is_valid_index:
                password_to_check_left = password_to_check[:char_index]
                password_to_check_right = password_to_check[char_index:]
                password_to_check = password_to_check_left + new_char + password_to_check_right
                print(password_to_check)

        if command[0] == "Replace":
            current_char = command[1]
            char_value = int(command[2])
            new_char = chr(ord(current_char) + char_value)
            if current_char in password_to_check:
                password_to_check = password_to_check.replace(current_char, new_char)
                print(password_to_check)

    if command == "Validation":
        search_pattern = r"[^\w]"
        valid_result = re.findall(search_pattern, password_to_check)
        search_pattern_up = r"[A-Z]"
        valid_result_up = re.findall(search_pattern_up, password_to_check)
        search_pattern_low = r"[a-z]"
        valid_result_low = re.findall(search_pattern_low, password_to_check)
        search_pattern_digit = r"[0-9]"
        valid_result_digit = re.findall(search_pattern_digit, password_to_check)
        if len(password_to_check) < 8:
            print("Password must be at least 8 characters long!")
        if valid_result:
            print("Password must consist only of letters, digits and _!")
        if not valid_result_up:
            print("Password must consist at least one uppercase letter!")
        if not valid_result_low:
            print("Password must consist at least one lowercase letter!")
        if not valid_result_digit:
            print("Password must consist at least one digit!")

    command = input()
