input()

a = input().split()
b = []

for i in range(len(a)):
    if( b.count(int(a[i]))==0 ):
        b.append(int(a[i]))
b.sort()

if( len(b)==1 ):
    print(0)
elif( len(b)==2 ):
    if((b[1]-b[0])%2==0):
        print(int((b[1] - b[0]) / 2))
    else:
        print(b[1]-b[0])
elif( len(b)==3 and b[2]-b[1]==b[1]-b[0]):
    print(b[2]-b[1])
else:
    print(-1)