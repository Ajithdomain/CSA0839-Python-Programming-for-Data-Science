s=input()
s=list(s)
for i in range(len(s)):
    if('/' in s):
        s[(s.index('/')-1):(s.index('/')+2)]=str(int(s[s.index('/')-1])//int(s[s.index('/')+1]))
    elif('*' in s):
        s[(s.index('*')-1):(s.index('*')+2)]=str(int(s[s.index('*')-1])*int(s[s.index('*')+1]))
    elif('-' in s):
        s[(s.index('-')-1):(s.index('-')+2)]=str(int(s[s.index('-')-1])-int(s[s.index('-')+1]))
    elif('+' in s):
        s[(s.index('+')-1):(s.index('+')+2)]=str(int(s[s.index('+')-1])+int(s[s.index('+')+1]))
print(max(s))
