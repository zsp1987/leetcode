import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        pq = []

        for i in intervals:
            if pq and pq[0][0] <= i[0]:
                heapq.heappop(pq)
            heapq.heappush(pq, (i[1], i[0]))
        
        return len(pq)