str1=input()
str1=str1.strip("[")
str1=str1.strip("]")
nums=list(map(int,str1.split(",")))
nums=sorted(nums)
print(nums)