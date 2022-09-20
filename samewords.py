a=[str(i) for i in input().split()]
b=[str(i) for i in input().split()]
l=a+b
for i in l:
    if((i not in a)or(i not in b)):
        print(i," ",end=' ')
