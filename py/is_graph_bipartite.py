from collections import deque


class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        nodes = deque()

        color = {}
        visited = {}
        cur_color = 0
        
        for i in range(n):
            if i not in visited:
                nodes.append(i)
                while nodes:
                    count = len(nodes)
                    for i in range(count):
                        node = nodes.popleft()
                        visited[node] = True
                        color[node] = cur_color
                        for next_node in graph[node]:
                            if next_node in color and color[next_node] == cur_color:
                                return False
                            if next_node not in visited:
                                nodes.append(next_node)
                    cur_color = 0 if cur_color == 1 else 1
        return True