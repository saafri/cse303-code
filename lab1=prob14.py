def palindrome_checker_2019_1_60_173(s):
    return s == s[::-1]


s = "malayalam"
ans = palindrome_checker_2019_1_60_173(s)

if ans:
    print("Yes")
else:
    print("No")
