username = input()
user_password = input()

while True:
    password = input()
    if password != user_password:
        continue
    else:
        print(f"Welcome {username}!")
        break
