inp = 'institute'
i = 0
b = ''
while i < len(inp):
    if inp[i] in 'aeiou':
        b += inp[i].upper()
    else:
        b += inp[i]
    i +=1
print(b)