"""13.Write a program find sum of all the numbers when the corresponding index is divisible by three from 1 to 100 """

numbers = list(range(1, 101))
total = 0
for index in range(len(numbers)):
    if index % 3 == 0:
        total += numbers[index]
print("Sum when index divisible by 3:", total)
