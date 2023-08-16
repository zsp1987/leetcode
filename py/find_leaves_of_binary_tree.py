class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.res = []
        self.recurse(root)
        return self.res

    
    def recurse(self, node):
        if not node:
            return -1
        
        left_height = self.recurse(node.left)
        right_height = self.recurse(node.right)

        cur_height = max(left_height, right_height) + 1

        if (len(self.res) == cur_height):
            self.res.append([])

        self.res[cur_height].append(node.val)
        return cur_height

class Solution1(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.visited = set()
        self.res = []
        while not root in self.visited:
            leaves = []
            self.recurse(root, leaves)
            self.res.append(leaves)
        return self.res

    
    def recurse(self, node, leaves):
        if not node or node in self.visited:
            return
        if (not node.left or node.left in self.visited) and (not node.right or node.right in self.visited):
            leaves.append(node.val)
            self.visited.add(node)
        self.recurse(node.left, leaves)
        self.recurse(node.right, leaves)