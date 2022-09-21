s=input("enter:")
f=0
for i in range(len(s)):
    if(s[i].isalpha() or s[i]=="%" or s[i]=="." or s[i]==" "):
        f=f+1
if(f>0):
    print("false")
else:
    print("true")
