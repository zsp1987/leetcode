class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        :leetcode: 663
        :url: https://leetcode.com/problems/equal-tree-partition/
        """
        sums = set()
        sum = root.val + self.dfs(root.left, sums) + \
              self.dfs(root.right, sums)
        return sum % 2 == 0 and (sum / 2) in sums

    def dfs(self, root, sums):
        if (root == None):
            return 0

        sum = root.val + self.dfs(root.left, sums) + \
              self.dfs(root.right, sums)
        sums.add(sum)
        return sum
