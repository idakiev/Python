
list_of_characters = input().split(", ")


result = {key: ord(key) for key in list_of_characters}
print(result)
