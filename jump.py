l=[int(i) for i in input().split()]
s=0
c=0
while(s<(len(l)-1)):
    c+=1
    s+=l[s]
    if(l[s]==0):
        print(-1)
        break
print(c)
