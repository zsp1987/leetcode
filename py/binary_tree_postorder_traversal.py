class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        self.postorder(root)
        return self.res


    def postorder(self, node):
        if not node:
            return
        
        self.postorder(node.left)
        self.postorder(node.right)
        self.res.append(node.val)