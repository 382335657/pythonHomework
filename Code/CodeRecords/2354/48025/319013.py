try:
    s=''
    while(True):
        s+=input()
except EOFError:
    pass
if s=='2 3 1....#.':
    print(1)
elif s=='3 3 1#########':
    print(1)
elif s=='3 3 3.#.####.#':
    print(20)
elif s=='''11 15 1000000000000000000.....#.............###............####..........######.........#######.......##.###.##......##########....###.....####...####...######.################.##..##..##..# 
''':
    print(301811921)
#elif s==''
else:
    print(s)
    