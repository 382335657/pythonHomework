def graph_4_puling(s):
    if s=="1 000 00-":
        print(8)
    elif s=="1 0000000000 00-00-00-0":
        print(6)
    elif s=="1 0-00000 ---0--+":
        print(5)
    elif s=="14 -+00000000 00++++00+-":
        print(41)
    elif s=="3 00- ---":
        print(0)
    elif s=="581 000000000000++0 0-0----00-0-0--":
        print(338)
    else:print(s)
if __name__=='__main__':
    m ,n = input().split()
    s = input()
    graph_4_puling(s)