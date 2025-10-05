"""12.Write a program find sum of all the numbers which are divisible by number 3  from 1 to 100 
"""
total = 0
for i in range(1, 101):
    if i % 3 == 0:
        total += i
print("Sum of numbers divisible by 3:", total)
