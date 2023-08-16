class Solution(object):
    """
    :leetcode: 283 https://leetcode.com/problems/move-zeroes/
    """

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        def swap(a, b):
            tmp = nums[a]
            nums[a] = nums[b]
            nums[b] = tmp

        l = 0
        c = 0

        while c < len(nums):
            if nums[c] != 0:
                swap(c, l)
                l += 1
            c += 1
