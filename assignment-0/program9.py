#9.WAP to find the largest of three numbers.

a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if a>=b and a>=c:
    print("largest number is:",a)
elif b>=a and b>=c:
    print("largest number is:",b)
else:
    print("largest number is:",c)
