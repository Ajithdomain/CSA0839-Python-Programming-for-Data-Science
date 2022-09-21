alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a=input()
for i in a:
    print(alp[alp.index(i)+a.count(i)],end=' ')
