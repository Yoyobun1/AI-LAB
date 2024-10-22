from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, goal):
    
    visited = set()
    queue = deque([(0,0,[])])
    
    while queue:
        jug1, jug2, path = queue.popleft()
        path.append((jug1, jug2))      
        if jug1 == goal or jug2 == goal or jug1 + jug2 == goal:
            return path        
        if (jug1, jug2) in visited:
            continue        
        
        # fill jug1
        queue.append((jug1_capacity, jug2, path.copy()))        
        #fill jug 2
        queue.append((jug1, jug2_capacity, path.copy()))     
        # empty jug 1
        queue.append((0, jug2, path.copy()))    
        # empty jug 2
        queue.append((jug1, 0, path.copy()))      
        # pour jug 1 to jug 2
        pour = min(jug1, jug2_capacity - jug2) # either pour all of jug1 to jug 2 or fill jug 2
        queue.append((jug1 - pour, jug2 + pour, path.copy()))

        # pour jug 2 to jug 1
        pour = min(jug2, jug1_capacity - jug1) # either pour all of jug2 to jug 1 or fill jug 1
        queue.append((jug1 + pour, jug2 - pour, path.copy()))
        
    return None


# Example usage
jug1_capacity = 3
jug2_capacity = 5
goal = 4

solution_path = water_jug_problem(jug1_capacity, jug2_capacity, goal)
if solution_path:
    print(f"Solution path to measure {goal} litres:")
    for step in solution_path:
        print(step)
else:
    print("No solution found.")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def water_jug_problem(jug1_capacity, jug2_capacity, goal):
    # visited = set()
    # queue = deque([(0, 0, [])])  # State includes path
    
    # while queue:
    #     jug1, jug2, path = queue.popleft()
    #     path.append((jug1, jug2))
        
    #     # Check if we have reached the goal in either jug or by combining both
    #     if jug1 == goal or jug2 == goal or jug1 + jug2 == goal:
    #         return path
        
    #     if (jug1, jug2) in visited:
    #         continue
        
    #     visited.add((jug1, jug2))
        
    #     # Fill jug1
    #     queue.append((jug1_capacity, jug2, path.copy()))
        
    #     # Fill jug2
    #     queue.append((jug1, jug2_capacity, path.copy()))
        
    #     # Empty jug1
    #     queue.append((0, jug2, path.copy()))
        
    #     # Empty jug2
    #     queue.append((jug1, 0, path.copy()))
        
    #     # Pour jug1 into jug2
    #     pour_jug1_to_jug2 = min(jug1, jug2_capacity - jug2)
    #     queue.append((jug1 - pour_jug1_to_jug2, jug2 + pour_jug1_to_jug2, path.copy()))
        
    #     # Pour jug2 into jug1
    #     pour_jug2_to_jug1 = min(jug2, jug1_capacity - jug1)
    #     queue.append((jug1 + pour_jug2_to_jug1, jug2 - pour_jug2_to_jug1, path.copy()))
    
    # return None
