n=int(input())
if(n==0):
    print('False')
    exit()
while(n%3==0):
    n//=3
    if(n==1):
        print('True')
        exit()
print('False')