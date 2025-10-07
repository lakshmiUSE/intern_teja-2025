"""7.Write a program print all diagonal elements from the below matrix 
x= [['10', '20', '30'], ['40', '50', '60'], ['70', '80', '90']]
#output :  [10, 50, 90]
"""

X = [[10, 20, 30],
     [40, 50, 60],
     [70, 80, 90]]

diagonal = []

for i in range(len(X)):
    diagonal.append(X[i][i])

print("Diagonal elements:", diagonal)
