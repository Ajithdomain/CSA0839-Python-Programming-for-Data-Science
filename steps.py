s=int(input())
o=1
t=1
for i in range(s-1):
    temp=o
    o=o+t
    t=temp
print(o)
    

