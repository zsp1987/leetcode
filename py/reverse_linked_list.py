class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None

        self.new_head = None

        def recurse(head):
            if head.next == None:
                self.new_head = head
                return head

            next_node = recurse(head.next)
            next_node.next = head
            head.next = None
            return head

        recurse(head)
        return self.new_head

node_1 = ListNode(1)
node_2 = ListNode(2)
node_1.next = node_2

s = Solution()
s.reverseList(node_1)

