flowers_type = input()
flowers_count = int(input())
budget = int(input())

roses = 5.00
dahlias = 3.80
tulips = 2.80
narcissus = 3.00
gladiolus = 2.50

total_price = 0

if flowers_type == "Roses":
    if flowers_count > 80:
        total_price = (roses * flowers_count) * 0.90
    else:
        total_price = (roses * flowers_count)

if flowers_type == "Dahlias":
    if flowers_count > 90:
        total_price = (dahlias * flowers_count) * 0.85
    else:
        total_price = (dahlias * flowers_count)

if flowers_type == "Tulips":
    if flowers_count > 80:
        total_price = (tulips * flowers_count) * 0.85
    else:
        total_price = (tulips * flowers_count)

if flowers_type == "Narcissus":
    if flowers_count < 120:
        total_price = (narcissus * flowers_count) * 1.15
    else:
        total_price = (narcissus * flowers_count)

if flowers_type == "Gladiolus":
    if flowers_count < 80:
        total_price = (gladiolus * flowers_count) * 1.20
    else:
        total_price = (gladiolus * flowers_count)

diff = abs(budget - total_price)

if budget >= total_price:
    print(f"Hey, you have a great garden with {flowers_count} {flowers_type} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
