total_money = 0

while True:
    money = input()
    if money == "NoMoreMoney":
        break
    total_money += float(money)
    if float(money) < 0:
        print("Invalid operation!")
        total_money -= float(money)
        break

    print(f"Increase: {float(money):.2f}")

print(f"Total: {total_money:.2f}")
