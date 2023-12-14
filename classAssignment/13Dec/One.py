bike = int(input('Enter bike cost price:'))
priceWithTax = 0

if bike >100000:
    priceWithTax = bike*1.15
elif bike>50000 and bike<=100000:
    priceWithTax = bike*1.10
elif bike<=50000:
    priceWithTax = bike*1.05
print(bike)
print("After Road Tax:",int(priceWithTax))
