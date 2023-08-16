class PeekingIterator(object):
    """
    :leetcode: 284
    :url: https://leetcode.com/problems/peeking-iterator/
    """

    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._peek = None
        self._iterator = iterator

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self._peek:
            return self._peek
        val = self._iterator.next()
        self._peek = val
        return val

    def next(self):
        """
        :rtype: int
        """
        if self._peek:
            val = self._peek
            self._peek = None
            return val
        return self._iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self._peek:
            return True
        return self._iterator.hasNext()
