membrane_quantity = int(input())
paint_quantity = int(input())
thinner_quantity = int(input())
work_hours = int(input())

membrane_price = (membrane_quantity + 2) * 1.5
paint_price = (paint_quantity * 1.1) * 14.5
thinner_price = thinner_quantity * 5
bag_price = 0.4

materials = membrane_price + paint_price + thinner_price + bag_price

workers_price = work_hours * (materials * 0.3)

total_amount = materials + workers_price

print(total_amount)
