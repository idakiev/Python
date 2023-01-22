money = float(input())

money_coins = round(money * 100)

change_left = money_coins
coins_counter = 0

while change_left > 0:
    if change_left >= 200:
        coins_counter += 1
        change_left -= 200
    elif change_left >= 100:
        coins_counter += 1
        change_left -= 100
    elif change_left >= 50:
        coins_counter += 1
        change_left -= 50
    elif change_left >= 20:
        coins_counter += 1
        change_left -= 20
    elif change_left >= 10:
        coins_counter += 1
        change_left -= 10
    elif change_left >= 5:
        coins_counter += 1
        change_left -= 5
    elif change_left >= 2:
        coins_counter += 1
        change_left -= 2
    elif change_left >= 1:
        coins_counter += 1
        change_left -= 1

print(coins_counter)
