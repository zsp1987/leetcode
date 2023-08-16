import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg_nums = [-i for i in nums]
        heapq.heapify(neg_nums)
        for _ in range(k):
            res = heapq.heappop(neg_nums)
        return -res