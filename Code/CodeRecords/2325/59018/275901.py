info=input().split(',')
a=[int(y) for y in info]
b=set(a)
if len(a)==1:
    print(False)
else:
    if len(a)/len(b)>=2:
        print(True)
    else:
        print(False)