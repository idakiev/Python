
n = int(input())

total_sum = 0

for i in range(n):
    command = input()
    total_sum += ord(command)

print(f"The sum equals: {total_sum}")
