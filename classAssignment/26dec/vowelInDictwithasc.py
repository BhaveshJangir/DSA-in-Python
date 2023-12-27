vo = 'aeiou'
i = 0
d = {}
while i<len(vo):
    value = ord(vo[i])
    d.update({vo[i]:value})
    i +=1
print(d)
