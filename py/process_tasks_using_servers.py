from collections import deque
import heapq
from typing import List


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        servers = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(servers)

        task_i = 0
        cur_t = 0
        server_seq = []
        task_queue = deque([])
        running_servers = []

        while task_i < len(tasks) or task_queue:
            if not servers:
                cur_t = running_servers[0][0]

            while running_servers and running_servers[0][0] <= cur_t:
                _, server_w, server_i = heapq.heappop(running_servers)
                heapq.heappush(servers, (server_w, server_i))

            while task_i < len(tasks) and task_i <= cur_t:
                task_queue.append(tasks[task_i])
                task_i += 1

            while servers and task_queue:
                next_serv_w, next_serv_i = heapq.heappop(servers)
                next_t = task_queue.popleft()
                server_seq.append(next_serv_i)
                heapq.heappush(running_servers,
                               (cur_t + next_t, next_serv_w, next_serv_i))

            cur_t += 1

        return server_seq
