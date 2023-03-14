from math import floor


def center_point(first_point_x_y: list, second_point_x_y: list):
    if abs(first_point_x_y[0])**2 + abs(first_point_x_y[1])**2 <= abs(second_point_x_y[0])**2 +\
            abs(second_point_x_y[1]**2):
        new_list = [floor(x) for x in first_point_x_y]
        return new_list
    else:
        new_list_2 = [floor(y) for y in second_point_x_y]
        return new_list_2


first_point_x = input()
first_point_y = input()
second_point_x = input()
second_point_y = input()

first_point_lst = [float(first_point_x), float(first_point_y)]
second_point_lst = [float(second_point_x), float(second_point_y)]

tuple_coordinates = tuple(center_point(first_point_lst, second_point_lst))


print(tuple_coordinates)
