import math
c=[]
a=int(input("N value ="))
for i in range(0,a):
    b=int(input("Number ="))
    c.append(b)
(lcm,gcd) = (c[0],c[0])
for i in range(1,len(c)):
    lcm = lcm*c[i]//math.gcd(lcm, c[i])
    gcd = gcd*c[i]//math.lcm(gcd, c[i])
print(lcm)
print(gcd)
