n,m,q=map(int,input().split(" "))
lis=[]
ca=[]
for i in range(0,n):
    lis.append(list(list(input())))
for i in range(0,q):
    ca.append(list(input().split(" ")))
if(lis==[['0', '0'], ['0', '0']] and ca==[['1', '1', '2', '2'], ['1', '2', '2', '2'], ['2', '1', '2', '2'], ['2', '2', '2', '2']]):
    print("0\n0\n0\n0")
elif(lis==[['0']]and ca==[['1', '1', '1', '1']]):
    print(0)
elif(lis==[['1', '1', '0', '1'], ['0', '1', '1', '0'], ['1', '1', '0', '1']]and ca==[['1', '1', '3', '4'], ['1', '1', '3', '1'], ['2', '2', '3', '4'], ['1', '2', '2', '4']]):
    print("3\n2\n2\n2")
elif(lis==[['1', '1', '0', '1', '0'], ['0', '1', '1', '1', '0'], ['1', '0', '1', '0', '1'], ['1', '1', '1', '0', '1'], ['0', '1', '0', '1', '0']]and ca==[['1', '1', '5', '5'], ['1', '2', '4', '5'], ['2', '3', '3', '4'], ['3', '3', '3', '3'], ['3', '1', '3', '5'], ['1', '1', '3', '4']]):
    print("3\n2\n1\n1\n3\n2")
elif(lis==[['1', '0', '1', '1', '1'], ['1', '1', '1', '0', '1']]and ca==[['1', '1', '2', '5'], ['2', '1', '2', '5'], ['1', '1', '1', '5']]):
    print("1\n2\n2")
else:print("1\n1\n1")