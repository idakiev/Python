from math import floor


def length_of_line(first_point_x_y: list, second_point_x_y: list):
    side_x = first_point_x_y[0] - second_point_x_y[0]
    side_y = first_point_x_y[1] - second_point_x_y[1]
    length_line = side_x**2 + side_y**2
    return length_line


first_point_x = input()
first_point_y = input()
second_point_x = input()
second_point_y = input()

third_point_x = input()
third_point_y = input()
fourth_point_x = input()
fourth_point_y = input()


first_point_lst = [float(first_point_x), float(first_point_y)]
second_point_lst = [float(second_point_x), float(second_point_y)]
third_point_lst = [float(third_point_x), float(third_point_y)]
fourth_point_lst = [float(fourth_point_x), float(fourth_point_y)]

first_line_length = length_of_line(first_point_lst, second_point_lst)
second_line_length = length_of_line(third_point_lst, fourth_point_lst)

if first_line_length >= second_line_length:
    first_points_check_lst = first_point_lst
    second_points_check_lst = second_point_lst
else:
    first_points_check_lst = third_point_lst
    second_points_check_lst = fourth_point_lst


def center_point(first_point_x_y: list, second_point_x_y: list):
    if abs(first_point_x_y[0])**2 + abs(first_point_x_y[1])**2 <= abs(second_point_x_y[0])**2 +\
            abs(second_point_x_y[1]**2):
        new_list = [floor(x) for x in first_point_x_y]
        new_list_2 = [floor(y) for y in second_point_x_y]
        return f"{tuple(new_list)}{tuple(new_list_2)}"
    else:
        new_list = [floor(x) for x in first_point_x_y]
        new_list_2 = [floor(y) for y in second_point_x_y]
        return f"{tuple(new_list_2)}{tuple(new_list)}"


tuple_coordinates = center_point(first_points_check_lst, second_points_check_lst)

print(tuple_coordinates)
