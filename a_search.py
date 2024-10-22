from queue import PriorityQueue

def a_search(start, goal, graph, heu):
    
    queue = PriorityQueue()
    cost_so_far = {start: 0}
    came_from = {start: None}
    queue.put((0, start))
    
    while queue:
        current_cost, current_node = queue.get()
        
        if current_node == goal:
            break
        
        for neighbour,cost in graph[current_node].items():
            new_cost = cost_so_far[current_node] + cost
            
            if neighbour not in cost_so_far or new_cost < cost_so_far[neighbour]:
                cost_so_far[neighbour] = new_cost
                priority = new_cost + heu[neighbour]
                queue.put((priority, neighbour))
                came_from[neighbour] = current_node
    
    current = goal
    path = []
    while current:
        path.append(current)
        current = came_from[current]
    path.reverse()
    print(" --> ".join(path))
        
        



graph = {
    "A": {"B": 1, "C": 4},
    "B":{ "A": 1, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1, "E": 3},
    "E": {"D": 3, "F": 2},
    "F": {"E": 2}
}

heu = {
    "A": 7,
    "B": 6,
    "C": 2,
    "D": 1,
    "E": 0,
    "F": 3
}        

a_search("A", "E", graph, heu)