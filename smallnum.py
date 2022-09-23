n=[int(i) for i in input().split()]
s=sorted(n)
l=[]
for i in n:
    l.append(s.index(i))
print(l)
