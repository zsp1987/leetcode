class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        po, ao = [], []
        for r in range(row):
            po.append([0]*col)
            ao.append([0]*col)

        result = []
        for r in range(row):
            self.dfs(heights, po, r, 0)
            self.dfs(heights, ao, r, col - 1)
        
        for c in range(col):
            self.dfs(heights, po, 0, c)
            self.dfs(heights, ao, row - 1, c)

        for r in range(row):
            for c in range(col):
                if po[r][c] == 1 and ao[r][c] == 1:
                    result.append([r, c])
        return result
    
    def dfs(self, heights, visited, r, c):
        visited[r][c] = 1
        for step in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r + step[0], c + step[1]
            if nr >= 0 and nr < len(heights) and nc >= 0 and nc < len(heights[0]):
                if visited[nr][nc] == 0 and heights[nr][nc] >= heights[r][c]:
                    self.dfs(heights, visited, nr, nc)