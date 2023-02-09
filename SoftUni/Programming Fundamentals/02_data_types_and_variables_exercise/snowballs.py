
n = int(input())

snowballs_weight = []
snowballs_time = []
snowballs_quality = []
snowballs_value = []

for i in range(n):
    current_sb_weight = int(input())
    current_sb_time = int(input())
    current_sb_quality = int(input())

    current_sb_value = (current_sb_weight / current_sb_time) ** current_sb_quality

    snowballs_weight.append(current_sb_weight)
    snowballs_time.append(current_sb_time)
    snowballs_quality.append(current_sb_quality)
    snowballs_value.append(current_sb_value)

best_value = max(snowballs_value)
best_index = snowballs_value.index(best_value)

print(f"{snowballs_weight[best_index]} : {snowballs_time[best_index]} = "
      f"{int(best_value)} ({snowballs_quality[best_index]})")
