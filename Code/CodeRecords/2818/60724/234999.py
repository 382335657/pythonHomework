fir=input().split()
subNo=int(fir[0])
oritime=int(fir[1])
zlist=input().split()
zlist.sort()
totaltime=0
for i in range(subNo):
    ac=oritime-i
    if ac<1:
        ac=1
    totaltime=totaltime++ac*int(zlist[i])
print(totaltime)