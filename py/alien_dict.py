import collections
from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = collections.defaultdict(set)
        indegree = collections.Counter({c : 0 for word in words for c in word})

        for cur_word, next_word in zip(words, words[1:]):            
            for c0, c1 in zip(cur_word, next_word):
                if c0 != c1:
                    if c1 not in graph[c0]:
                        graph[c0].add(c1)
                        indegree[c1] += 1
                    break
            else:
                if len(next_word) < len(cur_word): return ""

        result = ""
        deque = collections.deque()
        for key in indegree.keys():
            if indegree[key] == 0:
                deque.append(key)


        while deque:
            key = deque.popleft()
            result += key
            for next_key in graph[key]:
                indegree[next_key] -= 1
                if indegree[next_key] == 0:
                    deque.append(next_key)

        if len(result) < len(indegree.keys()):
            return ""
        return result

s = Solution()
print(s.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
