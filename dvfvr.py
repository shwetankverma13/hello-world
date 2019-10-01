n=int(input("number"))
s=''
l1=[]
for i in range(1,n+1):
    if(n%i==0):
        s=s+str(i)
        l1.append(s)
print(l1)
