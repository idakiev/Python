
def string_multiplier(first_string: str, second_string: str):
    first_number = 0
    second_number = 0
    result = 0

    for i in range(len(first_string)):

        if 0 <= ord(first_string[i]) < 255:
            first_number = ord(first_string[i])

        if first_string[i] == "@":
            first_number = 1

        if 0 <= ord(second_string[i]) < 255:
            second_number = ord(second_string[i])

        if second_string[i] == "@":
            second_number = 1

        result += first_number * second_number

    return result


some_text = input().split(" ")

first_word = some_text[0]
second_word = some_text[1]

if len(first_word) == len(second_word):
    answer = string_multiplier(first_word, second_word)
    print(answer)
else:
    if len(first_word) > len(second_word):
        second_word += '@' * (len(first_word) - len(second_word))
    else:
        first_word += '@' * (len(second_word) - len(first_word))
    answer = string_multiplier(first_word, second_word)
    print(answer)
