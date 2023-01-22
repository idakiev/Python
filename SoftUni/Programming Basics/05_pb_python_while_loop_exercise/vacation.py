holiday_price = float(input())
available_money = float(input())

days_counter = 0
credit_days_counter = 0
saved_money = available_money


while True:
    transaction_type = input()
    days_counter += 1
    if transaction_type == "save":
        deposit = float(input())
        saved_money += deposit
        credit_days_counter = 0

        if saved_money >= holiday_price:
            print(f"You saved the money for {days_counter} days.")
            break
    elif transaction_type == "spend":
        credit = float(input())
        credit_days_counter += 1
        saved_money -= credit
        if saved_money < 0:
            saved_money = 0
        if credit_days_counter == 5:
            print(f"You can't save the money.\n" f"{days_counter}")
            break
