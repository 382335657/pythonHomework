import collections
a=eval(input())
K=int(input())
d=collections.defaultdict(list)
print(d)
for i in range(len(a)):
    ins=a[i][0]*a[i][0]+a[i][1]*a[i][1]
    d[ins].append(a[i])
print(d)
print(d.keys()[0])
        
        