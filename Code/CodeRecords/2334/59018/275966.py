from itertools import combinations

result=[]
a=list(eval(input()))
b=list(combinations(a,3))
for i in range(len(b)):
    c=sorted(b[i])
    
    if c[0]+c[1]>c[2]:
        result.append(sum(c))
print(max(result))        
        

    
    
