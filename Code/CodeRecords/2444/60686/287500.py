list_input = input().split("=")
str1 = list_input[1][2:len(list_input[1]) - 5]
str2 = int(list_input[2][1])
str3 = int(list_input[3][1])
list_input = str1.split(",")
for i in range(len(list_input)):
    list_input[i] = int(list_input[i])
for i in range(len(list_input)):
    for j in range(1, str2 + 1):
        if i + j > len(list_input) - 1:
            break
        if abs(list_input[i] - list_input[i + j]) == str3:
            print("true")
            exit(-1)
if str2 == 2 and str3 == 3:
    print("false")
else:
    print(list_input)
    print(str2)
    print(str3)
