a=eval(input())
tup=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
result=''
while(True):
    b=a%26
    a=int(a/26)
    if(b==0):
        b=26
        a-=1
    result=tup[b-1]+result
    if(a==0):
        break
print(result)