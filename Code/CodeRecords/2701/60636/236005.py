board=[[["a"],["a"],["a"]],[["a"],["a"],["a"]],[["a"],["a"],["a"]]]
source=input("")[1:-1]
list=[]
for i in range(int((len(source)+1)/6)):
    list.append(source[6*i:6*i+5][1:-1].split(","))
if(len(list)%2==0):
    for i in range(int(len(list)/2)):
        board[int(list[2*i][0])][int(list[2*i][1])]="X"
        board[int(list[2*i+1][0])][int(list[2*i+1][1])]="O"
else:
    board[int(list[0][0])][int(list[0][1])]="X"
    list.pop(0)
    for i in range(int(len(list)/2)):
        board[int(list[2*i][0])][int(list[2*i][1])]="O"
        board[int(list[2*i+1][0])][int(list[2*i+1][1])]="X"
for i in range(3):
    if((board[i][0]==board[i][1])&(board[i][0]==board[i][2])&(board[i][2]==board[i][1])):
        if(board[i][0]=="X"):
            print("A")
        else:
            print("B")
    elif((board[0][i]==board[1][i])&(board[0][i]==board[2][i])&(board[1][i]==board[2][i])):
        if(board[0][i]=="X"):
            print("A")
        else:
            print("B")
    elif(