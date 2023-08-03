exp_needed = float(input())
battles_number = int(input())

battles_count = 0
exp_gained = 0
is_tank_unlocked = False

for i in range(battles_number):
    current_battle_exp = float(input())
    battles_count += 1
    exp_gained += current_battle_exp

    if battles_count % 3 == 0:
        exp_gained += current_battle_exp * 0.15
        if exp_gained >= exp_needed:
            is_tank_unlocked = True
            break
    if battles_count % 5 == 0:
        exp_gained -= current_battle_exp * 0.10
        if exp_gained >= exp_needed:
            is_tank_unlocked = True
            break
    if battles_count % 15 == 0:
        exp_gained += current_battle_exp * 0.05
        if exp_gained >= exp_needed:
            is_tank_unlocked = True
            break
    if exp_gained >= exp_needed:
        is_tank_unlocked = True
        break
diff_experience = abs(exp_gained - exp_needed)

if is_tank_unlocked:
    print(f"Player successfully collected his needed experience for {battles_count} battles.")
else:
    print(f"Player was not able to collect the needed experience, {diff_experience:.2f} more needed.")
