from collections import deque

# Define the graph as a dictionary of nodes and their neighbors
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

# Define the heuristic values as a dictionary
heu = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 0
}

def get_heu(node):
    return heu[node]

def greedy_bfs(start, goal, graph, heu):
    queue = deque([start])
    visited = set()
    
    while queue:
        current_node = queue.popleft()
        
        if current_node in visited:
            continue
        
        print(f"current node: {current_node}")
        visited.add(current_node)
        
        if current_node == goal:
            print("Goal reached")
            return
        
        sorted_graph = sorted(graph[current_node], key=get_heu)
        
        for neighbour in sorted_graph:
            if neighbour not in visited:
                
                queue.append(neighbour)
                
    print("Goal not reachable")
        
    
    queue = deque([start])
    visited = set()
    
    while queue:
        
        current_node = queue.popleft()
        
        if current_node in visited:
            continue
        
        print(f"current node: {current_node}") 
        visited.add(current_node)
        
        if current_node == goal:        
            print("Goal reached")
            return
        
        sorted_graph = sorted(graph[current_node], key=get_heu)
        
        for neighbours in sorted_graph:
            if neighbours not in visited:
                queue.append(neighbours)
                
    print("Goal not reachable")

        
    # Perform Greedy BFS
greedy_bfs('A', 'D', graph, heu)