class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        :leetcode: 22
        :url: https://leetcode.com/problems/generate-parentheses/
        """
        res = []
        self.dfs(res, n, 0, 0, 0, '')
        return res

    def dfs(self, res, n, count, left, right, s):
        if left < right or left > n:
            return

        if count == 2 * n:
            res.append(s)
            return

        self.dfs(res, n, count + 1, left + 1, right, s + '(')
        self.dfs(res, n, count + 1, left, right + 1, s + ')')
