import json

def read_data(file_name):
    with open(file_name) as f:
        return json.load(f)

# Read input data
graph = []
with open("graph.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        graph.append(list(map(int, line.strip().split())))

groups = read_data('groups.json')
teachers = read_data('teachers.json')
classrooms = read_data('classrooms.json')
lessons = read_data('lessons.json')

def find_smallest_available_color(adjacency_matrix, colors, vertex):
    used_colors = [False] * len(adjacency_matrix)
    
    for neighbor in range(len(adjacency_matrix[vertex])):
        if adjacency_matrix[vertex][neighbor] == 1 and colors[neighbor] != -1:
            used_colors[colors[neighbor]] = True

    for color in range(len(used_colors)):
        if not used_colors[color]:
            return color

    return -1

def hybrid_graph_coloring(adjacency_matrix):
    n = len(adjacency_matrix)
    colors = [-1] * n

    # Apply greedy algorithm for initial coloring
    for vertex in range(n):
        colors[vertex] = find_smallest_available_color(adjacency_matrix, colors, vertex)

    # Define local search function
    def local_search(current_colors):
        for vertex in range(n):
            original_color = current_colors[vertex]
            best_color = original_color
            min_conflicts = float('inf')

            for color in range(n):
                if color == original_color:
                    continue

                current_colors[vertex] = color
                conflicts = 0

                for neighbor in range(len(adjacency_matrix[vertex])):
                    if adjacency_matrix[vertex][neighbor] == 1 and current_colors[neighbor] == color:
                        conflicts += 1

                if conflicts < min_conflicts:
                    min_conflicts = conflicts
                    best_color = color

            current_colors[vertex] = best_color

    # Apply local search to improve the coloring
    local_search(colors)

    return colors

colors = hybrid_graph_coloring(graph)

for i, color in enumerate(colors):
    print(f"Task {i + 1} has color {color}")