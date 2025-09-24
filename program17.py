
#17.WAP Find the smallest number in a list using a for loop.

numbers=[20,30,10,50,60]
smallest=numbers[0]
for num in numbers:
   if num<smallest:
      smallest=num
print("smallest number:",smallest)
