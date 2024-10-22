# implement bfs using a queue
from collections import deque

def bfs(graph, start):
    #adding start node to queue and visited list
    queue = deque([start])
    visited = set([start])
    
    while queue:
        currend_node = queue.popleft()
        print(f"{currend_node}", end =" ")
        
        for neighbour in graph[currend_node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph, 'A')
    
    
    
