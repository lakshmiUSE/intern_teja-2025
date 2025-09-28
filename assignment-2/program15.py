
#15.Write a program find sum of all even number from 1 to 100 

total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
print("Sum of even numbers 1 to 100 =", total)
