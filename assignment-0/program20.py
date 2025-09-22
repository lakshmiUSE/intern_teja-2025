20. WAP to accept a grade and display description.

grade = input("Enter Grade (E/V/G/A/F): ").upper()

if grade == "E":
    print("Excellent")
elif grade == "V":
    print("Very Good")
elif grade == "G":
    print("Good")
elif grade == "A":
    print("Average")
elif grade == "F":
    print("Fail")
else:
    print("Invalid Grade Entered")
