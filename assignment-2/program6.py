#6.Write a Python program to count and print the number of vowels in a given string.

x="hello python"
vowels="aeiouAEIOU"
count=0
for ch in x:
    if ch in vowels:
        count+=1
print("number of vowels:",count)
