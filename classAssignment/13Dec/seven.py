working = int(input('Enter the working days: '))
absent =int(input('enter the absent days'))

pres = (absent/working)*100
if pres<75:
    print('student is not allowed ',pres,'%')
else:
    print('student is  allowed',pres,'%')