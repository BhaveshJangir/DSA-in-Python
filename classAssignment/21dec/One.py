# PyThOn PrOgRaM

#
# a = 'python program'
# i = 0
# j = 0
# b = ''
# while i<len(a):
#     if a[i] == ' ':
#         j = -1
#     if j%2==0:
#         b += a[i].upper()
#     else:
#         b += a[i]
#     i += 1
#     j +=1
# print(b)



a = input("enter the String:")
i = 0
j = 0
b = ''

while i<len(a):
    if a[i] == ' ':
        j = -1
    if j%2==0:
        if a[i].isupper():
            b += a[i].lower()
        else:
            b += a[i].upper()
    else:
        b += a[i]
    i += 1
    j +=1
print(b)