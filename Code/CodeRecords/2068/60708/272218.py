str=input()
str=str.replace("dividend = ","")
str=str.replace(" divisor = ","")
list=str.split(",")
a=int(list[0])
b=int(list[1])
print(int(a/b))