# implement DFS

from collections import deque

visited = set()
    
def dfs( start, visited, graph):
    
    if start not in visited:
        visited.add(start)
        print(start, end = " ")
        
        for neighbours in graph[start]:
            dfs(neighbours, visited, graph)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}
dfs('A', visited, graph)
            
    
        