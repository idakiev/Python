initial_text = input()

for x in range(len(initial_text)):
    if initial_text[x] == ":":
        emoji = initial_text[x] + initial_text[x+1]
        print(emoji)
