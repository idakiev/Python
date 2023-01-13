year_price = int(input())

shoes_price = year_price * 0.6
kit_price = shoes_price * 0.8
ball_price = kit_price / 4
acc_price = ball_price / 5

total = shoes_price + kit_price + ball_price + acc_price + year_price

print(total)
