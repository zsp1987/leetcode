import heapq


class Solution(object):
    def assignBikes(self, workers, bikes):
        def dist(w, b):
            return abs(workers[w][0] - bikes[b][0]) + abs(workers[w][1]- bikes[b][1])
        h = [(0,0,0)]
        visited = set()

        while True:
            cost, w, b_taken = heapq.heappop(h)
            if (w, b_taken) in visited: continue
            visited.add((w, b_taken))
            if w == len(workers):
                return cost
            for b in range(len(bikes)):
                if b_taken & (1 << b) == 0:
                    heapq.heappush(h, [cost + dist(w, b), w + 1, b_taken | (1 << b)])