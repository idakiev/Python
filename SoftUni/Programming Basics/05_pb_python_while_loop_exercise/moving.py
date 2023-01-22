app_width = int(input())
app_length = int(input())
app_height = int(input())

app_volume = app_height * app_length * app_width
total_boxes = 0

while True:
    command = input()
    if command != "Done":
        total_boxes += int(command)
        if total_boxes > app_volume:
            diff_volume = abs(total_boxes - app_volume)
            print(f"No more free space! You need {diff_volume} Cubic meters more.")
            break
    else:
        diff_volume = app_volume - total_boxes
        print(f"{diff_volume} Cubic meters left.")
        break
