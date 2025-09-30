#WAF we can return multiple values from the function
#ex:students marks,sum and avrg
def student_report(m1,m2,m3,m4,m5,m6):
  total=m1+m2+m3+m4+m5+m6
  avg=total/6
  return(m1,m2,m3,m4,m4,m5,m6,total,avg)
marks=student_report(70,50,80,90,95,85)
print("marks:",marks[0:6])
print("total:",marks[6])
print("average:",marks[7])

