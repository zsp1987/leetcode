class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.res = ""
        def pre_order(node):
            if not node:
                self.res = self.res + "None" + ","
            else:
                self.res = self.res + str(node.val) + ","
                pre_order(node.left)
                pre_order(node.right)
        pre_order(root)
        print(self.res)
        return self.res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.tokens = data[:-1].split(",")
        self.count = 0
        def pre_order():
            if self.tokens[self.count] == 'None':
                self.count = self.count + 1
                return None
            node = TreeNode()
            node.val = int(self.tokens[self.count])
            self.count = self.count + 1
            node.left = pre_order()
            node.right = pre_order()
            return node
        root = pre_order()
        return root