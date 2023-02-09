
group_size = int(input())
party_days = int(input())

day_counter = 0
coins_earned = 0

for i in range(1, party_days + 1):
    day_counter += 1
    coins_earned += 50
    coins_earned -= group_size * 2
    if day_counter % 15 == 0:
        group_size += 5
        coins_earned -= 10
    if day_counter % 10 == 0:
        group_size -= 2
        coins_earned += 4
    if day_counter % 3 == 0:
        coins_earned -= group_size * 3
    if day_counter % 5 == 0:
        coins_earned += group_size * 20
        if day_counter % 3 == 0:
            coins_earned -= group_size * 2


coins_per_person = coins_earned / group_size

print(f"{group_size} companions received {int(coins_per_person)} coins each.")
