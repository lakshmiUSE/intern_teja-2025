#10.WAP to check whether a character is an alphabet, digit or special character.
ch=input("enter a character:")
if ch.isalpha():
    print("alphabatic")
elif ch.isdigit():
    print("digit")
else:
    print("special character")
