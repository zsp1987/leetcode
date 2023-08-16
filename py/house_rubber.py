"""
leetcode 198 https://leetcode.com/problems/house-robber/
"""


class TopDown(object):
    def __init__(self):
        self.memo = {}

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return self.rob_helper(nums, n - 1)

    def rob_helper(self, nums, n):
        if n == 0:
            res = nums[0]
        elif n == 1:
            res = max(nums[0], nums[1])
        elif n in self.memo:
            res = self.memo[n]
        else:
            res = max(self.rob_helper(nums, n - 2) + nums[n], \
                      self.rob_helper(nums, n - 1))
        self.memo[n] = res
        return res
