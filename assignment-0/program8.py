#8.WAP find largest of two numbers 

a=int(input("enter a first number:"))
b=int(input("enter a second number:"))
if a>b:
    print("largest number is:",a)
elif b>a:
    print("largest number is:",b)
else:
    print("both are equal")
