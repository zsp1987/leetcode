from collections import deque


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        queue = deque()
        queue.append((0, 0))
        visited = set()
        visited.add((0, 0))
        level = 0

        while queue:
            level = level + 1
            count = len(queue)
            for i in range(count):
                r, c = queue.popleft()
                if r == n - 1 and c == n - 1:
                    return level
                for nr, nc in ((r + 1, c + 1), (r + 1, c), (r + 1, c - 1), (r, c + 1), (r, c - 1), (r-1, c+1), (r-1, c), (r -1, c-1)):
                    if nr >= 0 and nr <= n - 1 and nc >= 0 and nc <= n -1:
                        if (nr, nc) not in visited and grid[nr][nc] == 0:
                            visited.add((nr, nc))
                            queue.append((nr, nc))


        return -1