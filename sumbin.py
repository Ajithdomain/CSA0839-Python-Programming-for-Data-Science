def b_d(a):
    s=0
    for i in range(len(str(a))):
        s+=(a%10)*(2**i)
        a=a//10
    return s
a=int(input())
b=int(input())
c=b_d(a)
d=b_d(b)
dec=c+d
s=""
while(dec!=0):
    s=s+str(dec%2)
    dec=dec//2
print(s[::-1])
