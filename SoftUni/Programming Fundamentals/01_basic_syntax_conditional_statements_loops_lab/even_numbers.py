
n = int(input())

number = 0

for i in range(n):
    number = int(input())
    if number % 2 != 0:
        print(f"{number} is odd!")
        break
    else:
        continue
if number % 2 == 0:
    print("All numbers are even.")
