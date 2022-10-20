l=[int(i) for i in input().split()]
area=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        area=max(area,min(l[i],l[j])*(j-i))
print(area)
