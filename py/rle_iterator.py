class RLEIterator(object):
    """
    :leetcode: 900
    :url: https://leetcode.com/problems/rle-iterator/
    """

    def __init__(self, encoding):
        """
        :type encoding: List[int]
        """
        self._idx = 0
        self._encoding = encoding

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while self._idx < len(self._encoding):
            if n <= self._encoding[self._idx]:
                self._encoding[self._idx] -= n
                return self._encoding[self._idx + 1]
            else:
                n -= self._encoding[self._idx]
                self._idx += 2
        return -1


class RLEIteratorNaive(object):

    def __init__(self, encoding):
        """
        :type encoding: List[int]
        """
        self._idx = 0
        self._count = 0
        self._num = None
        self._list = encoding

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n > 0:
            if self._count >= n:
                self._count -= n
                n -= n
            else:
                n -= self._count
                if self._idx >= len(self._list):
                    self._count = 0
                    return -1
                self._count = self._list[self._idx]
                self._idx += 1
                if not self._count == 0:
                    self._num = self._list[self._idx]
                self._idx += 1
        return self._num
