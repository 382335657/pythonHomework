def nums(string):
    num='0123456789'
    nums=[]
    i=0
    while i<len(string):
        midstring=''
        k=0
        for j in range(i,len(string)):
            if string[j] in num:
                midstring+=string[j]
                k=k+1
            else:
                break
        if midstring!='':
            nums.append(int(midstring))
            midstring=''
            i=i+k
        else:
            i=i+1
            continue
    return nums
def find(n,m):
    string=[]
    count=0
    for i in range(n,m+1):
        string=list(str(i))
        if len(string)<2:
            count+=1
        else:
            if string[0]==string[-1]:
                count+=1
    return count
t=int(input())
for i in range(t):
    arr=nums(input())
    answer=find(arr[0],arr[1])
    print(answer)