import collections


class LFUCache(object):
    """
    :leetcode: 460
    :url: https://leetcode.com/problems/lfu-cache/
    """

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._capacity = capacity
        self._size = 0
        self._minfreq = 0
        self._nodes = dict()
        self._freqs = collections.defaultdict(DLinkedList)

    def _update(self, node):
        freq = node.freq
        self._freqs[freq].pop(node)
        if self._minfreq == freq and not self._freqs[freq]:
            self._minfreq += 1

        node.freq += 1
        self._freqs[node.freq].append(node)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self._nodes:
            return -1
        node = self._nodes[key]
        self._update(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self._capacity == 0:
            return

        if key in self._nodes:
            node = self._nodes[key]
            self._update(node)
            node.val = value
        else:
            if self._size == self._capacity:
                node = self._freqs[self._minfreq].pop()
                del self._nodes[node.key]
                self._size -= 1

            node = Node(key, value)
            self._nodes[key] = node
            self._freqs[1].append(node)
            self._minfreq = 1
            self._size += 1


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None


class DLinkedList:
    def __init__(self):
        self._sential = Node(None, None)  # dummy
        # ! sential is both first and last of the list :O
        self._sential.next = self._sential.prev = self._sential
        self._size = 0

    def __len__(self):
        return self._size

    def append(self, node):
        node.next = self._sential.next
        node.prev = self._sential
        node.next.prev = node
        self._sential.next = node
        self._size += 1

    def pop(self, node=None):
        if self._size == 0:
            return

        if not node:
            node = self._sential.prev

        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1

        return node
