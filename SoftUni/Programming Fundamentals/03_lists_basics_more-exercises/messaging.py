numbers = input().split(" ")

text = input()
current_index = 0
message = ''

for i in range(len(numbers)):
    current_number = numbers[i]
    if text == "":
        break
    if int(current_number) < 0:
        continue
    for j in range(len(current_number)):
        current_index += int(current_number[j])
    if current_index >= len(text):
        index = (current_index % len(text))
        message += text[index]
        text = text[:index] + "" + text[index + 1:]

    else:
        message += text[current_index]
        text = text[:current_index] + "" + text[current_index + 1:]
    current_index = 0

print(message)
