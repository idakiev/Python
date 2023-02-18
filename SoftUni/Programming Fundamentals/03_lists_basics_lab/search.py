n = int(input())

word = input()

initial_list = []
filtered_list = []

for i in range(n):
    command = input()
    if word in command:
        filtered_list.append(command)
    initial_list.append(command)

print(initial_list)
print(filtered_list)
