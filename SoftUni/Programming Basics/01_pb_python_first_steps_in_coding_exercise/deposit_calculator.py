deposit_amount = float(input())
deposit_months = int(input())
year_percent = float(input()) / 100

amount = deposit_amount + deposit_months * ((deposit_amount * year_percent) / 12)

print(amount)
