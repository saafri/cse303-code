Name = input("Enter the input= ")

for number in range(len(Name)):
    if number % 2 == 0:
        print(Name[number], end='')
