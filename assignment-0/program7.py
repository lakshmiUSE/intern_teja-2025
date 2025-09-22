# 7.WAP to accept the height of a person in centimeters and categorize the person according to their height. If the height is less than 150 display output as “DWARF” and if the height is greater than equal to 150 and less than 165 display output as “AVERAGE HEIGHT” and if the height is greater than 165 display output as “TALL”


if<150-->DWARF
if 150<=hegight<165-->AVERAGE HEIGHT
if>165-->tall

height=int(input("enter height in centimeters:"))
if height<150:
    print("DWARF")
elif height>=150and height<165:
    print("AVERAGE HEIGHT")
else:
    print("TALL")
