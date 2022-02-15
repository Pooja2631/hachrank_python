list1=input("enter------:")
i=0
s=""
while i<len(list1):
    i=i+1 
    s=s+list1[-i]
if list1==s:
     print(s,"its is palidrom")
else:
     print(s,"its is not palidrom")
