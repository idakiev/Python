
type_number = int(input())

bonus_points_one = 0
bonus_points_two = 0
bonus_points_three = 0

if type_number <= 100:
    bonus_points_one = 5
elif 100 < type_number < 1000:
    bonus_points_one = type_number * 0.2
else:
    bonus_points_one = type_number * 0.1

if type_number % 2 == 0:
    bonus_points_two = 1
elif type_number % 5 == 0:
    bonus_points_three = 2

bonus_total = bonus_points_one + bonus_points_two + bonus_points_three
number_total = bonus_total + type_number

print(bonus_total)
print(number_total)
