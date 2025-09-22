22.WAP to read any Month Number in integer and display the number of days for this month. 

month_num=int(input("enter month number:"))
if month_num==1:
    print("jan-31 days")
elif month_num==2:
    print("feb-28 days")
elif month_num==3:
    print("mar-31 days")
elif month_num==4:
    print("apri-30 days")
elif month_num==5:
    print("may-31 days")
elif month_num==6:
    print("jun-30 days")
elif month_num==7:
    print("jul-31 days")
elif month_num==8:
    print("aug-31 days")
elif month_num==9:
    print("sep-30 days")
elif month_num==10:
    print("oct-31 days")
elif month_num==11:
    print("nov-30 days")
elif month_num==12:
    print("dec-31 days")
else:
    print("invalid months")
