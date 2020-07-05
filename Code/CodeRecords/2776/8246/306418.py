class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_end = False


class Trie:
    def __init__(self, word_list):
        self.root = TrieNode()
        for word in word_list:
            if word:
                self.insert(word)

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.child:
                node.child[w] = TrieNode()
            node = node.child[w]
        node.is_end = True


class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        t = Trie(words)
        res = []

        def dfs(node, i, w, has_cut):
            if i == len(w):
                return node.is_end and has_cut
            if node.is_end:
                if dfs(t.root, i, w, True):
                    return True

            if w[i] not in node.child:
                return False
            else:
                return dfs(node.child[w[i]], i + 1, w, has_cut)

        for w in words:
            if dfs(t.root, 0, w, False):
                res.append(w)
        return res
if __name__ == '__main__':
    data =input()
    data=eval(data)
    s1 = Solution()
    print(s1.findAllConcatenatedWordsInADict(data))