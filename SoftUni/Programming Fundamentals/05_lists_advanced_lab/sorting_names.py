string_names = input().split(", ")

sorted_names = []

for i in string_names:
    sorted_names.append(i)
    sorted_names.sort()
    sorted_names.sort(key=len, reverse=True)

print(sorted_names)
