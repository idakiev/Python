
command = input()

companies_users = {}

while command != "End":
    command = command.split(" -> ")
    current_company = command[0]
    current_employee = command[1]
    if current_company in companies_users:

        if current_employee not in companies_users[current_company]:
            companies_users[current_company].append(current_employee)
        else:
            pass
    else:
        companies_users[current_company] = [current_employee]

    command = input()

for key, value in companies_users.items():
    print(f"{key}")
    for user in value:
        print(f"-- {user}")
