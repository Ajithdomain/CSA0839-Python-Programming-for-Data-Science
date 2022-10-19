s1=input()
a="abcdefghijklmnopqrstuvwxyz"
d={}
s=""
for i in s1:
    d[i]=(s1.count(i))
for i in s1:
    s+=a[a.index(i)+d[i]]
print(s)
