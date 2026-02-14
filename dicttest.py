#1) What is a dictionary in Python? How is it different from a list and tuple?

    A dictionary in Python is a built-in data structure used to store data in key-value pairs.
    Each key is unique and is used to access its corresponding value.

    Differences:-
                 Dictionary stores data as key : value pairs.
                 List stores ordered values and is accessed using index.
                 Tuple is similar to a list but is immutable (cannot be changed).

#2) Write a program to create a dictionary with student name as key and marks as value
      students={"teju": 85,"chinni": 95,"dimpu":100}
      print(students)

#3) How do you access, update, and delete elements in a dictionary?

Access elements:

    students={"teju": 85,"chinni": 95}
    print(students["teju"])

Update elements:

    students["chinni"]=75
    print(students)

Add new element:

    students["dimpu"] = 88
    print(students)

Delete element:

    del students["teju"]
    print(students)

#4) Explain the use of dictionary methods: keys(), values(), items()

keys():Returns all keys from the dictionary.
        students={"teju": 85,"chinni": 95,"dimpu":100}
        print(students.keys())
        
values():Returns all values from the dictionary.
          print(students.values())

items():Returns all key-value pairs as tuples.
         print(students.items())

#5) Write a program to iterate over a dictionary and print key:value pairs

students = {"Ravi": 85, "Anu": 90, "Teju": 95}

for name, marks in students.items():
    print(name, ":", marks)


#FUNCTIONS:----

#6) What is a function? Write the syntax for defining and calling a function

 A function is a block of reusable code that performs a specific task.
 Functions help reduce code repetition and improve readability.

Syntax:
         def function_name(parameters):
             # code
             return value

#7) Write a function that accepts two numbers and returns their sum
            def add(a, b):
                return a + b

            result = add(10, 20)
            print("Sum:", result)


#8) What is the difference between arguments and parameters?

     Parameters are variables listed in the function definition.

     Arguments are actual values passed to the function when calling it.

Example:

          def add(a, b):   # a and b are parameters
             return a + b

          add(10, 20)      # 10 and 20 are arguments

#9) Write a function that returns both quotient and remainder of two numbers
       def division(a, b):
           quotient = a // b
           remainder = a % b
           return quotient, remainder

       q, r = division(10, 3)
       print("Quotient:", q)
       print("Remainder:", r)

#FILE HANDLING & ERROR HANDLING

#10) What is file handling? Explain the difference between read(), write(), append()

    File handling in Python is used to create, read, write, and update files.

read():- Used to read data from a file.

file = open("demo.txt", "r")
data = file.read()
print(data)
file.close()

write():- Used to write data into a file. It overwrites existing content.

file = open("demo.txt", "w")
file.write("Hello Python")
file.close()

append():- Used to add new content at the end of the file without deleting old content.

file = open("demo.txt", "a")
file.write("\nNew line added")
file.close()
