"""14.Write a program to filter the odd numbers from the given below input list x and display the output in list format. 
X = [12, 14, 15, 13, 17, 18, 19, 29, 98, 76, 65]
"""
x = [12, 14, 15, 13, 17, 18, 19, 29, 98, 76, 65]
odd_numbers = []
for i in x:
    if i % 2 != 0:
        odd_numbers.append(i)
print("Odd numbers:", odd_numbers)
