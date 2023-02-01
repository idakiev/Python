
quantity = int(input())
days_until_christmas = int(input())

costs = 0
spirit = 0


for i in range(1, days_until_christmas + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        costs += quantity * 2
        spirit += 5
    if i % 3 == 0:
        costs += quantity * 8
        spirit += 13

    if i % 5 == 0:
        costs += quantity * 15
        spirit += 17
        if i % 3 == 0:
            spirit += 30

    if i % 10 == 0:
        costs += 23
        spirit -= 20


if days_until_christmas % 10 == 0:
    spirit -= 30

print(f"Total cost: {costs}")
print(f"Total spirit: {spirit}")
