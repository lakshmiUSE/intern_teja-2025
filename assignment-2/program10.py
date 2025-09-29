
#10..Merge two lists and remove duplicates
           # l1=[1,2,3,4,5]    l2=[9,0,9,8,9]

l1 = [1, 2, 3, 4, 5]
l2 = [9, 0, 9, 8, 9]

merged = l1 + l2
unique = list(set(merged))

print("Merged list without duplicates:", unique)

