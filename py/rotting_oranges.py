class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])

        fresh_count = 0
        rotten_queue = deque()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh_count += 1
                if grid[r][c] == 2:
                    rotten_queue.append((r, c))
        
        if not rotten_queue and not fresh_count:
            return 0

        level = 0

        while rotten_queue:
            level = level + 1
            count = len(rotten_queue)
            for i in range(count):
                r, c = rotten_queue.popleft()
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if nr >= 0  and nr <= row - 1 and nc >= 0 and nc <= col - 1:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh_count -= 1
                            rotten_queue.append((nr, nc))
            
        if fresh_count == 0:
            return level - 1
        return -1