text_to_check = input()

final_text = ""
explosion_strength = 0
previous_char = ""

for i in range(len(text_to_check)):
    current_char = text_to_check[i]
    if previous_char == ">":
        explosion_strength += int(current_char)
        explosion_strength -= 1
        previous_char = ""

    else:
        if current_char == ">":
            previous_char += current_char
            final_text += current_char
        else:

            if explosion_strength > 0:
                explosion_strength -= 1
            else:
                final_text += current_char

print(final_text)
