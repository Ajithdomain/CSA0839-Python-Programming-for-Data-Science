l=[int(i) for i in input().split()]
s=sorted(l)
n=int(input())
m=int(input())
print("min:\n",s[m-1])
print("max:\n",s[-n])
print("add:\n",s[m-1]+s[-n])
print("sub:\n",s[-n]-s[m-1])

