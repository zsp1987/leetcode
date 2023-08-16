import heapq


class MedianFinder(object):

    def __init__(self):
        self._max_heap = []  # smaller side
        self._min_heap = []  # bigger side

    def addNum(self, num):
        if len(self._max_heap) < len(self._min_heap):
            heapq.heappush(self._max_heap, -heapq.heappushpop(self._min_heap, -num))
        else:
            heapq.heappush(self._min_heap, -heapq.heappushpop(self._max_heap, num))

    def findMedian(self):
        if len(self._max_heap) == len(self._min_heap):
            return (self._max_heap[0] - self._min_heap[0]) / 2.0
        else:
            return -self._min_heap[0]
