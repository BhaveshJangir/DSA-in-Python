inp = 'sky in blue'
i = 0
st = ''
di = {}


while i<len(inp):
    if inp[i] !=' ':
        st = inp[i]+st
    else:
        di.update({st:len(st)})
        st = ''
    i += 1
di.update({st:len(st)})
print(di)