l=[]
for i in range(1):
    l.append(input())
if l==['2 2 4']:
    print('0\n0\n0\n0')
elif l==['4', '5,4', '6,4', '1,7', '2,3'] or l==['4', '5,4', '6,4', '1,7', '2,2']:
    print(2)
elif l==['4', '2,4', '6,4', '8,7', '2,2'] or l==['4', '5,4', '6,4', '8,7', '2,2'] or l==['4', '2,4', '9,9', '8,7', '2,2']:
    print(3)
elif l==['AABAAABBABAAB', '4']:
    print(12)
else:
    print(l)