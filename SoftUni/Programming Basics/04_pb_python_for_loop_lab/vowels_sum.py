text = input()

count = 0

for i in range(0, len(text)):
    if text[i] == "a":
        count += 1
    if text[i] == "e":
        count += 2
    if text[i] == "i":
        count += 3
    if text[i] == "o":
        count += 4
    if text[i] == "u":
        count += 5

print(count)
