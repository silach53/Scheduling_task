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

# Welsh-Powell algorithm to solve the graph coloring problem
def welsh_powell(graph):
    n = len(graph)
    degrees = [(i, sum(row)) for i, row in enumerate(graph)]

    # Sort the vertices by descending degree
    degrees.sort(key=lambda x: x[1], reverse=True)

    color = [0] * n
    c = 1  # Initialize the first color
    for i in range(n):
        u = degrees[i][0]
        if color[u] == 0:  # If the vertex has not been colored yet
            color[u] = c

            # Color all uncolored vertices that are not adjacent to the current vertex
            for j in range(i + 1, n):
                v = degrees[j][0]
                if color[v] == 0 and not graph[u][v]:
                    can_color = True
                    for k in range(n):
                        if graph[v][k] and color[k] == c:
                            can_color = False
                            break
                    if can_color:
                        color[v] = c
            c += 1  # Increment the color for the next group of vertices

    return color

color = welsh_powell(graph)

# Print color assignments
for i in range(len(color)):
    print(f"Task {i + 1} has color {color[i]}")