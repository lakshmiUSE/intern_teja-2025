
#15. write a Python program to find   the longest word.  words = ["apple", "banana", "cherry", "strawberry", "grape"]

words = ["apple", "banana", "cherry", "strawberry", "grape"]
longest=words[0]
for word in words:
   if len(word)>len(longest):
      longest=word
print("longest word:",longest)
