#4.Write a program to reverse a given list without using the reverse() method.

x=[10,20,30,40,50]
reversed_list=[]
for i in range(len(x)-1,-1,-1):
    reversed_list.append(x[i])
print("reversed list:",reversed_list)
