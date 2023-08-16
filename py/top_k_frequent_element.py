import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1

        pq = []
        for key, value in count.items():
            heapq.heappush(pq, (-value, key))

        res = []
        for i in range(k):
            res.append(heapq.heappop(pq)[1])
        return res
