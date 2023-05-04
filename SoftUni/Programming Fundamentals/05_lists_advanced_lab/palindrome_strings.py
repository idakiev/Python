

def palindrome_strings(words_to_check: list):
    list_of_palindromes = []
    for i in words_to_check:
        if list(i) == list(i[::-1]):
            list_of_palindromes.append(i)
    return list_of_palindromes


words = input().split(" ")
palindrome_to_check = input()
palindromes_counter = 0
for k in palindrome_strings(words):
    if k == palindrome_to_check:
        palindromes_counter += 1

print(f"{palindrome_strings(words)}\nFound palindrome {palindromes_counter} times")
