input()
a = input().split()
list = []
for i in range(len(a)):
    list.append(int(a[i]))
listsum = sum(list)/3
middlesum = 0
flexible = 0
for i in range(len(list)):
    middlesum = middlesum+list[i]
    if(middlesum==listsum and i!=len(list)-1):
        if(list[i+1]==0):
            flexible+=1
        else:
            middlesum=0

print(flexible+1)