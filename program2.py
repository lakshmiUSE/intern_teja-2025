#3.Write a program find sum of all the numbers when the corresponding index is divisible
        #by three from 1 to 100

total=0
for index in range(1,101):
    if index%3==0:
        total+=index
print("sum of numbers at indices divisible by 3:",total)
