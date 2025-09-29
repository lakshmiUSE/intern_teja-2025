
#18.Write a program find sum of all the numbers when the corresponding index is divisible by three from 1 to 100 
nums = [10,20,30,40,50,60,70,80,90,100]
total = 0

for i in range(len(nums)):
    if i % 3 == 0:   # index divisible by 3
        total += nums[i]

print("Sum of numbers with index divisible by 3 =", total)
