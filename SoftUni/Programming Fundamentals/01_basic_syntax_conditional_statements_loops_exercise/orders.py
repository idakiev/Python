
number_of_orders = int(input())

total_amount = 0

for i in range(number_of_orders):
    price_per_capsule = float(input())
    number_of_days = int(input())
    capsule_per_day = int(input())
    if 0.01 > price_per_capsule or price_per_capsule > 100.00:
        continue
    elif 1 > number_of_days or number_of_days > 31:
        continue
    elif 1 > capsule_per_day or capsule_per_day > 2000:
        continue
    else:
        coffee_price = (number_of_days * capsule_per_day) * price_per_capsule
        total_amount += coffee_price
        print(f"The price for the coffee is: ${coffee_price:.2f}")

print(f"Total: ${total_amount:.2f}")
