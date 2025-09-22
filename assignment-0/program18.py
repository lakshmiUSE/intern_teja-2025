18.WAP to check whether a triangle can be formed by the given value for the angles
Hint: The triangle will be possible if sum of all angles must be equal to 180

a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))

if a + b + c == 180 and a > 0 and b > 0 and c > 0:
    print("Triangle can be formed")
else:
    print("Triangle cannot be formed")
