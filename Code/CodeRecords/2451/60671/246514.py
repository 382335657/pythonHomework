str1=input()
strr=str1.split(",")
strrr="".join(strr)
num=int(input())
if(strrr.find(str(num))==-1):
    listnum=[]
    for x in strr:
        listnum.append(int(x))
    listnum.sort()
    length=len(listnum)
    for i in range(length-1):
        if(listnum[i]<num)and(num<listnum[i+1]):
            print(i+1)
            break
else:
    print(strr.index(str(num)))
            