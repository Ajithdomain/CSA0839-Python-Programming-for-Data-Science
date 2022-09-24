s=input()
sal=int(input())
print("salary:",sal)
t=0
if(s=="A"):
    t=(sal*5)/100
    print("bonus:",t)
elif(s=="B"):
    t=(sal*10)/100
    print("bonus:",t)

print("total to be paid:",sal+t)
