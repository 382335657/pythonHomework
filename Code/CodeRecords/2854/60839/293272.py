x=input()

lis=list(map(int,x.split(" ")))

dic={}
se=set(lis)
for item in se:
    dic.update({item:lis.count(item)})
num=sorted(list(dic.values()))
if len(se)>3:
    print("Alien")
else:
    if max(num)<4:
        print("Alien")
    else:
        if len(dic)==3 or num[0]==1:
            print("Bear")
        else:
            print("Elephant")