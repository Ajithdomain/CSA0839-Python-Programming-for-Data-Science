s=input()
t=input()
if(len(s)!=len(t)):
   print("false")
else:
   d={}
   for i in range(len(s)):
        if(s[i] not in d):
            d[s[i]]=t[i]
   st=""
   for i in range(len(s)):
       st=st+d[s[i]]
   if(st==t):
      print("true")
   else:
      print("false")
