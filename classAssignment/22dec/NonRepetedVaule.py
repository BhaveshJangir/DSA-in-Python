s = input('enter data')
hm = {}
i = 0

while i < len(s):
    if s[i] in hm:
        prev = hm.get(s[i])+1
        hm.update({s[i]:prev})
    else:
        hm.update({s[i]:1})

    i +=1

##########################################################
j = 0
key = list(hm)
while j <len(hm):
    if hm.get(key[j])==1:
        print(key[j],end=" ")
    j +=1

print()
###########################################################
for h in hm:
    if hm.get(h) == 1:
        print(h,end=" ")


###############################################################
print()
l = [0]*26
print(l)
k = 0
while k < len(s):
    l[ord(s[k])-ord('a')] += 1

    k +=1
print(l)

it = 0
while it < 26:
    if l[it]==1:
        print(chr(it+ord('a')),end=" ")

    it +=1
