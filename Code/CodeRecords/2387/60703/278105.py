
in1 = [int(x) for x in input().split()]
n= in1[0]
m = in1[1]
nums= [int(x) for x in input().split()]
moves = []
for i in range(m):
    temp = [int(x) for x in input().split()]
    moves.append(temp)

q = int(input())

for move in moves:
    if(move[0]==0):
        nums[ move[1]-1:move[2]-1 ].sort(reverse=False)
    else:
        nums[ move[1]-1:move[2]-1 ].sort(reverse=True)
print(nums[q-1])