from collections import deque


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        res = []
        q = deque()
        q.append(root)

        while q:
            count = len(q)
            for i in range(count):
                cur = q.popleft()
                if i == count - 1:
                    res.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

        return res
