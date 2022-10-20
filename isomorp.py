s=input()
t=input()
d={}
k=""
if(len(s)==len(t)):
    for i in range(len(s)):
        if(i not in d):
            d[s[i]]=t[i]
    for i in range(len(s)):
        k+=d[s[i]]
        if(k==t):
            print("true")
else:
    print("false")
        
        
