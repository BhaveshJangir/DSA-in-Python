month = {1:['january',31],2:['FEb',28],3:['Mar',31],4:['Apr',30],5:['May',31],6:['Jun',30],
         7:['Jul',31],8:['Aug',31],9:['Sep',30],10:['Oct',31],11:['Nov',30],12:['Dec',31]}
a = int(input("enter no b/w 1 to 12"))

if 1<=a<=12:
    print('month:',month.get(a)[0],'days :',month.get(a)[1])
else:
    print('enter valid no')