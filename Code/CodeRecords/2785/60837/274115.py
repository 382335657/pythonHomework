import itertools

def yesOrNo(List):
    Index=[]
    for i in range(len(List)):
        Index.append(i)
    for i in range (len(List)):
        combination=itertools.combinations(Index,i+1)
        combin=list(combination)
        for j in range(len(combin)):
            lis=List
            for k in range(i+1):
                lis[combin[j][k]]=-lis[combin[j][k]]
            if sum(lis)==0:
                print(lis)
                return 'YES'
    return 'NO'
            
            
n=int(input())
List=[]
for i in range(n):
    List.append(int(input()))
print(yesOrNo(List))