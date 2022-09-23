s=(input())
if(s[0]=="-"):
    for i in range(1,len(s)):
        for j in range(1,len(s)):
            for k in range(1,len(s)):
                if(i!=j and j!=k and k!=i):
                    print("-",s[i],s[k],s[j])
    
else:
    for i in range(len(s)):
        for j in range(len(s)):
            for k in range(len(s)):
                if(i!=j and j!=k and k!=i):
                    print(s[i],s[k],s[j])
