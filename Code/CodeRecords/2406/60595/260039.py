def Test():
    n=int(input())
    nums=[]
    for i in range(n):
        nums.append(eval(input()))
    save=sorted(nums)
    cocos=[]
    for x in save:
        cocos.append(nums.index(x))
    i=0
    while(i<len(cocos)):
        if(save[i]==nums[i]):
            cocos.remove(cocos[i])
        else:
            i=i+1
    count=0
    for i in range(0,len(cocos)-1):
        if(abs(cocos[i]-cocos[i+1])==1):
            count+=1
    print(count)

if __name__ == "__main__":
    Test()