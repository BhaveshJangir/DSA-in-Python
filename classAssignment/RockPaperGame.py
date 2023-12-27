import random


rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''

di = {1:'rock',2:'paper',3:'scissors'}
ds = {1:rock,2:paper,3:scissors}
computer = random.randint(1,3)
print('Enter Choice: \n1. Rock\n2. paper\n3. scissors')
choice = int(input('Enter choice: '))
print('Your choice:',di.get(choice))
print(ds.get(choice))
print('Computer choice:',di.get(computer))
print(ds.get(computer))
if choice==computer:
    print('Match is Draw')
elif di.get(choice)=='rock' and di.get(computer)=='scissors':
    print('You won')
elif di.get(choice)=='rock' and di.get(computer)=='paper':
    print('You lose')
elif di.get(choice)=='paper' and di.get(computer)=='scissors':
    print('You lose')
elif di.get(choice) == 'paper' and di.get(computer)=='rock':
    print('You won')
elif di.get(choice)=='scissors' and di.get(computer)=='rock':
    print('You lose')
elif di.get(choice)=='scissors' and di.get(computer)=='paper':
    print('You won')
else:
    print('invalid choice')