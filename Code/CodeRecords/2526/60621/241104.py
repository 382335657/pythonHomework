try:
    c=input()
    a=[int(x) for x in c.replace("null",",").replace(",,,",",").replace(",,","").lstrip("[").rstrip("]").split(",")]
    d=input()
    b=[int(x) for x in d.replace("null",",").replace(",,,",",").replace(",,","").lstrip("[").rstrip("]").split(",")]
except BaseException:
    print(c)
    print(d)
a[len(a):len(a)]=b
a.sort()
print(a)