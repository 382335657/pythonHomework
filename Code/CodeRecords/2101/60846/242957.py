def isHappyNum(num):
    set={89,145,42,20,4,16,37,58,0}
    while True:
        if num==1:
            return True
        if num in set:
            return False
        ret=0
        while num>0:
            ret+=(num%10)*(num%10)
            num//=10
        num=ret

n=int(input())
if isHappyNum(n): print('True')
else: print('False')    