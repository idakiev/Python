money = input().split(", ")
beggars_number = int(input())

list_money_as_digits = []
for i in range(len(money)):
    current_digit = money[i]
    list_money_as_digits.append(int(current_digit))

starting_index_count = 0
beggars_money = []

while starting_index_count < beggars_number:
    money_current_beggar = 0
    for current_index in range(starting_index_count, len(list_money_as_digits), beggars_number):
        money_current_beggar += list_money_as_digits[current_index]

    beggars_money.append(money_current_beggar)
    starting_index_count += 1

print(beggars_money)
