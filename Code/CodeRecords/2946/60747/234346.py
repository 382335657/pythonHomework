s=input()
count=0
for i in range(1,len(s)):
    if s[i]!=s[i-1]:
        count = count + 1
if s[len(s)-1]=='0':
    count = count + 1
print(count,end='')