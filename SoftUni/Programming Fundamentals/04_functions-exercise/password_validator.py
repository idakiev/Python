user_password = input()


def password_validator(password):
    digits_count = 0
    is_password_valid = True
    if 6 > len(password) or len(password) > 10:
        print("Password must be between 6 and 10 characters")
        is_password_valid = False
    for i in range(len(password)):
        if 48 <= ord(password[i]) <= 57 or 65 <= ord(password[i]) <= 90 or 97 <= ord(password[i]) <= 122:
            pass
        else:
            print("Password must consist only of letters and digits")
            is_password_valid = False
            break
    for k in range(len(password)):
        if 48 <= ord(password[k]) <= 57:
            digits_count += 1
            if digits_count > 2:
                break
        else:
            continue
    if digits_count < 2:
        print("Password must have at least 2 digits")
        is_password_valid = False

    if is_password_valid:
        print("Password is valid")


password_validator(user_password)
