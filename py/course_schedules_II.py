import collections
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {idx: [] for idx in range(numCourses)}
        indegree = {idx: 0 for idx in range(numCourses)}
        for p in prerequisites:
            graph[p[1]].append(p[0])
            indegree[p[0]] += 1
        queue = collections.deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        result = []
        while queue:
            course = queue.popleft()
            result.append(course)
            for dependent in graph[course]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    queue.append(dependent)
        if len(result) == numCourses:
            return result
        return []

s = Solution()
print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))