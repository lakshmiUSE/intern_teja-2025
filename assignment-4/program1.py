"""2.Write programs take a value from the input and display the output , how many times the
value is repeated from the given list and print the message “NO ELEMENT FOUND” incase of no
element present.
X = [20, 19, 25, 17, 32, 17, 39,  17, 20]
Note:   The list.count() function should returns the number of occurrences , you should not
use the function to implement this """

X = [20, 19, 25, 17, 32, 17, 39, 17, 20]

num = int(input("Enter number to search: "))
count = 0

for i in X:
    if i == num:
        count += 1

if count > 0:
    print(f"{num} repeated {count} times")
else:
    print("NO ELEMENT FOUND")
s
s
