def exam5():
    i=input().split(" ")
    i.remove("0")
    i.sort(reverse=True)
    string=i[0]
    for j in range(1,len(i)):
        string=string+" "+i[j]
    print(string)
exam5()