from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        visited = []
        for r in range(row):
            visited.append([False]*col)
        for r in range(row):
            for c in range(col):
                if self.dfs(board, word, row, col, visited, r, c, 0):
                    return True

        return False

    def dfs(self, board, word, row, col, visited, r, c, level):
        if r < 0 or r > row - 1 or c < 0 or c > col - 1:
            return False
        if visited[r][c]:
            return False
        if level >= len(word):
            return False
        if board[r][c] != word[level]:
            return False
        if level == len(word) - 1:
            return True

        visited[r][c] = True
        result = False

        for step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            result = result or self.dfs(
                board, word, row, col, visited, r + step[0], c + step[1], level + 1)

        visited[r][c] = False
        return result


s = Solution()
s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE")
