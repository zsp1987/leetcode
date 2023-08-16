import collections

class MyHashSet(object):
    def __init__(self):
        self._key_range = 997
        self._buckets = [collections.deque() for i in range(self._key_range)]

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        idx = self._hash(key)
        if key not in self._buckets[idx]:
            self._buckets[idx].append(key)

    def _hash(self, n):
        return n % self._key_range

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        idx = self._hash(key)
        if key in self._buckets[idx]:
            self._buckets[idx].remove(key)

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        idx = self._hash(key)
        return key in self._buckets[idx]
