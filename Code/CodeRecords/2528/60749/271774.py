str1=input()
str1=str1.strip("[")
str1=str1.strip("]")
nums=list(map(int,input().split(",")))
nums=sorted(nums)
print(nums)