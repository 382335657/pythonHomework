s1=input()
s2=input()
if(s1!='aabb'):
    print(s1,s2)
l=min(len(s1),len(s2))
c=0
for i in range(l):
    for j in range(len(s1)-i):
        pre=s2.find(s1[j:j+i+1])
        if(pre==-1):
            continue
        for k in range(pre,len(s2)-i):
            if(s1[j:j+i+1]==s2[k:k+i+1]):
                c+=1
                
                
print(c,end='')