beginWord = input()
endWord = input()
wordList = eval(input())

wordList = set(wordList)
res, visited, forward, backward, _len = [], set(), {beginWord: [[beginWord]]}, {endWord: [[endWord]]}, 2
while forward:
    if len(forward) > len(backward): 
        forward, backward = backward, forward
    tmp = {} 
    while forward:
        word, paths = forward.popitem() 
        visited.add(word) 
        for i in range(len(word)):
            for a in 'abcdefghijklmnopqrstuvwxyz':
                new = word[:i]+a+word[i+1:] 
                if new in backward: 
                    if paths[0][0] == beginWord:
                        res.extend(fPath + bPath[::-1] for fPath in paths for bPath in backward[new])
                    else:  
                        res.extend(bPath + fPath[::-1] for fPath in paths for bPath in backward[new])
                if new in wordList and new not in visited:
                    tmp[new] = tmp.get(new, []) + [path + [new] for path in paths]
    _len += 1
    if res and _len > len(res[0]):
        break
    forward = tmp
    
if endWord not in wordList:
    print(0)
else:
    print(len(res[0]))