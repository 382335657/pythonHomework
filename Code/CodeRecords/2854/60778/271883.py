sticks=list(map(int,input().split()))
sticks.sort()
if(sticks[1]==sticks[2] and sticks[2]==sticks[3] and sticks[3]==sticks[4]):
    print("Bear")
elif(sticks[0]==sticks[1] and sticks[1]==sticks[2] and sticks[2]==sticks[3] and sticks[4]==sticks[5]):
    print("Elephant")
elif(sticks[0]==sticks[1] and sticks[1]==sticks[2] and sticks[2]==sticks[3] and sticks[4]<sticks[5]):
    print("Bear")
else:
    print("Alien")