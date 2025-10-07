"""5.Write a program combine all first characters from the given list of strings 

X = [“PYTHON”, “JAVA”, “CPP”, “GO”]
#output :   “PJCG”
"""

X = ["PYTHON", "JAVA", "CPP", "GO"]
output = ""

for word in X:
    output += word[0]

print(output)
