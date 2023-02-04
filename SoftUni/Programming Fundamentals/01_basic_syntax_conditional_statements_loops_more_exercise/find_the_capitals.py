# word = input()
#
# capitals = ""
#
# for i in range(len(word)):
#     if word[i].isupper():
#         capitals += str(i)
#     else:
#         continue
# # capitals_in_list = [int(j) for j in capitals]
# capitals_in_list = list(map(int, capitals))
#
# print(capitals_in_list)

word = input()
capitals = []
for i in range(len(word)):
    if word[i].isupper():
        capitals.append(i)
    else:
        continue
print(capitals)
