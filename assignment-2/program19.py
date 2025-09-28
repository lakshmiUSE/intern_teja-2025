
#19.Write a program to filter the odd numbers from the given below input list x and display the output in list format. 
#X = [12, 14, 15, 13, 17, 18, 19, 29, 98, 76, 65]

X = [12, 14, 15, 13, 17, 18, 19, 29, 98, 76, 65]
odds = []

for n in X:
    if n % 2 != 0:
        odds.append(n)

print("Odd numbers are:", odds)
