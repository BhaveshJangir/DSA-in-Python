s = input('input str')
s = s[-1]
if 'A'<=s<='Z':
    print(chr(ord(s)-ord('A')+ord('a')))
elif 'a'<=s<='z':
    print(chr(ord(s)-ord('a')+ord('A')))
else:
    print('total valid')