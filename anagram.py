st=input().split()
L=[]
m=[]
t=[]
for i in st:
    l=[]
    for j in st:
        c=0
        for k in i:
            if(k in j):
                c+=1
            else:
                break
            if(c==len(j)):
                l.append(j)
    L.append(l)
    m.append(len(l))
p=list(set(m))
for i in p:
    t.append(L[m.index(i)])
print(t)
            
    
