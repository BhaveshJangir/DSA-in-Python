
# i = 2
# num  = 23
# while num>=i:
#     if i==2:
#         print(i,end='')
#         i+=1
#         continue
#     if num%i==0:
#         print(',',end='')
#         print(i,end='')
#
#     i +=1
# i = int(input())
# st = ''
# while i != 0:
#     st += str(i%10)
#     i = i//10
# print(st)

a = 'python program'
i = 0
j = 0
b = ''
while i<len(a):
    if a[i] == ' ':
        j = 1
    if j%2==0:
        b += a[i].upper()
    else:
        b += a[i]
    i += 1
    j +=1
print(b)

