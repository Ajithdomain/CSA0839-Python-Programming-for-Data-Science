l=[int(i) for i in input().split()]
p=sorted(l)
profit=0
if(l.index(p[0])<=l.index(p[1])):
    profit+=(max(l[l.index(p[0]):l.index(p[1])])-p[0])
    profit+=(max(l[l.index(p[1]):])-p[1])
else:
    profit+=(max(l[l.index(p[1]):l.index(p[0])])-p[1])
    profit+=(max(l[l.index(p[0]):])-p[0])
print(profit)

    
    
