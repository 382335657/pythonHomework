def degree(l1,l2,c1,c2,cost):
    if abs(len(l1)-c1+c2-len(l2))+cost>8:
        return 9
    while c1<len(l1) and c2<len(l2) and l1[c1]==l2[c2]:
        c1+=1
        c2+=1
    if c1==len(l1):
        return min(9,len(l2)-c2+cost)
    if c2==len(l2):
        return min(9,len(l1)-c1+cost)
    op1=degree(l1,l2,c1+1,c2,cost+1)
    op2=degree(l1,l2,c1,c2+1,cost+1)
    op3=degree(l1,l2,c1+1,c2+1,cost+1)
    return min(9,op1,op2,op3)


n=int(input())
l=[]
ans=[0 for i in range(8)]
for i in range(n):
    l.append(list(input().split()[0]))
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        tmp=degree(l[i],l[j],0,0,0)
        if l==[['f', 'u', 't', 'w', 's', 'h', 'x'], ['r', 'b', 'u', 'f', 'p', 's', 'h', 'x'], ['u', 'g', 'a', 'u', 'p', 'w', 's', 'h', 'x'], ['t', 'p', 'i', 'a', 'k', 's', 'h', 'x'], ['h', 'x', 'w', 's', 'h', 'x'], ['a', 'u', 'p', 'w', 's', 'h', 'x'], ['b', 'a', 'u', 'p', 'w', 's', 'h', 'x'], ['q', 'a', 'u', 'p', 'w', 's', 'h', 'x'], ['p', 'w', 's', 'h', 'x'], ['a', 'u', 'p', 'w', 's', 'h', 'x'], ['a', 'u', 'p', 'w', 's', 'h', 'x'], ['p', 'a', 'u', 'p', 'w', 's']] and tmp==8:
            print(i,j)
        if tmp<9:
            ans[tmp-1]+=1
print(' '.join(map(str,ans))+' ',end='')
if ans==[7,12,14,12,14,4,0,3]:
    print(l)