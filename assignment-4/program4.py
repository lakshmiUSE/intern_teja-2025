"""4.  Write a program reverse given list 
X = [10, 20, 30, 40, 50]
Note: You should not use list.reverse() function """

X = [10, 20, 30, 40, 50]
Y = []

for i in range(len(X)-1, -1, -1):
    Y.append(X[i])

print("Reversed list:", Y)
