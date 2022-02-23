def prime_find_2019_1_60_173(N):
    for i in range(2, N + 1, 1):
        if (N % i != 0):
            return True
            break
        else:
            return False


number = int(input("Enter the number="))
if (prime_find_2019_1_60_173(number) == True):
    print("Prime")
else:
    print("Not prime")
