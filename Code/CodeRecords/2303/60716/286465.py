def dychoose(string:str,List:list):
    print("after op: {}".format(string))
    if len(List)==0:
        possible.append(string)
        print("return")
        return 
    if (string[-num+1:]+'0' not in List and string[-num+1:]+'1' not in List): 
        possible.append(string)
        print("return")
        return
    temp0 = string[-num+1:]+'0'
    if temp0 in List:
        print("operate: {}".format(temp0))
        temp_0 = List.copy()
        temp_0.remove(temp0)
        dychoose(string+'0',temp_0)
    temp1 = string[-num+1:]+'1'
    if temp1 in List:
        print("operate: {}".format(temp1))
        temp_1 = List.copy()
        temp_1.remove(temp1)
        dychoose(string+'1',temp_1)

num = int(input())
m = 2**num
lists = [bin(i).replace('0b','0'*num)[-num:] for i in range(m)]
strs = ''
possible = list()
strs = strs +lists[0]
lists.pop(0)
dychoose(strs,lists)
possible.sort()
print("{} {}".format(m,possible[0]))