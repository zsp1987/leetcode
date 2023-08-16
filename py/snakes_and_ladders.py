class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        row = len(board)
        step = 0
        queue = deque()
        queue.append(1)
        visited = {}

        while queue:
            step += 1
            for i in range(len(queue)):
                pos = queue.popleft()
                for n in range(6):
                    next_pos = pos + n + 1
                    r = row - 1 - int((next_pos - 1) / row)
                    c = (next_pos - 1) % row if int((next_pos - 1) / row) % 2 == 0 else row -1 -((next_pos - 1) % row)
                    if board[r][c] != -1:
                        next_pos = board[r][c]
                    if next_pos >= row * row:
                        return step
                    if next_pos not in visited:
                        visited[next_pos] = True
                        queue.append(next_pos)

        return -1