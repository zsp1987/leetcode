import heapq


class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        row, col = len(heights), len(heights[0])
        queue = [(0, 0, 0)]
        visited = [[False] * col for _ in range(row)]
        max_effort = 0

        while queue:
            effort, r, c = heapq.heappop(queue)
            visited[r][c] = True
            max_effort = max(effort, max_effort)

            if r == row - 1 and c == col - 1:
                return max_effort
            
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < row and 0 <= nc < col and not visited[nr][nc]:
                    next_effort = abs(heights[nr][nc] - heights[r][c])
                    heapq.heappush(queue, (next_effort, nr, nc))
                

        return max_effort