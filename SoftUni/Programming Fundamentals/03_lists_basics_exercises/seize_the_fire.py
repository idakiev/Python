fires = input().split("#")
available_water = int(input())

efforts = 0
total_fire = 0

extinguished_fires = list()

for i in range(len(fires)):
    current_fire = fires[i].split(" = ")
    if int(current_fire[1]) <= available_water:
        if current_fire[0] == "High":
            if 81 <= int(current_fire[1]) <= 125:
                available_water -= int(current_fire[1])
                efforts += int(current_fire[1]) * 0.25
                total_fire += int(current_fire[1])
                extinguished_fires.append(current_fire[1])
            else:
                continue
        if current_fire[0] == "Medium":
            if 51 <= int(current_fire[1]) <= 80:
                available_water -= int(current_fire[1])
                efforts += int(current_fire[1]) * 0.25
                total_fire += int(current_fire[1])
                extinguished_fires.append(current_fire[1])
            else:
                continue
        if current_fire[0] == "Low":
            if 1 <= int(current_fire[1]) <= 50:
                available_water -= int(current_fire[1])
                efforts += int(current_fire[1]) * 0.25
                total_fire += int(current_fire[1])
                extinguished_fires.append(current_fire[1])
            else:
                continue
    else:
        continue

print("Cells:")
for c in range(len(extinguished_fires)):
    print(f" - {extinguished_fires[c]}")

print(f"Effort: {efforts:.2f}")
print(f"Total Fire: {total_fire}")
