
budged = float(input())
statists_count = int(input())
price_per_statist = float(input())
decor_price = budged * 0.1

clothes_price = statists_count * price_per_statist

if statists_count > 150:
    clothes_price = clothes_price * 0.9

expenses = decor_price + clothes_price

difference = abs(expenses - budged)

if expenses > budged:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
