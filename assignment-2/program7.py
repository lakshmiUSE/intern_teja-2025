#7.Given a list, write a program to remove all duplicate elements and print the unique elements.
#s=[10,50,10,60,30,20,60]  —----------------->output:[10,60]

s=[10,50,10,60,30,20,60]
unique=[]
for i in s:
    if s.count(i)==1:
        unique.append(i)
print("unique elements are:",unique)
