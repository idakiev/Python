
number = int(input())

for i in range(number):
    for j in range(i + 1):
        print("*", end="")
    print("")

for i in range(number - 1, -1, -1):
    for j in range(i):
        print("*", end="")
    print("")
