from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        node = dummy
        while l1 and l2:
            sum_v = l1.val + l2.val + carry
            new_node = ListNode()
            if sum_v >= 10:
                new_node.val = sum_v - 10
                carry = 1
            else:
                new_node.val = sum_v
                carry = 0
            l1 = l1.next
            l2 = l2.next
            node.next = new_node
            node = new_node

        while l1:
            sum_v = l1.val + carry
            new_node = ListNode()
            if sum_v >= 10:
                new_node.val = sum_v - 10
                carry = 1
            else:
                new_node.val = sum_v
                carry = 0
            l1 = l1.next
            node.next = new_node
            node = new_node

        while l2:
            sum_v = l2.val + carry
            new_node = ListNode()
            if sum_v >= 10:
                new_node.val = sum_v - 10
                carry = 1
            else:
                new_node.val = sum_v
                carry = 0
            l2 = l2.next
            node.next = new_node
            node = new_node

        if carry:
            new_node = ListNode()
            new_node.val = 1
            node.next = new_node

        return dummy.next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
