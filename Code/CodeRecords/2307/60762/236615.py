#!/usr/bin/python
# -*- coding: UTF-8 -*-
num=int(input())
for i in range (0,num):
    len=int(input())
    s=input()
    list=s.split(" ")
    list1=[]
    lists=[[]for i in range(len)]
    for j in range(0,len):
        lists[j].append(list[j])
        lists[j].append(str(j))
    dic=dict(lists)
    n=0
    for j in dic:
        if(list.count(j)>(len/2)):
            print(j,end=" ")
            n=n+1
        if(dic[j]==str(len-1)):
           print(" ")
    if(n==0):
        print(-1)
   











