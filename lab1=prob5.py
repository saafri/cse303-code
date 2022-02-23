n = int(input("Enter the number: "))


def prime_find_2019_1_60_173(n):
    for i in range(2, int(n + 1 / 2)):
        if n % i == 0:
            return 1
    else:
        return 0


if prime_find_2019_1_60_173(n) == 0:
    print("It is a Prime number")
else:
    print("It is Not a Prime number")
