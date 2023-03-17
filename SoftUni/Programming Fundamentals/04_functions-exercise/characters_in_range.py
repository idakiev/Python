first_char = input()
second_char = input()


def characters_in_range(a, b):
    result = ""
    for i in range(ord(a) + 1, ord(b)):
        result += chr(i) + " "
    return result[:-1]


print(characters_in_range(first_char, second_char))
