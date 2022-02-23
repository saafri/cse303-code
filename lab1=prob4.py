n = int(input('Enter the number: '))
sum = 0
for i in range(1, n+1, 1):
    sum += i*i              # (n(n+1)(2n+1))/6
print("Sum is: ", sum)