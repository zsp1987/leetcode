class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        self.res = ""
        
        def first_order(node):
            if not node:
                self.res = self.res + "None" + "|" + "0" + ","
                return
            children_count = len(node.children)
            self.res = self.res + str(node.val) + "|" + str(children_count) + ","
            for child in node.children:
                first_order(child)
        
        first_order(root)
        return self.res



    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        self.tokens = data[:-1].split(',')
        self.count = 0
        def first_order():
            if self.tokens[self.count].split('|')[0] == 'None':
                self.count += 1
                return None
            val_and_count = self.tokens[self.count].split('|')
            val_str = val_and_count[0]
            count_str = val_and_count[1]
            val, count = int(val_str), int(count_str)
            node = TreeNode()
            self.count += 1
            node.val = val
            node.children = []
            for _ in range(count):
                node.children.append(first_order())
            
            return node
        
        root = first_order()
        return root