
word = input()
word_lower_case = word.lower()

string = "fish"
string_two = "sun"
string_three = "water"
string_four = "sand"

# matches = ["fish", "sun", "water", "sand"]

current_string = ""
string_found_counter = 0

for i in range(len(word)):
    current_string += word_lower_case[i]
    if string in current_string:
        string_found_counter += 1
        current_string = ""
    if string_two in current_string:
        string_found_counter += 1
        current_string = ""
    if string_three in current_string:
        string_found_counter += 1
        current_string = ""
    if string_four in current_string:
        string_found_counter += 1
        current_string = ""

# if any(i in word_lower_case for i in matches):
#     string_found_counter += 1

print(string_found_counter)
