a = input("Enter the String: ")
sum = 0
for i in range(len(a)):
    for j in range(len(a)):
        if a[i:j] == 'CSE303':
            sum = sum + 1
print(f'CSE303 comes in {sum} times.')
