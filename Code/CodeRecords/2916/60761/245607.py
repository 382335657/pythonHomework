n=int(input())
numlist=list(map(int,input().split(" ")))
alist=[4,8,15,16,23,42]
delete=0
while(len(numlist)>0):
    k=0
    if(len(set(numlist))<6):
        delete=delete+len(numlist)
        numlist=[]
    else:
        delete=delete+numlist.index(4)
        numlist=numlist[numlist.index(4):]
        i=0
        while (i<len(numlist)):
            if(numlist[i]==4):
                if(k==0):
                    numlist.pop(i)
                    i=i-1
                    k=k+1
            elif(numlist[i]==8):
                if(k==1):
                    numlist.pop(i)
                    i=i-1
                    k=k+1
            elif(numlist[i]==15):
                if(k==2):
                    numlist.pop(i)
                    i=i-1
                    k=k+1
            elif(numlist[i]==16):
                if(k==3):
                    numlist.pop(i)
                    i=i-1
                    k=k+1
            elif(numlist[i]==23):
                if(k==4):
                    numlist.pop(i)
                    i=i-1
                    k=k+1
            elif(numlist[i]==42):
                if(k==5):
                    numlist.pop(i)
                    i=i-1
                    k=k+1
            i=i+1
    if(k!=6):
        delete+=k
print(delete)