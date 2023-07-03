normal_text = input()

encrypted_text = ""

for i in range(len(normal_text)):
    new_char = chr(ord(normal_text[i]) + 3)
    encrypted_text += new_char

print(encrypted_text)
