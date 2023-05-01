# Graph Coloring Project

This project uses Integer Linear Programming (ILP) to solve the graph coloring problem. The input is a graph represented by an adjacency matrix, and the goal is to assign colors to the vertices such that no two adjacent vertices share the same color. The solution minimizes the number of colors used.

## Requirements

- Python 3.6 or higher
- Gurobi Optimizer with Python interface (gurobipy)

To install the Gurobi Python interface, run:

```

pip install gurobipy

```
markdownCopy code
## Input Data

The input data for the graph coloring problem consists of the following files:

1. `graph.txt`: A text file containing the adjacency matrix representation of the graph. Each row is a list of space-separated integers, where '1' represents an edge between two vertices, and '0' represents no edge.
2. `groups.json`: A JSON file containing information about the groups.
3. `teachers.json`: A JSON file containing information about the teachers.
4. `classrooms.json`: A JSON file containing information about the classrooms.
5. `lessons.json`: A JSON file containing information about the lessons.

## Running the Script

To run the script, execute the following command:

```

python graph_coloring_ilp.py

```
scssCopy code

The output will display the color assignments for each task (vertex) in the graph.

## License

This project is released under the [MIT License](https://opensource.org/licenses/MIT).

This README.md file provides a brief overview of the graph coloring project, its requirements, input data, instructions for running the script, and the license information.