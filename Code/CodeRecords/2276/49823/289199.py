def do(R,C,r0,c0):
    out=[[r0,c0]]
    for i in range(1,(max([r0,c0,R-r0-1,C-c0-1])+1)*2):
        add=i%2==1
        for j in range(i):
            c0+=1 if add else -1
            if (add and c0>=C) or (not add and c0<0):
                c0+=i-j-1 if add else -(i-j-1)
                break
            if r0>=0 and r0<R and c0>=0 and c0<C:
                out.append([r0,c0])
        for j in range(i):
            r0+=1 if add else -1
            if (add and r0>=R) or (not add and r0<0):
                r0+=i-j-1 if add else -(i-j-1)
                break
            if r0>=0 and r0<R and c0>=0 and c0<C:
                out.append([r0,c0])
    print(out)
if __name__ == '__main__':
    do(int(input()),int(input()),int(input()),int(input()))
