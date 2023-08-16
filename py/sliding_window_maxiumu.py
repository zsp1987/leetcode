from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums
        
        def clean_deque(i):
            if dq and dq[0] == i - k:
                dq.popleft()
            
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
        
        dq = deque() # mono decrease queue with idx numbers
        max_i = 0

        for i in range(k):
            clean_deque(i)
            dq.append(i)
            if nums[i] > nums[max_i]:
                max_i = i
        
        output = [nums[max_i]]

        for i in range(k, n):
            clean_deque(i)
            dq.append(i)
            output.append(nums[dq[0]])

        return output