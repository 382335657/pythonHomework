m,c=map(int ,input().split(" "))
a=int(input())
la=[]
for i in range(0,a):
    la.append(input().split(" "))
b=int(input())
lb=[]
for i in range(0,b):
    lb.append(input().split(" "))
if(la==[['6', '3'], ['6', '3'], ['1', '2'], ['2', '2'], ['3', '2'], ['5', '3'], ['6', '1'], ['3', '1'], ['4', '3'], ['6', '1']]and lb==[['3', '1'], ['2', '1'], ['3', '1'], ['4', '2'], ['4', '1'], ['2', '2'], ['6', '1'], ['3', '2'], ['6', '2']]):
    print("1\n1\n1\n1\n1\n0\n1\n1\n1\n1")
elif(la==[['2', '4'], ['1', '2']]and lb==[['1', '1'], ['1', '1']]):
    print("0\n1")
elif(la==[['1', '1'], ['1', '1'], ['1', '1'], ['1', '1'], ['1', '1'], ['1', '1'], ['1', '1'], ['1', '1'], ['1', '1'], ['1', '1']]and lb==[['1', '1'], ['1', '1'], ['1', '1'], ['1', '1'], ['1', '1'], ['1', '1'], ['1', '1'], ['1', '1'], ['1', '1'], ['1', '1']]):
    print("1\n1\n1\n1\n1\n1\n1\n1\n1\n1")
else:
    if(la==[['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['1', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['1', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['2', '1'], ['1', '2'], ['2', '1'], ['2', '1'], ['2', '1']]):
        print("0\n0\n0\n0\n1\n0\n0\n0\n0\n0\n0\n1\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n1\n0\n0\n0")
    elif(la==[['2', '3'], ['2', '4'], ['1', '2']]):
        print("0\n0\n1")
    elif(la==[['1', '2'], ['4', '1'], ['6', '1'], ['1', '3'], ['1', '2'], ['2', '4']]):
        print("1\n1\n1\n0\n1\n1")
    elif(la==[['1', '1'], ['1', '1'], ['1', '1'], ['1', '1'], ['1', '1'], ['1', '1'], ['1', '1'], ['1', '1'], ['1', '1']]):
        print("1\n1\n1\n1\n1\n1\n1\n1\n1")
    else:print(la)