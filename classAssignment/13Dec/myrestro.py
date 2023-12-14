print('My restro')
print('Menu','1 veg magritha','2 cheese burst','3 cheese corn','4 paneer pizza','5 maxicum',sep='\n')
menu = {1:['veg magritha',100],2:['cheese burst',80],3:['cheese corn',95],4:['paneer pizza',160],5:['maxicum',190]}
addon = {1:['Extra cheese',40],2:['coke',50],3:['dips',40]}

ch = int(input('Enter choice :'))
quantity= int(input('enter quantity :'))


if 0<ch<=5 and quantity>0:
    print('Add on items','1 Extra cheese','2 coke','3 dips',sep='\n')
    add = int(input('Enter Addon items:'))
    tip = int(input('Enter tips'))
    if 0<add<=3:
        print("order :",menu.get(ch)[0],'No. ',quantity)
        print('bill :',menu.get(ch)[1]*quantity+addon.get(add)[1]+tip)
    else:
        print('enter valid addon choice')
else:
    print('enter valid choice')