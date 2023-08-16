import heapq
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        pq = []
        for i in range(n):
            heapq.heappush(pq, (0, i, 0)) # endtime, room#, count
        
        for m in meetings:
            while pq[0][0] < m[0]:
                next_room = heapq.heappop(pq)
                heapq.heappush(pq, (m[0], next_room[1], next_room[2]))
            next_room = heapq.heappop(pq)
            next_end = m[1] if m[0] >= next_room[0] else m[1] - m[0] + next_room[0]
            heapq.heappush(pq, (next_end, next_room[1], next_room[2]+1))
        
        pq.sort(key=lambda x: (-x[2], x[1]))
        return pq[0][1]
    
s = Solution()
s.mostBooked(4, [[18,19],[3,12],[17,19],[2,13],[7,10]])
    
    