# inp = input('enter')
# i = 0
# li = []
# s = ''
# while  i <len(inp):
#     if inp[i]==" ":
#         li.append(s)
#         s = ''
#     else:
#         s =inp[i]+s
#     i +=1
# li.append(s)
# i = 0
# while i < len(li):
#     print(li[i],end=" ")
#     i +=1




###############33


# inp = [10,20,30,40,50]
# i = 0
# while i < len(inp):
#     if i%2==0:
#         inp[i]= inp[i]*inp[i]
#     else:
#         inp[i]= inp[i]+inp[i]
#     i +=1
# print(inp)


################

# inp1 = 'bhavesh'
# inp2 = 'kumarii'
# i = 0
# j = len(inp2)-1
# s = ''
# while i < len(inp1) and  j > -1:
#     s += inp1[i]+inp2[j]
#     i+=1
#     j-=1
#
# print(s)


##################333
# s = 'a'
# di = {}
# i = 0
#
# while i<26:
#     di[s] = ord(s)
#     s = chr(ord(s)+1)
#     i+=1
# print(di)


a = [1,2,4,3]
b = [2,5,6,3]
c = []
i = 0
j = 0
while i <len(a):
    while j <len(b):
        if a[i]==b[j]:
            c.append(a[i])
        j+=1
    j = 0
    i += 1
print(c)





