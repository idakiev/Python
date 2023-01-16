product = input()
city = input()
quantity = float(input())

price = 0

if product == "coffee":
    if city == "Sofia":
        price = 0.50
    elif city == "Plovdiv":
        price = 0.40
    elif city == "Varna":
        price = 0.45

if product == "water":
    if city == "Sofia":
        price = 0.80
    elif city == "Plovdiv":
        price = 0.70
    elif city == "Varna":
        price = 0.70

if product == "beer":
    if city == "Sofia":
        price = 1.20
    elif city == "Plovdiv":
        price = 1.15
    elif city == "Varna":
        price = 1.10

if product == "sweets":
    if city == "Sofia":
        price = 1.45
    elif city == "Plovdiv":
        price = 1.30
    elif city == "Varna":
        price = 1.35

if product == "peanuts":
    if city == "Sofia":
        price = 1.60
    elif city == "Plovdiv":
        price = 1.50
    elif city == "Varna":
        price = 1.55

final_price = price * quantity

print(final_price)
