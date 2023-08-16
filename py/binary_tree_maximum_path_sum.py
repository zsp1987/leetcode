class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.max = root.val
        self.recurse(root)
        return self.max

    def recurse(self, node):
        if not node:
            return 0
        left_sum = max(0, self.recurse(node.left))
        right_sum = max(0, self.recurse(node.right))

        self.max = max(self.max, node.val + left_sum + right_sum)
        return node.val + max(left_sum, right_sum)
