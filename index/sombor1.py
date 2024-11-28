import numpy as np

def calculate_sombor_index(adjacency_matrix):
    # Convert adjacency matrix to numpy array for easier operations
    adjacency_matrix = np.array(adjacency_matrix)
    
    # Calculate degrees of each vertex
    degrees = np.sum(adjacency_matrix, axis=1)
    
    # Initialize Sombor index
    sombor_index = 0
    
    # Iterate over all pairs of vertices to compute the index
    num_vertices = len(adjacency_matrix)
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if adjacency_matrix[i][j] == 1:  # Check if there's an edge
                sombor_index += np.sqrt(degrees[i]**2 + degrees[j]**2)
    
    return sombor_index

# Example usage
adj_matrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]

sombor_index = calculate_sombor_index(adj_matrix)
print(f"Sombor Index: {sombor_index}")
