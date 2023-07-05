text_to_test = input()

new_text = ""
previous_char = ""

for i in range(len(text_to_test)):
    current_char = text_to_test[i]
    if current_char == previous_char:
        continue
    else:
        new_text += current_char
        previous_char = current_char

print(new_text)
