if __name__ == '__main__':
    import re
    lst = list(map(int,re.findall(r'\d+',input())))
    root = min(lst)
    n = max(lst)
    edges = []
    for i in range(len(lst)//2):
        edges.append([lst[2*i], lst[2*i+1]])
    delete = []
    vertices = []
    for e in edges:
        e_back = e.copy()
        e[0],e[1] = min(e), max(e)
        if e[0] not in vertices:
            vertices.append(e[0])
            vertices.append(e[1])
        else:
            if e[1] not in vertices:
                vertices.append(e[1])
            else:
                delete.append(e_back)
print(delete[-1])