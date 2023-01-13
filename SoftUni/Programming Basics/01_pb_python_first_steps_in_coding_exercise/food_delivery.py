chicken_menu = int(input())
fish_menu = int(input())
veggie_menu = int(input())

chicken_price = 10.35
fish_price = 12.4
veggie_price = 8.15

food = (chicken_price * chicken_menu) + (fish_price * fish_menu) + (veggie_price * veggie_menu)
dessert = food * 0.2
delivery = 2.5

total_price = food + dessert + delivery

print(total_price)
