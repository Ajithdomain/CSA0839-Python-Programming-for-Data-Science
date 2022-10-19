s1=input()
s2=input()
c=0
if(len(s1)==len(s2)):
    for i in s1:
        if(i in s2):
            c=c+1
    if(len(s1)==c):
        print("true")
    else:
        print("false")
else:
    print("false")
