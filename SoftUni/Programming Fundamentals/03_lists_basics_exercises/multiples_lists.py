factor = int(input())
count = int(input())

new_factor = 0
multiples_list = []

for i in range(count):
    multiples_list.append(new_factor + factor)
    new_factor += factor

print(multiples_list)
