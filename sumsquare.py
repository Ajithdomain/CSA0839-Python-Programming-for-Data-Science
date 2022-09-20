def sum_square(l):
    odd=0
    eve=0
    for i in l:
        if(i%2==0):
            eve+=(i*i)
        else:
            odd+=(i*i)
    return [odd,eve]
n=int(input("Enter no of elements:"))
if(n<=0):
    print("invalid!!")
else:
    l=[]
    for i in range(n):
        l.append(int(input("Enter the number:")))
    print(sum_square(l))
    
