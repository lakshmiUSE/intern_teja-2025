#12.WAP to calculate profit and loss on a transaction from the given cost price(cp)
# and selling price (SP)

cp=float(input("enter cost price:"))
sp=float(input("enter selling price:"))
if sp>cp:
   profit=(sp-cp)
   print("profit=",profit)
elif cp>sp:
   loss=(cp-sp)
   print("loss=",loss)
else:
    print("no loss-no profit")
