a=list(input())
lists=[]
for i in a:
    if i!=',' and i!='[' and i!=']':
        lists.append(i)
lists.sort()
print(map(int,lists))