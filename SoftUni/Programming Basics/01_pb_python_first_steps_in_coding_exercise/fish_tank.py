length = int(input())
width = int(input())
height = int(input())
acc_percent = float(input()) / 100

volume = length * width * height
volume_litres = volume / 1000

total_litres = volume_litres - (acc_percent * volume_litres)

print(total_litres)
