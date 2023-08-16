from data_type import TreeNode

class Solution(object):
    """
    leetcode 617 https://leetcode.com/problems/merge-two-binary-trees/
    """
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """

        if root1 == None and root2 == None:
            return None

        node = TreeNode((0 if root1 == None else root1.val) + (0 if root2 == None else root2.val))
        node.left = self.mergeTrees(None if root1 == None else root1.left, None if root2 == None else root2.left)
        node.right = self.mergeTrees(None if root1 == None else root1.right, None if root2 == None else root2.right)
        return node