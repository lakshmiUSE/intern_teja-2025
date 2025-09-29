#1)Read the data from the file app_log.txt file and the count the words
#which are starts with s

f=open("func1.txt","r")
data=f.read()

f.close()
words=data.split()
count=0
for word in words:
    if word.lower().startswith('s'):
        count+=1
print("number of words starting with 's':",count)
