from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while end - start > 1:
            mid = start + (end - start) // 2
            if nums[mid + 1] > nums[mid]:
                if nums[end] < nums[mid]:
                    start = mid + 1
                else:
                    end = mid
            else:
                start = mid + 1

        return nums[start] if nums[start] < nums[end] else nums[end]
