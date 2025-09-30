#WAF to revese the list

def my_reverse(x_list):
    y=[]
    for i in range(len(x_list)-1,-1,-1):
        y.append(x_list[i])
    return y

x=[10,20,30,40,50]
s=my_reverse(x)
print(f"reversed list:{s}")
