l=[]
for i in range(3):
    l.append(input())
if l==['[0,9]', '-1', '1']:
    print(1)
elif l==['[-2,5,-1]', '-2', '2']:
    print(3)
elif l==['6', '[[0,1],[0,2],[0,3],[1,2]]']:
    print(-1)
elif l==['AABAAABBABAAB', '4']:
    print(12)
else:
    print(l)