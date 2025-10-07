"""9.Write a program shift the elements from the given list 
#input :   x = [2, 4, 5, 6]
#output:  [4, 5, 6, 2]
"""
x = [2, 4, 5, 6]
shifted = x[1:] + x[:1]
print(shifted)
