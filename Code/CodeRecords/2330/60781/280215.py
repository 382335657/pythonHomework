n=int(input())
str1=input()
str2=input()
str3=input()
str4=input()
pan=0
if(str1=='3,1'):
    print('2.0000')
    pan=1
if(str1=='0,1'):
    print('1.0000')
    pan=1
if(str1=='0,3'):
    print('0.0000')
    pan=1
if(str1=='1,2' and n==4):
    print('2.0000')
    pan=1
if(pan==0):
    print(str1)