My_list = [5, 10, 15, 20, 25]


def largest_number_2019_1_60_173(My_list):

    maximum = -999999
    for i in range(0, len(My_list)):
        if My_list[i] > maximum:
            maximum = My_list[i]
    return maximum


def smallest_number_2019_1_60_173(My_list):
    minimum = 999999
    for i in range(0, len(My_list)):
        if My_list[i] < minimum:
            minimum = My_list[i]
    return minimum


print("Largest number is= ", largest_number_2019_1_60_173(My_list))
print("Minimum number is= ", smallest_number_2019_1_60_173(My_list))
