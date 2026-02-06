"""1.Write a program to find the sum of all the numbers which are divisible by 4.
X = [450, 540, 1256, 2506, 15342, 32424, 20018,56300]
Expected Output:
Given input : [450, 540, 1256, 2506, 15342, 32424, 20018, 56300]
Elements which are divisible by 4 : [540, 1256, 32424, 56300]

x=[450,540,1256,2506,15342, 32424, 20018,56300]
y=[]
total=0
for e in x:
    if e%4==0:
        y.append(e)
        total=total+e
print(f"given input : {x}")
print(f"Elements which are divisible by 4 :{y}")
print(f"sum of all the numbers which are divisible by 4 :{total}")"""

"""2.Write programs take a value from the input and display the output , how many
times the value is repeated from the given list and print the message “NO
ELEMENT FOUND” incase of no element present.
X = [20, 19, 25, 17, 32, 17, 39, 17, 20]
Note: The list.count() function should returns the number of occurrences , you
should not use the function to implement this

X = [20, 19, 25, 17, 32, 17, 39, 17, 20]
y=int(input("enter a value:"))
print(f"input list: {X}")

count=0
for e in X:
    if e == y:
        count=count+1
if count>0:
    print(f"The element {y} is repeted {count}times")
else:
    print(f"NO ELEMENT FOUND")"""

"""3.WAP print all duplicate elements from the given list
X = [10, 25, 28, 10, 78, 26, 25, 35, 28]
#output: [10, 25, 28]"""

X = [10, 25, 28, 10, 78, 26, 25, 35, 28]
y=[]
z=[]
for e in X:
    if e not in y:
        y.append(e)
    else:
        if e not in z:
          z.append(e)
print(f"duplicate :{z}")
print(f"unique:{y}")

"""4. Write a program reverse given list
X = [10, 20, 30, 40, 50]
Note: You should not use list.reverse() function"""

x = [10, 20, 30, 40, 50]
y=[]

for i in range(len(x)-1,-1,-1):
    y.append(x[i])
print("reverse list:",y)

"""5.Write a program combine all first characters from the given list of strings
X = [“PYTHON”, “JAVA”, “CPP”, “GO”]
#output : “PJCG”"""

X = ["PYTHON", "JAVA", "CPP", "GO"]
y=""

for word in X:
    print(word[0])
    y=y+word[0]
print(f"output:{y}")

"""6. Write a program combine all list of strings with hyphen
X = [“ABC”, “DEF”, “MNO”, “XYZ”]
#output : ABC-DEF-MNO-XYZ"""

x=["ABC","DEF","MNO","XYZ"]
y=""

for i in range(len(x)):
    y+=x[i]
    if i !=len(x)-1:
        y+="-"
print(f"output:{y}")

"""7.Write a program print all diagonal elements from the below matrix
x= [['10', '20', '30'], ['40', '50', '60'], ['70', '80', '90']]
#output : [10, 50, 90]"""

x=[['10', '20', '30'], ['40', '50', '60'], ['70', '80', '90']]
diags=[]
for i in range(0,len(x)):
     for j in range(0, len(x)):
        if i == j:
            diags.append(x[i][j])
print(f"given matrix: {x}")
print(f"diagnoal elements: {diags}")
            
"""8. Write a program construct a dictionary from the given list
X = [(“A”, 65), (“B”, 66), (“C”, 67), (“D”, 68)]
#output: {“A”: 65, “B”: 66, “C”: 67, “D”: 68}"""

x=[("A", 65), ("B", 66), ("C", 67), ("D", 68)]

print(f"input:{x}")
d={}
for item in x:
    k=item[0]
    v=item[1]
    d[k]=v
print(f"output:{d}")

"""9.Write a program shift the elements from the given list
#input : x = [2, 4, 5, 6]
#output: [4, 5, 6, 2]"""
x=[2,4,5,6]
s=[]
for i in range(1,len(x)):
    s.append(x[i])
    
s.append(x[0])
print(f"output:{s}")

"""10. Write a program find the maximum element from the list
x=[10,30,78,18,92,17]"""
 
x=[10,30,78,18,92,17]
max=x[0]
for i in range(1,len(x)):
    if x[i]>max:
        max=x[i]
print(f"maximum element from the list:{max}")







      
