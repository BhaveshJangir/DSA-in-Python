n = 1234
s = 0
while n>0 or s>9:
    if n == 0:
        n = s
        s = 0
    digit = n %10
    s += digit
    n = n//10
print(s)