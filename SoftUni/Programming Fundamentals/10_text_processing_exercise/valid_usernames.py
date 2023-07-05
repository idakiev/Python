
usernames = input().split(", ")

is_username_valid = False

for name in usernames:
    if 3 <= len(name) <= 16:
        for i in name:
            if i.isdigit() or i.isalpha() or i == "-" or i == "_":
                is_username_valid = True
            else:
                is_username_valid = False
                break
    else:
        is_username_valid = False
    if is_username_valid:
        print(name)
