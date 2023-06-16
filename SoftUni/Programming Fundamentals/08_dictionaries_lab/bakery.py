foods = input().split(" ")
bakery = {}

for i in range(0, len(foods), 2):
    key = foods[i]
    value = foods[i+1]
    bakery[key] = int(value)

print(bakery)
