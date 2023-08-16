class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = head
        count = 0
        prev = ListNode(0, head)
        prev_start = prev
        while fast != None:
            if count >= n:
                prev = prev.next
            count += 1
            fast = fast.next
        prev.next = prev.next.next
        return prev_start.next


class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next
