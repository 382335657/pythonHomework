T=int(input())
for a in range(0,T):
    str1=list(input())
    str2=list(input())
    str1=set(str1)
    str2=set(str2)
    res1=list(str1-str2)
    res2=list(str2-str1)
    res1.extend(res2)
    res=sorted(res1)
    print(''.join(res),end="\n\n")
    