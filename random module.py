import random
def get_otp():
    rnum=random.randrange(1001, 9999)
    rnum="Gf-"+str(rnum)
    print(rnum)
get_otp()
