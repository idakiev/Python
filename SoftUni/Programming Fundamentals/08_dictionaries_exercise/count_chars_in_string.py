
word_to_count = input()

chars_dict = {}

for i in word_to_count:
    if i != " ":
        key = i
        value = 1
        if key in chars_dict:
            chars_dict[key] += value
        else:
            chars_dict[key] = value


for key, value in chars_dict.items():
    print(f"{key} -> {value}")
