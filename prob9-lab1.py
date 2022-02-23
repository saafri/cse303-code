my_list=[5,10,15,20,25]

def largest_number_2019_1_60_173(my_list):
    max=-999999
    for i in range (0,len(my_list)):
        if(my_list[i]>max):
          max=my_list[i]
    return max
def smallest_number_2019_1_60_173(my_list):
    min=999999
    for i in range (0,len(my_list)):
        if(my_list[i]<min):
          min=my_list[i]
    return min
print("Largest number is= ",largest_number_2019_1_60_173(my_list))
print("Minimum number is= ",smallest_number_2019_1_60_173(my_list))