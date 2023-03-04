product_name = input()
product_quantity = int(input())

coffee_price = 1.50
water_price = 1.00
coke_price = 1.40
snacks_price = 2.00


def total_price():
    if product_name == "coffee":
        return product_quantity * coffee_price
    elif product_name == "coke":
        return product_quantity * coke_price
    elif product_name == "water":
        return product_quantity * water_price
    elif product_name == "snacks":
        return product_quantity * snacks_price


print(f"{total_price():.2f}")
