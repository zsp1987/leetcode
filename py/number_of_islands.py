from ast import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        row, col = len(grid), len(grid[0])
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    count += 1
                self.visit(grid, r, c, row, col)

        return count

    def visit(self, grid, r, c, row, col):
        if r < 0 or r >= row or c < 0 or c >= col:
            return
        if grid[r][c] == "0":
            return
        
        grid[r][c] = "0"

        for step in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = step
            self.visit(grid, r + nr, c+nc, row, col)
