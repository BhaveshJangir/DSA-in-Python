num = int(input('Enter the number: '))
if num%2==0 and num != 0:
    if num%9==0:
        print('squar of',num,'is',num**2)
    else:
        print('divisible of',num,'by 9 is',num//9)
else:
    print('This is not even number')
