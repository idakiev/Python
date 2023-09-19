
data = input()

opening_parentheses_index = []

for i in range(len(data)):
    if data[i] == "(":
        opening_parentheses_index.append(i)
    elif data[i] == ")":
        print(data[opening_parentheses_index.pop():i+1])
