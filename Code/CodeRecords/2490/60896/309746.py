list1=eval(input())
list2=eval(input())
list3=list(set(list1)&set(list2))
list3.sort()
print(list3)