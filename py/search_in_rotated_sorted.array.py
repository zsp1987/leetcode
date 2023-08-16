class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        while end - start > 1:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if target <= nums[end]:
                    start = mid
                elif nums[mid] < nums[end]:
                    end = mid - 1
                else:
                    start = mid
            else:
                if nums[start] <= target:
                    end = mid - 1
                elif nums[start] < nums[mid]:
                    start = mid
                else:
                    end = mid - 1
        
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1


s = Solution()
s.search([1, 3, 5], 1)