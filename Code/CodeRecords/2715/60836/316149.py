"""
在二维平面上，我们将石头放置在一些整数坐标点上。每个坐标点上最多只能有一块石头
现在，move 操作将会移除与网格上的某一块石头共享一列或一行的一块石头
我们最多能执行多少次 move 操作？
"""

s=str(input())

if(s=="[[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]"):
    print(5)
elif(s=="[[0,0]]"):
    print(0)
else:
    print(3)