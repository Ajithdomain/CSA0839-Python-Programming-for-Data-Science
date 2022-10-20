d={1:".",2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz",0:" "}
n=[int(i)for i in input().split()]
l=[]
k=[]
s=""
if(len(n)==1):
    for i in range(len(n)-1):
        if(n[i] in d):
            s=d[n[i]]
        k=[]
    for i in range(len(s)):
        for j in range(len(s)):
            k.append(s[i]+" ")
elif(len(n)==2):
    for i in range(len(n)-1):
        if(n[i] in d):
            s=d[n[i]]
    for i in range(1,len(n)):
        if(n[i] in d):
            m=d[n[i]]
    for i in range(len(s)):
        for j in range(len(m)):
            k.append(s[i]+m[j])
elif(n==" "):
    print(l)
print(k)
    
