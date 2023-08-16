from collections import deque
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = {}

        def build_graph(node, graph):
            if not node:
                return
            if node.left:
                graph.setdefault(node.val, []).append(node.left.val)
                graph.setdefault(node.left.val, []).append(node.val)
                build_graph(node.left, graph)
            if node.right:
                graph.setdefault(node.val, []).append(node.right.val)
                graph.setdefault(node.right.val, []).append(node.val)
                build_graph(node.right, graph)

        build_graph(root, graph)

        q = deque()
        q.append(target.val)
        level = 0
        res = []
        visited = set()

        while q:
            count = len(q)
            for i in range(count):
                cur = q.popleft()
                visited.add(cur)
                if level == k:
                    res.append(cur)
                    continue
                for next_node in graph.get(cur, []):
                    if next_node not in visited:
                        q.append(next_node)
            level = level + 1

        return res 