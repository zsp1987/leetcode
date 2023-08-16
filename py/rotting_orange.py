import collections


class Solution(object):
    """
    leetcode 994 https://leetcode.com/problems/rotting-oranges/
    """
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        count = 0  # orange count
        rotted = 0
        q = collections.deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                    rotted += 1
                    count += 1
                elif grid[r][c] == 1:
                    count += 1

        if count == 0:
            return 0

        round = 0
        while q:
            if rotted == count:
                return round
            round += 1
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                for ri, ci in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    nr = r + ri
                    nc = c + ci

                    if nr >= 0 and nr < m and nc >= 0 and nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        rotted += 1
                        q.append((nr, nc))

        return -1
