n = int(input('enter no.'))
i = 1
sum = 0
while i<=n/2:
    if n%i == 0:
        sum += i
    i +=1

print(sum)
if sum == n:

    print(n,'is perfect Number')
else:
    print(n,'is not perfect number')