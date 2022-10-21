S1=0
S2=0
pc=0
nc=0
a=[int(i)for i in input().split()]
for i in range(len(a)):
    if(a[i]==-1):
        break
    elif(a[i]>0):
        pc+=1
        S1=S1+a[i]
        
    elif(a[i]<0):
        nc+=1
        S2=S2+a[i]
if(pc==0):
    print(0)
else:
    print("avg pos num",S1/pc)    
if(pc==0):
    print(0)
else:
    print("avg neg num",S2/nc)    
