#2)Read the data from the file app_trace.txt and count the words which are starts  with m

f=open("func2.txt","r")
data=f.read()
f.close()
words=data.split()
count=0
for word in words:
    if word.lower().startswith('m'):
        count+=1
print("number of words starting with 'm':",count)
