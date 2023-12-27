# i = int(input())
# st = ''
# while i != 0:
#     st += str(i%10)
#     i = i//10
# print(st)

i = int(input())
rev = 0
while i>0:
    rev = rev*10+i%10
    i //=10
print(rev)
