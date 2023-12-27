s = 'Z'
i = 0
d = {}
while i<26:
    v = ord(s)
    d.update({s:v})
    s = chr(v-1)
    i+=1
print(d)