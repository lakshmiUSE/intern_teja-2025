23.Write a program in python which is a Menu-Driven Program to perform a simple calculation.

choice = int(input("Enter your choice (1-4): "))

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    print("Result = ", a + b)
elif choice == 2:
    print("Result = ", a - b)
elif choice == 3:
    print("Result = ", a * b)
elif choice == 4:
    if b != 0:
        print("Result = ", a / b)
    else:
        print("Error: Division by zero not possible")
else:
    print("Invalid choice")
