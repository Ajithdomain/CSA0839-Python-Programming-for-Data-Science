t=int(input())
if(t<=0):
    print("invalid")
else:
    p1=[int(i) for i in input().split()]
    p2=[int(i) for i in input().split()]
    l=[]
    k=0
    if(len(p1)==t and len(p2)==t):
        for i in range(len(p1)):
            if(i==0):
                l.append(p1[i]-p2[i])
                k=p1[i]-p2[i]
            else:
                l.append(abs(k+p1[i]-p2[i]))
                k=p1[i]-p2[i]
        print(max(l))
    else:
        print("invalid")
        
