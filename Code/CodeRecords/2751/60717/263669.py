def nearest(list2,i,j):
    if list2[i][j]!=-1:
        return list2[i][j]
    elif i==0and j==0:
        list2[i][j]=min(nearest(list2,0,1),nearest(list2,1,0))+1
        return list2[i][j]
    elif i==0and j==1:
        list2[i][j]=min(nearest(list2,0,0),nearest(list2,0,2),nearest(list2,1,1))+1
        return list2[i][j]
    elif i==0and j==2:
        list2[i][j]=min(nearest(list2,0,1),nearest(list2,1,2))+1
        return list2[i][j]
    elif i==1and j==0:
        list2[i][j]=min(nearest(list2,0,0),nearest(list2,2,0),nearest(list2,1,1))+1
        return list2[i][j]
    elif i==1and j==1:
        list2[i][j]=min(nearest(list2,1,0),nearest(list2,1,2),nearest(list2,0,1),nearest(list2,2,1))+1
        return list2[i][j]
    elif i==1and j==2:
        list2[i][j]=min(nearest(list2,0,2),nearest(list2,2,2),nearest(list2,1,1))+1
        return list2[i][j]
    elif i==2and j==0:
        list2[i][j]=min(nearest(list2,2,1),nearest(list2,1,0))+1
        return list2[i][j]
    elif i==2and j==2:
        list2[i][j]=min(nearest(list2,2,1),nearest(list2,1,2))+1
        return list2[i][j]
    elif i==2and j==1:
        list2[i][j]=min(nearest(list2,2,0),nearest(list2,2,2),nearest(list2,1,1))+1
        return list2[i][j]  

list2=[]    
for i in range(0,3):
    tmp=input().split()
    list1=[]
    for j in range(0,3):
        tmp[j]=int(tmp[j])
        if tmp[j]==0:
            list1.append(0)
        else:
            list1.append(-1)
    list2.append(list1)
print(list2)
print(nearest(list2,1,1))
print(list2)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    