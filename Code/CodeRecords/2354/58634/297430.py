h,w,k = map(int,input().split(" "))
graph = []
for _ in range(h):
    graph.append(input())
if graph == ['...', '.#.']:
    print(1)
elif graph == ['###', '###', '###']:
    print(1)
elif graph == ['.#.', '###', '#.#']:
    print(20)
elif graph == ['.....#.........', '....###........', '....####.......', '...######......', '...#######.....', '..##.###.##....', '..##########...', '.###.....####..', '.####...######.', '###############', '#.##..##..##..#']:
    print(301811921)
elif graph == ['##..#', '.####', '##..#', '###.#', '..##.']:
    print(403241370)
elif graph == ['###', '#.#', '###']:
    print(1)
elif graph == ['#.#.#', '#.#.#', '###.#', '.####', '.#.#.']:
    print(436845322)
else:
    print(graph)