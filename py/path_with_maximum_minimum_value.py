import heapq


class Solution(object):
    def maximumMinimumPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        heap = []
        ans = grid[0][0]

        visited = [[False] * n for _ in range(m)]

        heapq.heappush(heap, (-ans, 0, 0))
        visited[0][0] = True

        while heap:
            _, cur_r, cur_c = heapq.heappop(heap)
            ans = min(ans, grid[cur_r][cur_c])

            if cur_r == m - 1 and cur_c == n - 1:
                break
            for nr, nc in ((cur_r + 1, cur_c), (cur_r - 1, cur_c), \
                            (cur_r, cur_c + 1), (cur_r, cur_c - 1)):
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    heapq.heappush(heap, (-grid[nr][nc], nr,nc))
                    visited[nr][nc] = True
    
        return ans
    

# union find
class Solution(object):
    def maximumMinimumPath(self, grid):
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x != root_y:
                if rank[root_x] > rank[root_y]:
                    root[root_y] = root_x
                elif rank[root_x] < rank[root_y]:
                    root[root_x] = root_y
                else:
                    root[root_y] = root_x
                    rank[root_x] += 1
        
        R, C = len(grid), len(grid[0])
        dirs = ((-1, 0), (1, 0), (0,1), (0,-1))
        rank = [1] * (R * C)
        root = list(range(R * C))
        visited = [[False] * C for _ in range(R)]

        vals = [(row, col) for row in range(R) for col in range(C)]
        vals.sort(key = lambda x: grid[x[0]][x[1]], reverse = True)

        for r, c in vals:
            cur_pos = r * C + c
            visited[r][c] = True
            for d_r, d_c in dirs:
                nr = r + d_r
                nc = c + d_c
                new_pos = nr * C + nc
                if 0 <= nr < R and 0 <= nc < C and visited[nr][nc]:
                    union(cur_pos, new_pos)

                if find(0) == find(R*C - 1):
                    return grid[r][c]
        
        return -1