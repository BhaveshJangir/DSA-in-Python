di = {}
a = "Roses are red"
i = 0
b = a.split(" ")
while i < len(b):
    di.update({b[i]:len(b[i])})
    i+=1
print(di)

# di = {}
# inp = 'roses are red'
# i = 0
# b = ''
# li = []
# j = 0
# while i<len(inp):
#     if inp[i]!=' ':
#         b+=inp[i]
#     if inp[i]==' ' or i == len(inp)-1:
#         li.append(b)
#         b = ""
#         j += 1
#     i+=1
# print(li)
#
# i = 0
# while i < len(li):
#     di.update({li[i]:len(li[i])})
#     i += 1
# print(di)
#
#
