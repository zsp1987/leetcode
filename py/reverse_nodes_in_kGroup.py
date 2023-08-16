class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None

        if k == 1:
            return head

        return self.recurse(head, k)

    def recurse(self, node, k):
        has_k = True
        head_node = node
        for i in range(k-1):
            if head_node == None:
                has_k = False
                break
            head_node = head_node.next
        if head_node == None:
            has_k = False
        if not has_k:
            return node
        else:
            next_head = self.recurse(head_node.next, k)
            head_node.next = None
            self.reverse(node)
            node.next = next_head
            return head_node

    def reverse(self, node):
        prev = None
        while node.next:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        node.next = prev
        return node
