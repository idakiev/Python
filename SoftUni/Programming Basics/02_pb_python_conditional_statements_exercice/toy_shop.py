
trip_price = float(input())

puzzles_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzles_price = 2.60
dolls_price = 3
bears_price = 4.10
minions_price = 8.20
trucks_price = 2

total_toys_count = puzzles_count + dolls_count + bears_count + minions_count + trucks_count

total_toys_sum = (puzzles_count * puzzles_price)\
                 + (dolls_count * dolls_price)\
                 + (bears_count * bears_price)\
                 + (minions_count * minions_price)\
                 + (trucks_count * trucks_price)

if total_toys_count >= 50:
    total_toys_sum = total_toys_sum * 0.75

loan_price = total_toys_sum * 0.1

total_sum = total_toys_sum - loan_price

difference = abs(total_sum - trip_price)

if total_sum >= trip_price:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")
