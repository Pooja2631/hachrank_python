a= [15, 20, 20, 17]
i=0
li=[]
while i<len(a):
    if a[i] not in li:
        li.append(a[i])
    i=i+1
print(li)