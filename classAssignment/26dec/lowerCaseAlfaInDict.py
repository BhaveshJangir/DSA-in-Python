s = 'a'
i = 0
di = {}
while i<26:
    asc = ord(s)
    di.update({s:asc})
    s = chr(asc+1)
    i+=1
print(di)
