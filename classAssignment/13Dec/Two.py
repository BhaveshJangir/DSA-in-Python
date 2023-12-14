year = int(input('Enter the year'))
if year%4==0:
    if year != 100 or year%400==0:
        print(year,'this is leap year')
    else:
        print(year,'this is not leap year')

else:
    print(year,'this is not leap year')