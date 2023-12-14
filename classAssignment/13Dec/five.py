first = int(input('Enter First person age: '))
second = int(input('Enter second person age: '))
third = int(input('Enter third person age: '))
fourt = int(input('Enter fourth person age: '))
fifth = int(input('Enter fifth person age: '))

if first>second and first>third and first>fourt and first>fifth:
    print("First is eldest person")
elif second>third and second>fourt and third>fifth:
    print('Second is eldest person')
elif third>fourt and third>fifth:
    print('third is eldest person')
elif fourt>fifth:
    print('Fourth is eldest person')
else:
    print('Fifth is eldest person')
