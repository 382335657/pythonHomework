def chufa(divended,divisor):
    i=divended
    j=0
    if(divended*divisor<0):
        if(divended<0):
            i=-i
        if(divisor<0):
            divisor=-divisor
            while(i>=divisor):
                i=i-divisor
                j=j+1
        print(0-j)
        return
    while(i>=divisor):
        i=i-divisor
        j=j+1
    print(j)
chufa(s,t)