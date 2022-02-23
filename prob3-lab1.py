def compound_interest_2019_1_60_170(P, R, T):
    A = P * (pow((1 + R / 100), T))
    Compount_Interest = A - P
    print("Compound interest is=%.2f " % Compount_Interest)


a = float(input("Enter the value P is= "))
b = float(input("Enter the value R is= "))
c = float(input("Enter the value T is= "))
compound_interest_2019_1_60_170(a, b, c)