def f(s,t):
    m=0
    for i in range(0,len(s)):
        for j in range(i+1,len(s)+1):
            m+=t.count(s[i:j])
    return m

print(f(input().strip(),input().strip()),end='')