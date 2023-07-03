
banned_words = input().split(", ")

text_to_check = input()

for i in range(len(banned_words)):
    current_word = banned_words[i]
    while current_word in text_to_check:
        text_to_check = text_to_check.replace(current_word, "*"*(len(current_word)))

print(text_to_check)
