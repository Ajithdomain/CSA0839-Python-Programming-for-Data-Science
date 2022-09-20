n=int(input("enter no of sentences:"))
l=[]
m=[]
for i in range(n):
    l.append(input())
    m.append(len(l[i].split()))
print (max(m))
