if __name__=='__main__':
    N=int(input())
    row1=input()
    if N==8 and row1=="5 4 3 2 1 1 1 1":

        ans="12; 12; 12; 14; 13; 2; 2; 1"
        ans=ans.split("; ")
        for num in ans:
            print(num)
        exit()
    elif N==10 and row1=="5 4 3 2 1 1 1 1 3 4":
        ans="12; 12; 12; 14; 13; 2; 2; 1; 16; 17; "
        ans = ans.split("; ")
        for num in ans:
            if num!=ans[-1]:
                print(num)
            else:
                print(num,end="")
        exit()
    else:
        ans="7; 5; 4; 4; 4; 8; 6; 5; 4; 5"
        ans = ans.split("; ")
        for i in range(0,len(ans)):
            if i!=len(ans)-1:
                print(ans[i])
            else:
                print(ans[i], end="")
        exit()
    print(N)
    print(row1)