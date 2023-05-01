import json
import random
import math

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

def is_valid_coloring(graph, colors):
    for u in range(len(graph)):
        for v in range(len(graph)):
            if graph[u][v] and colors[u] == colors[v]:
                return False
    return True

def count_colors(colors):
    return len(set(colors))

def simulated_annealing(graph, max_colors, max_iterations, initial_temperature, cooling_rate):
    n = len(graph)
    colors = [random.randint(1, max_colors) for _ in range(n)]

    temperature = initial_temperature
    best_colors = colors.copy()
    best_color_count = count_colors(colors)

    for iteration in range(max_iterations):
        new_colors = colors.copy()
        vertex = random.randrange(n)
        new_color = random.randint(1, max_colors)
        new_colors[vertex] = new_color

        if is_valid_coloring(graph, new_colors):
            new_color_count = count_colors(new_colors)
            color_diff = new_color_count - best_color_count

            if color_diff < 0 or random.random() < math.exp(-color_diff / temperature):
                colors = new_colors

                if new_color_count < best_color_count:
                    best_colors = new_colors.copy()
                    best_color_count = new_color_count

        temperature *= 1 - cooling_rate

    return best_colors

max_colors = 5
max_iterations = 10000
initial_temperature = 1000
cooling_rate = 0.003

colors = simulated_annealing(graph, max_colors, max_iterations, initial_temperature, cooling_rate)

# Print color assignments
for i, color in enumerate(colors):
    print(f"Task {i + 1} has color {color}")
