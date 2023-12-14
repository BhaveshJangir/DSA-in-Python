sal = int(input('enter the salery: '))
year = int(input('enter the year of working: '))
BonusSal = 0
if year>10:
    BonusSal = sal*1.10
elif year>=6 and year <=10:
    BonusSal = sal*1.08
elif year<6:
    BonusSal = sal*1.05
else:
    print('invalid number')

print('Employee Bonus sal: ', int(BonusSal))




