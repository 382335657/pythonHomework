import math


binary = input()
bout = 0
ternary = input()
tout = 0
out = 0
for i in range(len(binary)):
    bout = bout*2+int(binary[i])
for i in range(len(ternary)):
    tout = tout*3+int(ternary[i])
#print(bout,tout)
diff = tout-bout
for i in range(1+max(int(math.log(bout,2)),int(math.log(tout,2)))):
    temp = math.log(3,abs(diff-math.pow(2,i)))
    if(math.log(abs(diff-math.pow(2,i)),3)%1==0):
        out = bout+math.pow(2,i)
    elif(math.log(abs(diff+math.pow(2,i)),3)%1==0):
        out = bout-math.pow(2,i)
print(int(out))