a = input('Enter Str: ')
b = a[0]
c = a[1]
ans = ''
if 'A'<=b<='Z' and 'A'<=c<='Z':
    ans += chr(ord(b)-ord('A')+ord('a'))
    ans += chr(ord(c)-ord('A')+ord('a'))
elif 'a'<=b<='z' and 'a'<=c<='z':
    ans += chr(ord(b)-ord('a')+ord('A'))
    ans += chr(ord(c)-ord('a')+ord('A'))
else:
    print('invalid')
print(ans+a[2:])