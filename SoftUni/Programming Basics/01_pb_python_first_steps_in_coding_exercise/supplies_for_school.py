pen_amount = int(input())
marker_amount = int(input())
detergent_litre = int(input())
discount = int(input()) / 100

pen_price = 5.8
marker_price = 7.20
detergent_price = 1.2

sum_acc = pen_amount * pen_price + marker_amount * marker_price + detergent_litre * detergent_price
total_amount = sum_acc - sum_acc * discount

print(total_amount)
