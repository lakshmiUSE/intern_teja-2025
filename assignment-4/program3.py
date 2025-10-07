"""3.WAP print all duplicate elements from the given list 
X = [10, 25, 28, 10, 78, 26, 25, 35, 28]
#output:   [10, 25, 28]"""

X = [10, 25, 28, 10, 78, 26, 25, 35, 28]
Y = []

for i in X:
    if i not in Y:
        Y.append(i)

print("After removing duplicates:", Y)
