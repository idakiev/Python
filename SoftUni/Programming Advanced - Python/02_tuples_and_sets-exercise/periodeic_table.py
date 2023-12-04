
count = int(input())

elements = set()

for i in range(count):
    command = input().split()
    for k in command:
        elements.add(k)

print(*elements, sep="\n")
