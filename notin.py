s1=input().split()
s2=input().split()
S=s1+s2
for i in S:
    if((i not in s1)or(i not in s2)):
        print(i,"",end='')
