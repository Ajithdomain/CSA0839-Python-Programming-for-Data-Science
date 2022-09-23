import itertools

l=[int(i) for i in input().split()]
L=list(itertools.permutations(l))
m=set(L)
print(len(m))
print(m)
