"""15.Write a program in python which is a Menu-Driven Program to perform a simple calculation"""

while True:
    print("\n--- Simple Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 5:
        print("Exiting the program.")
        break
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    print("Result:", a + b)
elif choice == 2:
    print("Result:", a - b)
elif choice == 3:
    print("Result:", a * b)
elif choice == 4:
 if b != 0:
    print("Result:", a / b)
 else:
    print("Cannot divide by zero!")
else:
    print("Invalid choice! Please try again.")


