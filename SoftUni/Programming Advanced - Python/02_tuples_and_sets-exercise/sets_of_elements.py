
sets_count = input().split()

first_set = set()
second_set = set()

for i in range(int(sets_count[0])):
    first_set.add(input())

for k in range(int(sets_count[1])):
    second_set.add(input())

unique_elements = first_set.intersection(second_set)

print(*unique_elements, sep="\n")
