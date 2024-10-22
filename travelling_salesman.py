import itertools

# Function to calculate the total distance for a given path
def calculate_distance(path, distance_matrix):
    total_distance = 0
    num_cities = len(path)
    
    # Calculate the total distance by adding the distance between consecutive cities
    for i in range(num_cities - 1):
        total_distance += distance_matrix[path[i]][path[i + 1]]
    
    # Add distance to return to the starting city
    total_distance += distance_matrix[path[-1]][path[0]]  # Return to the starting city
    return total_distance

# Brute-force solution for TSP
def tsp_brute_force(distance_matrix):
    cities = list(range(len(distance_matrix)))  # List of city indices (e.g., [0, 1, 2, 3])
    
    # Generate all possible permutations of cities
    all_permutations = itertools.permutations(cities)
    
    # Initialize minimum distance to a large number and best path as None
    min_distance = float('inf')
    best_path = None

    # Iterate over all possible paths (permutations)
    for path in all_permutations:
        current_distance = calculate_distance(path, distance_matrix)
        
        # If the current distance is smaller than the known minimum, update the best path and distance
        if current_distance < min_distance:
            min_distance = current_distance
            best_path = path

    return best_path, min_distance

# Example usage
distance_matrix = [
    [0, 10, 15, 20],  # Distances from city 0
    [10, 0, 35, 25],  # Distances from city 1
    [15, 35, 0, 30],  # Distances from city 2
    [20, 25, 30, 0]   # Distances from city 3
]

# Call the brute-force TSP solver
best_path, min_distance = tsp_brute_force(distance_matrix)

# Output the best path and the minimum distance
print("Best Path:", best_path)
print("Minimum Distance:", min_distance)
