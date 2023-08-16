
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        self.lca = None
        self.search(root, p, q)
        return self.lca
    
    def search(self, root, p, q):
        if self.lca:
            return 3
        if not root:
            return 0


        left = self.search(root.left, p , q)
        right = self.search(root.right, p, q)
        
        res = 0

        if root == p:
            res = 1 
        if root == q:
            res = 1 << 1

        res = res | left | right

        if res == 3 and not self.lca:
            self.lca = root
        
        return res