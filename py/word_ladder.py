
import collections
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        que = collections.deque()
        que.append((beginWord, 1))
        while que:
            word, length = que.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordSet:
                        wordSet.remove(next_word)
                        que.append((next_word, length+1))
        return 0
        
s = Solution()
# s.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"])
# s.findLadders("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"])