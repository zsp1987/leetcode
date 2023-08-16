from collections import defaultdict


class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        self.fromGraph(n, connections)
        self.dfs(0, 0)

        result = []
        for u, v in self.conn_dict:
            result.append([u, v])

        return result

    def dfs(self, node, discovery_rank):
        if self.rank[node]:
            return self.rank[node]

        self.rank[node] = discovery_rank
        min_rank = discovery_rank + 1
        for neighbor in self.graph[node]:
            if self.rank[neighbor] and self.rank[neighbor] == discovery_rank - 1:
                continue

            recursive_rank = self.dfs(neighbor, discovery_rank + 1)

            if recursive_rank <= discovery_rank:
                del self.conn_dict[(min(node, neighbor), max(node, neighbor))]

            min_rank = min(min_rank, recursive_rank)

        return min_rank

    def fromGraph(self, n, connections):
        self.rank = {}
        self.graph = defaultdict(list)
        self.conn_dict = {}

        for i in range(n):
            self.rank[i] = None

        for edge in connections:
            u, v = edge[0], edge[1]
            self.graph[u].append(v)
            self.graph[v].append(u)

            self.conn_dict[(min(u, v), max(u, v))] = 1
