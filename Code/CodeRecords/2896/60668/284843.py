def strings_10_noname(str1,str2):
    pd = 0
    for i in range(len(str2)):
        if str2[i]!=' ':
            pd = str1.find(str2[i])
            if pd == -1:
                return "NO"
            else:
                str1 = str1.replace(pd, " ")
    return "YES"
if __name__=='__main__':
    str1 = input()
    str2 = input()
    print(strings_10_noname(str1,str2))