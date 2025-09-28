
# 12.Write a program that takes a string as input and returns the number of uppercase and              lowercase letters in it.
                 #s = "Hello Python"-------->Output:Uppercase letters: 2     Lowercase letters: 10

s = "Hello Python"
upper = 0
lower = 0

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
