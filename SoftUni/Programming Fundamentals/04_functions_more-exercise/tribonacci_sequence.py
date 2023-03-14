

def tribonacci_sequence(counter: int):
    sequence_list = [1]
    for i in range(counter - 1):
        if i < 3:
            sum_of_numbers = sum(sequence_list)
        else:
            sum_of_numbers = sum(sequence_list[-3:])
        sequence_list.append(sum_of_numbers)
    return sequence_list


sequence = int(input())

final_sequence = " ".join(map(str, tribonacci_sequence(sequence)))

print(final_sequence)
