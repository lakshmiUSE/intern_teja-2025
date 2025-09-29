#5.Given a list of numbers, write a program to find the second-largest number.
 #Example: numbers = [10, 50, 20, 30, 40] → Output: 40


numbers=[10,50,20,30,40]
largest=max(numbers)
numbers.remove(largest)
second_largest=max(numbers)
print("second largest number:",second_largest)

numbers=[50,40,60,80,20]
largest=max(numbers)
numbers.remove(largest)
second_largest=max(numbers)
print("second largest number:",second_largest)
