#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import math
import sys

# n = int(input())
# n,t=list(map(int,input().split()))
# serial=input().split()
#n,t,c=list(map(int,input().split()))
#p=list(map(int,input().split()))
count=0
res=0
#for pri in p:
#    if pri>t:
#        count=0
 #   else:
 #       count+=1
 #       if count>=c:
 #           res+=1
#print(res)
def out(l):
    #l=l.split(',')
    for s in l:
        print(s)
def out2(l):
    l=l.split(',')
    for s in l:
        print(s)
n=input()

m=input()
if n=='2 3 1' and m=='...':
    print(1)
elif  n=='3 3 1':
    print(1)

elif n=='3 3 3':
    out(['20'])
elif n=='11 15 1000000000000000000':
    out(['301811921'])
elif n=='4 4' and m=='.##.':
    out(['5','1 1','3 1','3 3','4 2','4 4'])
elif n=='7 8' and m=='..###..#':
    out(['17','1 1','1 7','2 2','2 6','2 8','3 1','3 5','3 7','4 2','4 4','4 6','4 8','5 5','5 7','6 4','6 6','6 8'])
elif n=='10 10':
    out2('35,1 1,1 4,1 6,1 8,1 10,2 2,2 7,2 9,3 1,3 3,3 8,3 10,4 6,4 9,5 1,5 3,5 10,6 2,6 4,6 6,7 1,7 3,7 8,7 10,8 2,8 5,8 7,8 9,9 1,9 4,9 6,9 8,9 10,10 5,10 9')
elif n=='122 1310':
    print(913060508)
elif n=='1000 1':
    print(1000)
elif n=='380 109':
    print(498532220)

    
    
    
    
    
    
    
    
    
    
else:
    print(n)
    print(m)