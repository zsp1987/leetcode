import collections

class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    """
    leetcode 116 https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
    """
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None:
            return None

        q = collections.deque()
        q.append(root)

        while q:
            length = len(q)
            last_node = None
            for i in range(length):
                cur_node = q.popleft()
                if last_node:
                    last_node.next = cur_node
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)

                last_node = cur_node

        return root