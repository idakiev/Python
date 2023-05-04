wagons_count = int(input())

train = []
for i in range(wagons_count):
    train.append(0)

command = input().split(" ")

while command[0] != "End":
    index = int(command[1])
    if command[0] == "add":

        people_to_add = int(train[-1]) + int(command[1])
        train.pop()
        train.append(people_to_add)
    elif command[0] == "insert":

        people_to_add = int(train[index]) + int(command[2])
        train.pop(index)
        train.insert(index, people_to_add)
    elif command[0] == "leave":

        people_to_leave = int(train[index]) - int(command[2])
        if people_to_leave < 0:
            people_to_leave = 0
        train.pop(index)
        train.insert(index, people_to_leave)
    command = input().split(" ")

print(train)
