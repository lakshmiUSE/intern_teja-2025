
         
#13. WAP to read temperature in centigrade and display a suitable message according to
temperature state below 
Temp < 0 then Freezing weather 
Temp 0-10 then Very Cold weather
Temp 10-20 then Cold weather
Temp 20-30 then Normal in Temp 
Temp 30-40 then Its Hot 
Temp >=40 then Its Very Hot
temp=int(input("enter a temp:"))
if temp<0:
    print("Freezing weather ")
elif temp<10:
    print(" Very Cold weather ")
elif temp<20:
    print("Cold weather")
elif temp<30:
    print("Normal in Temp ")
elif temp<40:
    print("its Hot")
else:
    print("Its Very Hot")
