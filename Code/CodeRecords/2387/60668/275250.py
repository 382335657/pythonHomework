def sort_7_local(q,list=[],list_sort=[]):
    for item in list_sort:
        if item[0]==0:
            list = sorted(list[item[1]:item[2]+1])
        elif item[0]==1:
            list = sorted(list[item[1]:item[2] + 1],reverse=True)
    print(list[q])
if __name__=='__main__':
    n,m = input().split()
    list_sort=[]
    list = [int(i) for i in input().split()]
    for _ in range(int(m)):
        list_n = [int(i) for i in input().split()]
        list_sort.append(list_n)
    q = int(input())
    sort_7_local(q,list,list_sort)