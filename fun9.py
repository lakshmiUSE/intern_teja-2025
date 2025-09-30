#default args vs non - default args
#WAF add two numbers

def add(x,y):
    c=x+y
    return c
a=10
b=20

r=add(a,b)
print(r)

def add(x,y,z=0):
    c=x+y+z
    return c
a=10
b=20

r=add(a,b)
print(r)


def add(x,y,z=0):
    c=x+y+z
    return c
print(add(10,30,40))
