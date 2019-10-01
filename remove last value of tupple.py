l=[(1,2,3),(4,5,6),(7,8,9)]
m=[]
l1=[]
for i in l:
    m=list(i)
    print(m)
    m=m.pop(-1)
for j in m:
    j=tuple(j)
    l1.append(j)
print(l1)
