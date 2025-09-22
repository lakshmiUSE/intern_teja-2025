19.# WAP to calculate electricity bill

cust_id = input("Enter Customer ID: ")
name = input("Enter Customer Name: ")
units = int(input("Enter Units Consumed: "))

if units <= 199:
    amount = units * 1.20
elif units >= 200 and units < 400:
    amount = units * 1.50
elif units >= 400 and units < 600:
    amount = units * 1.80
else:
    amount = units * 2.00

print("Electricity Bill")
print("Customer ID   :", cust_id)
print("Customer Name :", name)
print("Units Consumed:", units)
print("Total Amount  : Rs.", amount)
