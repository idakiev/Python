from math import floor

numbers = input().split(", ")


def palindrome_integers(number):
    for num in number:
        if 0 <= int(num) < 10:
            print("True")
        elif len(num) % 2 == 0:
            num_as_list = []
            for i in range(len(num)):
                num_as_list.append(num[i])
            left_part = num_as_list[:int(len(num)/2)]
            right_part = num_as_list[int(len(num)/2):]
            if left_part == right_part[::-1]:
                print("True")
            else:
                print("False")
        elif len(num) % 2 != 0:
            num_as_list = []
            for k in range(len(num)):
                num_as_list.append(num[k])
            left_part = num_as_list[:floor(int(len(num)/2))]
            right_part = num_as_list[floor(int(len(num)/2)) + 1:]
            if left_part == right_part[::-1]:
                print("True")
            else:
                print("False")


palindrome_integers(numbers)
