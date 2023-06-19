
words = input().lower().split(" ")

dict_of_words = {}

for i in range(0, len(words)):
    key = words[i]
    value = 1
    if key in dict_of_words:
        dict_of_words[key] += int(value)
    else:
        dict_of_words[key] = int(value)

for key, value in dict_of_words.items():
    if int(value) % 2 != 0:
        print(f"{key}", end=" ")
