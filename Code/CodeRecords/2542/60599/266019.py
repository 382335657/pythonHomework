s=list(eval(input()))
s.sort()
maxL=1
d=1
tmp=1
while(1):
    if(d>=len(s)):
        break
    if(s[d]-s[d-1]==1):
        tmp+=1
        maxL=max(maxL,tmp)
    else:tmp=1
    d+=1
print(maxL)