if __name__=='__main__':
    n = int(input())
    list = [int(i) for i in input().split(',')]
    co = []
    re = 0
    con = 0
    for i in range(len(list)):
        con = list[i]
        re = 1
        if(con>=n):
            co.append(1)
            break
        else:
            for j in range(i+1,len(list)):
                if(con + list[j] <=n):
                    re += 1
                    con += list[j]
                else:
                    co.append(re)
    print(min(co))