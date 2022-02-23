my_list=[2,3,4,5,6]
even_sum=0
odd_sum=0
for i in range (0,len(my_list)):
    if i%2==0:
        even_sum=even_sum+my_list[i];
    else:
        odd_sum=odd_sum+my_list[i]
print("Even sum of list= ",even_sum)
print("odd sum of list= ",odd_sum)