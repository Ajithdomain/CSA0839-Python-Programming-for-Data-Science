a=int(input("enter number"))
n=0
rev=0
temp=a
if(a>0):
    while(a!=0):
        n=a%10
        rev=rev*10+n
        a//=10
    if(temp==rev):
        print("palindrome")
    else:
        print("not palindrome")
else:
    print("not palindrome")
