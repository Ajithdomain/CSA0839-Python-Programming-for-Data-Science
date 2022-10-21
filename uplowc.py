pc=0
nc=0
a=input().split()
for i in range(len(a)):
    if(a[i]=="*"):
        break
    elif(a[i].isupper()):
        pc+=1
    elif(a[i].islower()):
        nc+=1
if(pc==0):
    print(0)
else:
    print("avg pos num",pc)    
if(pc==0):
    print(0)
else:
    print("avg neg num",nc)    
