from typing import List

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = {}
        for emp in employees:
            graph[emp.id] = emp
        return self.dfs(graph[id], graph)
    
    def dfs(self, emp, graph):
        if emp == None:
            return 0
        
        sum = 0

        for sub in emp.subordinates:
            sum += self.dfs(graph[sub], graph)

        return emp.importance + sum 
    
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates