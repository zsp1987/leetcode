import collections

class Solution(object):
    """
    leetcode 542 https://leetcode.com/problems/01-matrix/
    """
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])

        dist = [[-1] * n for _ in range(m)]
        count = 0
        q = collections.deque()

        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    dist[row][col] = 0
                    count += 1
                    q.append((row, col))

        while q and count < n * m:
            row, col = q.popleft()
            for ri, ci in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_row = row + ri
                next_col = col + ci
                if next_row >= 0 and next_row < m and next_col >= 0 \
                        and next_col < n and dist[next_row][next_col] < 0:
                    dist[next_row][next_col] = dist[row][col] + 1
                    count += 1
                    q.append((next_row, next_col))

        return dist
