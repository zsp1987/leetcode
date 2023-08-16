from collections import deque


class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = deque()
        res_map = {}
        min_v, max_v = 0, 0
        q.append((0, root))
        res_map.setdefault(0, []).append(root.val)

        while q:
            v, cur_node = q.popleft()
            if cur_node.left:
                q.append((v - 1, cur_node.left))
                res_map.setdefault(v-1, []).append(cur_node.left.val)
                min_v = min(min_v, v-1)
            if cur_node.right:
                q.append((v + 1, cur_node.right))
                res_map.setdefault(v+1,[]).append(cur_node.right.val)
                max_v = max(max_v, v+1)
        res = []
        for i in range(min_v, max_v+1):
            res.append(res_map.get(i))
        return res