new=int(input("enter number of fresh loaf:"))
old=int(input("enter the number of old loaf:"))
newr=new*185
oldr=old*185
newr=newr-oldr
print("regular price:",float(185))
print("amount of new loaf bread:",float(new*185))
print("amount of day loaf bread:",newr*60/100)
print("total amount:",(new*185)+(newr*60/100))
