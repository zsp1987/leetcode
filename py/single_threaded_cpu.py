import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(v[0], v[1], i) for i, v in enumerate(tasks)] # start_time, duration, task_num
        tasks.sort()
        res = []
        cur_time = 0
        task_idx = 0
        task_queue = []

        while task_idx < len(tasks) or task_queue:
            if not task_queue and cur_time < tasks[task_idx][0]:
                cur_time = tasks[task_idx][0]
            
            while task_idx < len(tasks) and cur_time >= tasks[task_idx][0]:
                _, duration, task_num = tasks[task_idx]
                heapq.heappush(task_queue, (duration, task_num))
                task_idx += 1
            
            duration, task_num = heapq.heappop(task_queue)
            cur_time += duration
            res.append(task_num)

        return res