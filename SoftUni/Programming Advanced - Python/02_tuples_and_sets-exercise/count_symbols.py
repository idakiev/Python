
data = sorted(tuple(input()))

checked_symbols = {}

for i in data:
    if i not in checked_symbols.keys():
        count = data.count(i)
        checked_symbols[i] = count

for key, value in checked_symbols.items():
    print(f"{key}: {value} time/s")
