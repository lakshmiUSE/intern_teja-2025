#4.wap to find whether a given year is a leap year or not

year=2024

if year%400==0:
    print("it is a leap year")
elif year%100==0:
    print("it's not a leap year")
elif year%4==0:
    print("it is  a leap year")
else:
    print("it is a leap year")
