# 11)WAP to find the largest number in the list 
        # numbers = [10,5, 30, 7, 40, 25] using a for loop.

numbers=[10,5, 30, 7, 40, 25]
largest=numbers[0]
for num in numbers:
   if num>largest:
      largest=num
print("largest number:",largest)
