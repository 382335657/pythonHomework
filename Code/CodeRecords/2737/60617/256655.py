def findMode():
    array=list(eval(input()))
    modeStandard=len(array)//3
    array.sort()
    count=1
    mode = []
    for i in range(0, len(array)):
        if count>modeStandard:
            mode.append(array[i])
        
        if i!=len(array)-1 and array[i]==array[i+1]:
            count+=1
            continue
        else:
            count=1
    print(mode)

if __name__=='__main__':
    findMode()



