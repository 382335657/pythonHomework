string=raw_input();
list0=string.split();
string1=list0[0];
string2=list0[1];
list1=list(string1);
list2=list(string2);
i=0;
while(list1[i]==list2[i]):
    i+=1;
print(ord(list1[i])-ord(list2[i]));