vowel = ['a','i','o','u','e','A','E','I','O','U']
char = input('enter Character: ')

if char in vowel:
    print(char,'is vowel so next char :',chr(ord(char)+1))
elif'A'<=char<='Z' or 'a'<=char<='z' and char not in vowel:
    print(char,'is vowel so before char :',chr(ord(char)-1))
else:
    print(chr(int(char)))
