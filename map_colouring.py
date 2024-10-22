def is_valid(graph, color_map):
    for node in graph:
        if node in color_map:
            for neighbour in graph[node]:
                if neighbour in color_map and color_map[node] == color_map[neighbour]:
                    return False
    return True
    
    
def brute_force(graph, colors, color_map = {}, node = None):
    
    if len(color_map) == len(graph):
        return color_map
    
    if node is None:
        for n in graph:
            if n not in color_map:
                node = n
                break
            
    for color in colors:
        color_map[node] = color
        
        if is_valid(graph, color_map):
            result = brute_force(graph, colors)
            if result:
                return result
            
        color_map.pop(node)
    return None
                

# Example usage:
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['A', 'C']
}

colors = ['Red', 'Green', 'Blue']

coloring = brute_force(graph, colors)
print(coloring)