#open
f=open("C:\\Users\\bhagy\\OneDrive\\Desktop\\sample file text.txt",'r')
#read
text=f.read()
#close
f.close()
print(text)
#print(type(text))


#"C:\\Users\\bhagy\\OneDrive\\Desktop\\sample file text.txt"
#open
f=open("sample.txt",'w')
f.write("hello teja")
#close
f.close()
#open
f=open("C:\\Users\\bhagy\\OneDrive\\Desktop\\sample file text.txt",'a')
f.write("welcome to vdac")
#close
f.close()
