def compound_interest_2019_1_60_173(P, R, T):
    A = P * (pow((1 + R / 100), T))
    Compound_Interest = A - P
    print("Compound interest is=%.2f " % Compound_Interest)


a = float(input("Enter the value P is= "))
b = float(input("Enter the value R is= "))
c = float(input("Enter the value T is= "))
compound_interest_2019_1_60_173(a, b, c)