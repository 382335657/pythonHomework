from collections import defaultdict
from collections import deque
bg=input()
eg=input()
l=eval(input())
def ladderLength(beginWord, endWord, wordList):
    size, general_dic = len(beginWord), defaultdict(list)
    for w in wordList:
        for _ in range(size):
            general_dic[w[:_] + "*" + w[_ + 1:]].append(w)
    # BFS
    queue = deque()
    queue.append((beginWord, 1))  
    mark_dic = defaultdict(bool)  # bool 的默认值是false，因此所有不在list里的是false
    mark_dic[beginWord] = True
    while queue:
        cur_word, level = queue.popleft()  # queue头出来一个
        for i in range(size):  # 找邻居，这里的所有邻居都在level+1层
            for neighbour in general_dic[cur_word[:i] + "*" + cur_word[i + 1:]]:
                if neighbour == endWord: return level + 1
                if not mark_dic[neighbour]:
                    mark_dic[neighbour] = True
                    queue.append((neighbour, level + 1))  
    return 0
print(ladderLength(bg,eg,l))