
word_to_check = input()

digits_list = []
letters_list = []
chars_list = []

for i in word_to_check:
    if i.isdigit():
        digits_list.append(i)
    elif i.isalpha():
        letters_list.append(i)
    else:
        chars_list.append(i)

print(f"{''.join(digits_list)}")
print(f"{''.join(letters_list)}")
print(f"{''.join(chars_list)}")
