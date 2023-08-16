class Solution(object):
    """
    leetcode 695 https://leetcode.com/problems/max-area-of-island/
    """

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        self.res = 0
        global_visited = set()

        def dfs(row, col, visited):
            if  row < 0 or row >= m or col < 0 or col >= n or \
                    grid[row][col] != 1 or (row, col) in visited or (row, col) in global_visited:
                return
            visited.add((row, col))
            global_visited.add((row, col))
            self.res = max(self.res, len(visited))
            dfs(row + 1, col, visited)
            dfs(row - 1, col, visited)
            dfs(row, col + 1, visited)
            dfs(row, col - 1, visited)

        for r in range(m):
            for c in range(n):
                dfs(r, c, set())

        return self.res