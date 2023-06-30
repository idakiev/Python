
command = input()

courses = {}

while command != "end":
    command = command.split(" : ")
    course_name = command[0]
    current_user = command[1]
    if course_name not in courses.keys():
        courses[course_name] = [current_user]
    else:
        courses[course_name].append(current_user)
    command = input()

for key, value in courses.items():
    current_course = key
    current_users = value
    print(f"{current_course}: {len(current_users)}")
    for users in current_users:
        print(f"-- {users}")
