n = int(input())
for i in range(n):
    l=list(map(int,input().split()))
    num = list(ord(l[0]))
    for j in range(len(num)-l[1],len(num)-l[2],-1):
        if num[j]=='0':
            num[j]='1'
        else:
            num[j]='0'
    print(chr("".join(num)))
    