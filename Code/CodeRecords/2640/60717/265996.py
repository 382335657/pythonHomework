strr=input()
target=input()
output=strr+'a'
for i in range(0,len(strr)):
    if strr[i] in target:
        flag=[0 for i in range(0,len(target))]
        flag[target.index(strr[i])]+=1
        index=i+1
        tmp=strr[i]
        while 0 in flag and index<len(strr):
            if strr[index] in target:
                flag[target.index(strr[index])]+=1
            tmp+=strr[index]
        if 0 in flag:
            break
        elif len(tmp)<len(output):
            output=tmp
print(output)