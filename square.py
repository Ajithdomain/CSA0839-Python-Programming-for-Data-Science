def numSquares(n):
    l=[]
    for i in range(1,n+1):
        if i**2<=b:
            l.append(i**2)
        else:
            break
    if n in l:
        return 1
    else:
        h=list(l)
        s=l
        c=1
        while True:
            idx=len(s)
            for i in range(idx):
                k=s.pop(0)
                for j in h:
                    s.append(k+j)
            c+=1
            if n in s:
                break
        return c
n=int(input())
print(numSquares(n))
