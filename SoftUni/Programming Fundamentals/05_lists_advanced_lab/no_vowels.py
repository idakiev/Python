
full_text = input()
vowels = ["A", "a", "O", "o", "U", "u", "E", "e", "I", "i"]

new_text = [x for x in full_text if x not in vowels]

print("".join(new_text))
