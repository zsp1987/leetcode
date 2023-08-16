class Solution(object):
    solution_count = 0
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        visited = [False] * (n + 1)
        self.check_solution(1, n, visited)
        return self.solution_count

    def check_solution(self, index, n, visited):
        if index > n:
            self.solution_count += 1
            return
        for i in range(1, n+1):
            if not visited[i] and (i % index == 0 or index % i == 0):
                visited[i] = True
                self.check_solution(index+1, n, visited)
                visited[i] = False
