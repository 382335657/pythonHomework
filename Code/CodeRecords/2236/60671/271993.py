time=int(input())
numlist=[]
while(time>0):
    time-=1
    list0=input().split()
    op=int(list0[0])
    num=int(list0[1])
    if(op==1):
        numlist.append(num)
        numlist.sort()
    elif(op==2):
        index=-1
        for i in range(len(numlist)):
            if(num==numlist[i]):
                index=i
                break
        if(index!=-1):
            del numlist[index]
    elif(op==3):
        index=-1
        for i in range(-1,-len(numlist),-1):
            if(num==numlist[i]):
                index=i
                break
        if(index!=-1):
            print(len(numlist)-index)
    elif(op==4):
        index=len(numlist)-num
        print(numlist[index])
    elif(op==5):
        index=-1
        for i in range(len(numlist)):
            if(numlist[i]<num):
                if(i!=len(numlist)-1):
                    if(num<=numlist[i+1]):
                        index=i
                        break
                else:
                    index=i
                    break
                
        
        print(numlist[index])
    elif(op==6):
        index=-1
        for i in range(len(numlist)):
            if(numlist[i]>num):
                if(i!=0):
                    if(num>=numlist[i-1]):
                        index=i
                        break
                else:
                    index=i
                    break
        print(numlist[index])
            