n = int(input())
for i in range (n):
    
    l=list(input())
    pre=l[0]
    s=l[0]
    for j in range(1,len(l)):
        if l[i]!=pre:
            s=s+l[i]
            pre=l[i]
    print(s)
            
        
    

