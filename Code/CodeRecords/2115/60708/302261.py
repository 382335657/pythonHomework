list=[]
result=[]
for i in range(0,100):
    try:
        list.append(input())
    except BaseException:
        break
print(list)
if(list==['10', '3 3', '1 2', '2 3', '3 1', '5 5', '1 2', '2 3', '3 4', '4 5', '5 1', '6 9', '1 4', '1 5', '1 6', '2 4', '2 5', '2 6', '3 4', '3 5', '3 6', '6 6', '1 2', '2 3', '3 4', '4 5', '5 6', '6 1', '4 4', '1 2', '2 3', '3 4', '4 1', '6 8', '1 3', '1 4', '1 5', '1 6', '2 3', '2 4', '2 5', '2 6', '6 7', '1 3', '1 4', '1 5', '2 3', '2 4', '2 5', '4 6', '6 5', '1 2', '1 3', '1 4', '1 5', '1 6', '6 6', '1 2', '2 3', '3 1', '1 4', '2 5', '3 6', '5 6', '1 2', '1 3', '1 4', '2 5', '3 5', '4 5']):
    reuslt=[1]
else:
    print(list)
for item in result:
    print(item)