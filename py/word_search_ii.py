from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.num_words = len(words)
        trie = Trie()
        for word in words:
            trie.insert(word)

        row, col = len(board), len(board[0])
        result = []
        for r in range(row):
            for c in range(col):
                self.dfs(board, row, col, trie.root, result, r, c, "")
        return result

    def dfs(self, board, row, col, node, result, r, c, cur_word):
        if self.num_words == 0: return
        if node.is_end_of_word:
            result.append(cur_word)
            node.is_end_of_word = False
            self.num_words -= 1

        if r < 0 or r > row - 1 or c < 0 or c > col - 1:
            return

        tmp = board[r][c]
        node = node.children.get(tmp)
        if not node:
            return

        board[r][c] = "#"
        cur_word = cur_word + tmp

        for step in ((0,1 ),(0,-1),(1,0),(-1,0)):
            self.dfs(board, row, col, node, result, r + step[0], c + step[1], cur_word)
        board[r][c] = tmp


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        current = self.root
        for c in word:
            current = current.children.setdefault(c, TrieNode())
        current.is_end_of_word = True
    
s = Solution()
result = s.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"])
print(result)