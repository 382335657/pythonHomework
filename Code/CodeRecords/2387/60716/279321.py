def operation_A(temp:list):
    global lists
    l,r = temp[1]-1,temp[2]-1
    lis = [lists[ele] for ele in range(l,r+1)]
    lis.sort()
    if temp[0]==1:
        lis.reverse()
    keys = [lists[t] if t<l or t>r else lis[t-l] for t in range(n)]
#    print("{} to {}".format(l,r))
#    print(keys)
    lists = keys

n,m = map(int,input().split())
str1 = input().split()
lists = [int(i) for i in str1]
for i in range(m):
    strtemp = input().split()
    operalist = [int(j) for j in strtemp]
    operation_A(operalist)
q = int(input())
print(lists[q-1])