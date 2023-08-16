class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self.check(root, None, None)

    def check(self, node, lmin, lmax):
        if not node:
            return True
        if lmin != None and node.val <= lmin:
            return False
        if lmax != None and node.val >= lmax:
            return False

        return self.check(node.left, lmin, node.val) and self.check(node.right, node.val, lmax)


class Solution2(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def check(node):
            valid, lmin, lmax = True, node.val, node.val

            if node.left:
                left_valid, left_min, left_max = check(node.left)
                valid = valid and left_valid and node.val > left_max
                lmin = left_min

            if node.right:
                right_valid, right_min, right_max = check(node.right)
                valid = valid and right_valid and node.val < right_min
                lmax = right_max

            return valid, lmin, lmax

        res, _, _ = check(root)
        return res
