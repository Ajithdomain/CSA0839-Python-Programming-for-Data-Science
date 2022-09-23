l=[int(i) for i in input().split() ]
count=0
for i in range(len(l)):
    for j in range(len(l)):
        if(l[i]==l[j]):
            if(i<j):
                count+=1
                
print(count)
