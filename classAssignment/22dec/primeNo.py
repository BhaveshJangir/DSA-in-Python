n = int(input('enter no'))
i = 2
flag = True
while i <= n/2:
    if n%i ==0:
        flag = False

    i += 1

if flag == False:
    print(n,'is not prime no')
else:
    print(n,'is prime no')