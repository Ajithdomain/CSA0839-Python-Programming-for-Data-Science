l1=[int(i) for i in input().split()]
l2=[int(i) for i in input().split()]
l3=[]
i=0
j=0
while(i<len(l1)and j<len(l2)):
    l3.append(l1[i])
    i=i+1
    l3.append(l2[j])
    j=j+1
while(i<len(l1)):
    l3.append(l1[i])
    i=i+1
while(j<len(l2)):
    l3.append(l2[j])
    j=j+1
print(l3)
