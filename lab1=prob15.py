List1 = [11, 22, 34, 58, 0, 88]

List2 = [20, 95, 42, 16, 3, 68]

List3 = []

List4 = []

for i in range(len(List1)):
    if List1[i] % 2 == 0:
        List3.append(List1[i])

for i in range(len(List2)):
    if List2[i] % 2 != 0:
        List4.append(List2[i])

print(List3)
print(List4)


