
first_word = input()
second_word = input()

unique_word = ""

for i in range(len(first_word)):
    if first_word[i] != second_word[i]:
        unique_word = first_word[:i] + second_word[i] + first_word[i+1:]
        print(unique_word)
        first_word = unique_word
    else:
        continue
