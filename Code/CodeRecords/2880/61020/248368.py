s = input()
n = int(s[0:1])
k = int(s[2:3])

'''
8 4
4 2 3 1 5 1 6 4'''

weight_list = input().split()

for i in range(0, len(weight_list)):
    weight_list[i] = int(weight_list[i])

left_index = 0
while weight_list[left_index] <= k:
    left_index += 1

right_index = len(weight_list) - 1
while weight_list[right_index] <= k:
    right_index -= 1

print(n - (right_index - left_index + 1))