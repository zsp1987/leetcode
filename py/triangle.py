"""
leetcode 120 https://leetcode.com/problems/triangle/
"""

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        level = len(triangle)
        if level == 1:
            return triangle[0][0]
        count = (1+level)*level / 2
        dp = [0] * count
        dp[0] = triangle[0][0]
        min_sum = float("inf")
        row_sum = 0
        for row in range(level):
            for col in range(row+1):
                if row == 0:
                    continue
                i = row_sum + col
                value = triangle[row][col]
                upper = float("inf") if col == row else dp[i - row]
                upper_left = float("inf") if col == 0 else dp[i - row - 1]
                dp[i] = min(value + upper, value + upper_left)
                if row == level -1:
                    min_sum = min(min_sum, dp[i])
            row_sum += (row + 1)

        return min_sum