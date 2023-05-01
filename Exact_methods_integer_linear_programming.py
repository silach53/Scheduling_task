import gurobipy as gp
from gurobipy import GRB
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

def solve_graph_coloring_ilp(graph, max_colors):
    n = len(graph)

    try:
        # Create a Gurobi environment and model
        env = gp.Env()
        model = gp.Model(env=env)

        # Create binary decision variables x[i][j]
        x = [[model.addVar(vtype=GRB.BINARY, name=f"x_{i}_{j}") for j in range(max_colors)] for i in range(n)]

        # Add constraint: each vertex must have exactly one color
        for i in range(n):
            model.addConstr(sum(x[i][j] for j in range(max_colors)) == 1, f"vertex_{i}")

        # Add constraint: adjacent vertices must have different colors
        for i in range(n):
            for j in range(i + 1, n):
                if graph[i][j]:
                    for k in range(max_colors):
                        model.addConstr(x[i][k] + x[j][k] <= 1, f"edge_{i}_{j}_color_{k}")

        # Set the objective function to minimize the number of colors
        obj = gp.quicksum(x[i][j] for j in range(max_colors) for i in range(n))
        model.setObjective(obj, GRB.MINIMIZE)

        # Solve the ILP problem
        model.optimize()

        # Retrieve the optimal vertex colors
        colors = [0] * n
        for i in range(n):
            for j in range(max_colors):
                if x[i][j].x > 0.5:
                    colors[i] = j + 1
                    break

        return colors

    except gp.GurobiError as e:
        print(f"Error code: {e.errno}")
        print(e.message)
    except:
        print("Unknown exception caught")

    return []

max_colors = 4

# Solve the graph coloring problem using ILP
colors = solve_graph_coloring_ilp(graph, max_colors)

# Print color assignments
for i, color in enumerate(colors):
    print(f"Task {i + 1} has color {color}")
