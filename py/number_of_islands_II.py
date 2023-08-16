from typing import List


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        size = m * n
        lands = [[0] * n] * m
        union_find = UnionFind(size)
        results = []
        for pos in positions:
            row, col = pos
            lands[row][col] = 1
            point = row * n + col
            if union_find.add(point):
                for step in ((0,-1), (-1, 0), (0, 1), (1, 0)):
                    next_row = row + step[0]
                    next_col = col + step[1]

                    if next_row >= 0 and next_row < m and next_col >= 0 \
                        and next_col < n and lands[next_row][next_col] == 1:
                        next_point = next_row * n + next_col
                        union_find.union(point, next_point)
            results.append(union_find.total)
        return results
                
            
class UnionFind:
    def __init__(self, size):
        self.parents = [-1] * size
        self.rank = [0] * size
        self.total = 0

    def add(self, x):
        if self.parents[x] != -1:
            return False
        self.parents[x] = x
        self.total += 1
        return True

    def find(self, x):
        if self.parents[x] == -1:
            return -1
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == -1 or y_root == -1 or x_root == y_root:
            return
        
        self.total -= 1

        if self.rank[x_root] < self.rank[y_root]:
            self.parents[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parents[y_root] = x_root
        else:
            self.parents[x_root] = y_root
            self.rank[y_root] += 1 