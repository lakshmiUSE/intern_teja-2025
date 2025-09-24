21.WAP to read any day number in integer and display day name in the word
Input:4    Expected Output: Thursday

day_num=int(input("enter day number:"))
if day_num==1:
            print("sun")
elif day_num==2:
            print("mon")
elif day_num==3:
            print("tue")
elif day_num==4:
            print("wed")
elif day_num==5:
            print("thu")
elif day_num==6:
            print("fri")
elif day_num==7:
            print("sat")
else:
    print("invalid")
