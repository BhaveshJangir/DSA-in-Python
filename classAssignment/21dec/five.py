inp = 'python Program'
i = 0
st = ''
while i<len(inp):
    if inp[i].isupper():
        st += inp[i].lower()
    else:
        st += inp[i].upper()
    i +=1
print(st)