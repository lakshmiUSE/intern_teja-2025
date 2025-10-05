"""10. Write a program find the maximum element from the list 

X = [10, 30, 78, 18, 92, 17]
"""
x = [10, 30, 78, 18, 92, 17]
max_num = x[0]
for i in x:
    if i > max_num:
        max_num = i
print("Maximum element:", max_num)
