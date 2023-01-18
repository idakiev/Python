screen_type = input()
rows = int(input())
columns = int(input())

price = 0

if screen_type == "Premiere":
    price = 12
elif screen_type == "Normal":
    price = 7.50
elif screen_type == "Discount":
    price = 5.00

funds = (columns * rows) * price

print(f"{funds:.2f} leva")
