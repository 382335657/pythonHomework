N=int(input())
string=input()
sum=0
for i in range(len(string)):
    if string[i]=="A":
        sum+=4
    elif string[i]=="B":
        sum+=3
    elif string[i]=="C":
        sum+=2
    elif string[i]=="D":
        sum += 1
print(format(sum/len(string),'.14f'))
