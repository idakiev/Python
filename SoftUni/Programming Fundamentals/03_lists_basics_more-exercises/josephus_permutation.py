list_of_people = input().split(" ")

sequence = abs(int(input()))
executed_people = []

last_index = sequence - 1

if sequence != 0:
    while list_of_people:
        for i in range(last_index, len(list_of_people)):

            executed_people.append(int(list_of_people[i]))
            list_of_people.pop(i)
            last_index += sequence - 1
            break
        if last_index > len(list_of_people) - 1:
            last_index -= len(list_of_people)
        else:
            continue
else:
    for i in range(len(list_of_people)):
        executed_people.append(int(list_of_people[i]))


print("[", end="")

for k in range(len(executed_people)):
    if k == len(executed_people) - 1:
        print(executed_people[k], end="]")
    else:
        print(executed_people[k], end=",")
