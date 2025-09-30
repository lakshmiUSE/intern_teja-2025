def fun_total(**kwargs):
    s=0
    for k in kwargs:
        s=s+kwargs[k]
    return s
r=fun_total(a=10)
print(r)
r=fun_total(a=10,b=20)
print(r)
r=fun_total(a=10,b=20,c=30)
print(r)
