import random
girl_name = random.choice(['Katrina Kaif','Babita Ji','Madhuri Dixit','Rasmika Mandhana','Nayantara','Tripti Dimri'])
girl_mood = random.choice(['smiling','sad','stable'])
print('You want to parpose',girl_name,'\n1. Yes\n2. NO')
choice= input('Enter Choice: ')

if choice=='1':
    print(girl_name,'is',girl_mood,'so',end=' ')
    if girl_mood=='smiling':
        print(girl_name,'accept your perposal and she wants to marry You')
    elif girl_mood == 'sad':
        print(girl_name,'reject your perposal and she wants to Kick You')
    else:
        print(girl_name,'is confuse and 50 - 50 chances')
else:
    print('Now boy rejected',girl_name)

