
number = int(input())

largest_number = sorted(str(number), reverse=True)
print(*largest_number, sep="")
