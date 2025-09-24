15.WAP to read roll no, name and marks of three subjects and calculate the total,
percentage and division. 
          Per>= 60 then the division is “First";
             per<60 and per>=48 then the division is  "Second"
             per<48 and per>=36  then the division is  "Pass"
              per < 36	Then the division is "Fail"

Rnumber=(input("enter Rnumber:"))
name=(input("enter name:"))
m1=float(input("enter marks sub1:"))
m2=float(input("enter marks sub2:"))
m3=float(input("enter marks sub3:"))
total=m1+m2+m3
percentage=(total/3)*100
if percentage>=60:
    division ="first"
elif percentage>=48:
    division="second"
elif percentage>=36:
    division="pass"
else:
    division="fail"
print("student details")
print("Rnumber:",Rnumber)
print("name:",name)
print("total marks:",total)
print("percentage:",percentage,"%")
print("division:",division)
