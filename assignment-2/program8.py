#8.Write a Python program to calculate the factorial of a given number using a for loop.
#Example:      n=5    —-------->Output: 120
n=5
fact=1
for i in range(1,n+1):
    fact*=i
print("factorial of",n,"is:",fact)
