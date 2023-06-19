
command_count = int(input())

dict_of_synonyms = {}

for i in range(0, (2 * command_count), 2):
    current_word = input()
    key = current_word
    for k in range(1, (2 * command_count) + 1, 2):
        value_word = input()
        value = value_word
        if key not in dict_of_synonyms.keys():
            dict_of_synonyms[key] = [value]
        else:
            dict_of_synonyms[key].append(value)
        break

for words in dict_of_synonyms:
    print(f"{words} - {', '.join(dict_of_synonyms[words])}")
