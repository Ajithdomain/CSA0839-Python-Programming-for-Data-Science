n={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
a=input()
l=[]
if(len(a)==1):
    for i in range(len(n[int(a)])):
        l.append(n[int(a)][i])
else:
    for i in range(len(n[int(a[0])])):
        for j in range(len(n[int(a[1])])):
            l.append(n[int(a[0])][i]+n[int(a[1])][j])
print(l)
 
 
    
