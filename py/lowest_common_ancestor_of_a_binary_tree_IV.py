class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        node_set = set(nodes)

        def recurse(root):
            if not root:
                return None
            if root in node_set:
                return root
            
            left = recurse(root.left)
            right = recurse(root.right)
    
            if left and right:
                return root
            
            return left or right
        
        return recurse(root)