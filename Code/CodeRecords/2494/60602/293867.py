nums=eval(input());
i=0;
count=0;
while(i<len(nums)):
    j=i+1;
    while(j<len(nums)):
        if(nums[i]>2*nums[j]):
            count+=1;
        j+=1;
    i+=1;
print(count);