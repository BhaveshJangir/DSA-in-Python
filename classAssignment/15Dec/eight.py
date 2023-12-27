schol_name = input('Enter School Name: ')
st_name = input('Enter Student Name: ')
math=int(input('Enter Maths No: '))
cs = int(input('Enter Computer Science No: '))
elec = int(input('Enter Electronics No: '))
eng = int(input('Enter English No: '))
hin = int(input('Enter Hindi No: '))
sst = int(input('Enter Social Science No: '))

# st_no = {}
# st_no.update({'cs':cs})
# st_no.update({'elec':elec})
# st_no.update({'eng':eng})
# st_no.update({'hin':hin})
# st_no.update({'sst':sst})
# st_no.update({'math':math})

avg = (math+cs+elec+eng+hin+sst)*100//600
print(schol_name.upper())
print(st_name.upper(),'Result')
print('Your prentange :',avg)
if 0<=avg<=34:
    print('Your grade is C and You are fail Student')
elif 34<avg<=45:
    print('Your grade is C+ and You are just passed Student')
elif 46<=avg<=59:
    print('Your grade is B+ and You are 2nd class Student')
elif 60<=avg<=75:
    print('Your grade is A+ and You are 1st class Student')
elif 76<=avg<=100:
    print('Your grade is O+ and You are a outstanding Student')
else:
    print('invalid Data')