s = input()
if s == "25" * (len(s) // 2):
    print(1)
    exit()
cnt = 0
tmp = ""
i = 0
while i != len(s) - 2:
    if s[i] == "2":
        if s[i+1] != "5":
            i += 1
        else:
            tmp += "25"
            i += 2
    else:
        if tmp != "":
            i += 1
            cnt += 1
            tmp = ""

        
print(cnt)
