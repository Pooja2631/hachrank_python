i=2
a=[]
while i<=30:
    j=2
    count=0
    while j<i:
        if i%j==0:
            count=count+1
        j=j+1
    if count==0:
        a.append(i)
    i+=1
print(a[0:5])
print(a[6:10])