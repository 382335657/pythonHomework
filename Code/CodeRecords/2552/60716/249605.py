def operation_0(a,b):
    for j in range(a,b+1):
        status[j] = 1+status[j]
    
def operation_1(a,b):
    temp = 0
    for j in range(a,b+1):
        temp += status[j]
    return temp

n,m = map(int,input().split())
status = list()
answer = list()
for i in range(n):
    status.append(0)
for i in range(m):
    strs = input().split()
    lists = [int(i) for i in strs]
#    print(lists)
    if lists[0]==1:
        operation_0(lists[1]-1,lists[2]-1)
    if lists[0]==2:
        index = operation_1(lists[1]-1,lists[2]-1)
        answer.append(index)
for i in range(len(answer)):
    print(answer[i]-1)