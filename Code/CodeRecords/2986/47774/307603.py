a=str(input())
b=str(input())
matrix=[[0 for i in range(len(a)+1)] for i in range(len(b)+1)]
matrix[0][0]=0
for i in range(1,len(a)+1):
    matrix[0][i]=i
for i in range(1,len(b)+1):
    matrix[i][0]=i
for i in range(1,len(b)+1):
    for j in range(1,len(a)+1):
        temp=''
        if a[j-1] ==b[i-1]:
            temp=matrix[i-1][j-1]
        else:
            temp=matrix[i-1][j-1]+1
        matrix[i][j]=min(min(matrix[i-1][j]+1,matrix[i][j-1]+1),temp)
print(matrix[len(b)][len(a)])
    