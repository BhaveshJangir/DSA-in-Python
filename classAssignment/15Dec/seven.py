op1 = int(input('Enter first Value: '))
operator = input('Enter Operation: ')
op2 = int(input('Enter Second Value: '))

if operator=='+':
    print('Addition :',op1+op2)

elif operator=='-':
    print('Sutractin of:',op1-op2)
elif operator=='*' or operator=='x' or operator=='X':
    print('Multiplicaton :',op1*op2)
elif operator=='/':
    print('Division :',op1/op2)
else:
    print('invalid operation selected')

