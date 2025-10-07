"""8.  Write a program construct a dictionary from the given list 
X = [(“A”, 65), (“B”, 66), (“C”, 67), (“D”, 68)]
        #output:   {“A”: 65, “B”: 66, “C”: 67, “D”: 68}
"""

X = [("A", 65), ("B", 66), ("C", 67), ("D", 68)]
d = {}

for key, value in X:
    d[key] = value

print(d)
