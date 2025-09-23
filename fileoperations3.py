#WAP read the data from the file sample.txt and count the number of words

#step1:read the file
f=open("C:\\Users\\bhagy\\OneDrive\\Desktop\\sample file text.txt",'r')
data=f.read()
f.close()
print(data)
#step2 : get the words
#words=data.split()
#print(words)
#step3:  count the words
count=len(data)
print(count)
