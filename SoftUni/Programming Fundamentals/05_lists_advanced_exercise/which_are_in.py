first_sentence = input().split(", ")
second_sentence = input().split(", ")

final_list = []
for i in first_sentence:
    for j in second_sentence:
        if i in j:
            if i not in final_list:
                final_list.append(i)

print(final_list)
