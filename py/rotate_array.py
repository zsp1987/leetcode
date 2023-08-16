class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        shift = k % length
        bak = nums[-shift:]

        i = length - 1 - shift
        while i >= 0:
            nums[i + shift] = nums[i]
            i -= 1

        j = 0
        while j < shift:
            nums[j] = bak[j]
            j += 1
